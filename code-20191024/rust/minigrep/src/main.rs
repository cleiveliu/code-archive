use std::env;
use std::process;

use minigrep;
use minigrep::run;
use minigrep::Config;

fn main() {
    //let args: Vec<String> = env::args().collect();

    let config = Config::new(env::args() /*&args*/).unwrap_or_else(|err| {
        eprintln!("Problem parsing arguments: {}", err);
        process::exit(1);
    });

    //println!("Search {} in {}\n\n",config.query,config.filename);
    if let Err(e) = run(config) {
        eprintln!("Applicating error: {}", e);
        process::exit(1);
    }
    //println!("{:?}",args);
}

/*
fn run(config: Config) -> Result<(),Box<dyn Error>> {
    let contents = fs::read_to_string(config.filename.clone())?;
        //.expect("Something WQrong here");
    println!("The {}'s content is :\n\n\n   {}\n\n",config.filename, contents);

    return Ok(());
}
*/

/*
struct Config {
    query: String,
    filename: String,
}

impl Config {
    fn new(args: &[String]) -> Result<Config,&'static str> {
        if args.len() < 3 {
            return Err("Not enough args");
        }

        let query = args[1].clone();
        let filename = args[2].clone();

        return Ok( Config { query, filename} );
    }
}
*/

/*
fn parse_config(args: &[String]) -> Config {
    let query = args[1].clone();
    let filename = args[2].clone();

    Config {query, filename}
}
*/
