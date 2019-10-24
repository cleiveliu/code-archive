use std::fs::File;
use std::io;
use std::io::Read;

fn read_from_file(filename: &str) -> Result<String, io::Error> {
    let f = File::open(filename);

    let mut f = match f {
        Ok(file) => file,
        Err(e) => return Err(e),
    };

    let mut s = String::new();

    match f.read_to_string(&mut s) {
        Ok(_) => Ok(s),
        Err(e) => Err(e),
    }
}

fn main() {
    let s = read_from_file("./hello.txt");
    let s = match s {
        Ok(s) => s,
        Err(_e) => panic!("Here you know"),
    };
    print!("{}", s);
}
