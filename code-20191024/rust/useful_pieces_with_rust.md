- # read the doc
```bash
rustup doc --std
```
```rust

#![allow(unused_variables)]
fn main() {
for s in vec.iter() {...} // &String
for s in vec.iter_mut() {...} // &mut String
for s in vec.into_iter() {...} // String

// 隐式!
for s in &vec {...} // &String
for s in &mut vec {...} // &mut String
for s in vec {...} // String
}
```