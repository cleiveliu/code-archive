use std::error::Error;
use std::fs;

pub struct Config {
    pub query: String,
    pub filename: String,
    pub case_sensitive: bool,
}

impl Config {
    pub fn new(mut args: std::env::Args /*args: &[String]*/) -> Result<Config, &'static str> {
        args.next();

        let query = match args.next() {
            Some(arg) => arg,
            None => return Err("Didn't get query string"),
        };

        let filename = match args.next() {
            Some(arg) => arg,
            None => return Err("Didn't get a filename"),
        };

        let case_sensitive = match args.next() {
            Some(arg) => {
                if arg.to_lowercase() == "y" {
                    true
                } else {
                    false
                }
            }
            None => false,
        };

        return Ok(Config {
            query,
            filename,
            case_sensitive,
        });

        /*
        if args.len() < 3 {
            return Err("Not enough args");
        }

        let query = args[1].clone();
        let filename = args[2].clone();

        let case_sensitive = if args.len() > 3 && args[3].to_lowercase() == "y" {
            true
        } else {
            false
        };

        return Ok( Config { query, filename, case_sensitive } );
        */
    }
}

pub fn run(config: Config) -> Result<(), Box<dyn Error>> {
    let contents = fs::read_to_string(config.filename)?;
    //.expect("Something WQrong here");
    //println!("The {}'s content is :\n\n\n   {}\n\n",config.filename, contents);
    let ret = if config.case_sensitive {
        search(&config.query, &contents)
    } else {
        search_case_insensitive(&config.query, &contents)
    };
    for line in ret {
        println!("{}", line);
    }
    return Ok(());
}

fn search<'a>(query: &str, contents: &'a str) -> Vec<&'a str> {
    contents
        .lines()
        .filter(|line| line.contains(query))
        .collect()
    /*
    let mut ret = Vec::new();
    for line in contents.lines() {
        if line.contains(query) {
            ret.push(line);
        }
    }
    return ret;
    */
}

fn search_case_insensitive<'a>(query: &str, contents: &'a str) -> Vec<&'a str> {
    //let query = query.to_lowercase();

    contents
        .lines()
        .filter(|line| line.to_lowercase().contains(&query.to_lowercase()))
        .collect()

    /*
    let query = query.to_lowercase();
    let mut ret = Vec::new();
    for line in contents.lines() {
        if line.to_lowercase().contains(&query) {
            ret.push(line);
        }
    }
    return ret;
    */
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn one_result() {
        let query = "duct";
        let contents = "\
Rust:
safe,fast,productive,
Pick three.";
        assert_eq!(vec!["safe,fast,productive,"], search(query, contents));
    }
    #[test]
    fn case_insensitive() {
        let query = "rUst";
        let contents = "\
Rust:
safe,fast,productive.
Pick three.
Trust me.";
        assert_eq!(
            vec!["Rust:", "Trust me."],
            search_case_insensitive(query, contents)
        );
    }
}
