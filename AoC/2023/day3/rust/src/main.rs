/* Incomplete rust attempt */

use std::io::{self, Read};

fn main() {
    let mut buffer = String::new();
 
    let _ = io::stdin().read_to_string(&mut buffer);

    let lines = buffer.split("\n");
    let mut n = 0;

    let mut matrix = Vec::<String>::new();

    for line in lines {
        n += 1;
        let m = line.len();
        matrix.push(line.to_string());
    }


}
