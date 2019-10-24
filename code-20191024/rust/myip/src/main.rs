extern crate actix_web;

use actix_web::{server, App, HttpRequest};

fn index(req: &HttpRequest) -> String {
    let conn = req.connection_info();
    let ip = conn.remote().unwrap();
    let v: Vec<&str> = ip.split(":").collect();
    let mut ret = String::from(v[0]);
    ret.push_str("fuck from rust");
    ret
}

fn main() {
    let addr = "0.0.0.0:10000";
    println!("Sever listening at {}", addr);
    server::new(||App::new().resource("/",|r| r.f(index)))
        .bind(addr)
        .expect("can not bind to port 10000")
        .run()
}