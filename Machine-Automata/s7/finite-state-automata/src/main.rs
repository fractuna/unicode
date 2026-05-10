/* A simple Finite State Automata Machine For Learning Purposes */

use std::collections::HashMap;

struct Machine {}

fn init_machine() -> HashMap<char, Vec<i32>> {
    let mut machine: HashMap<char, Vec<i32>> = HashMap::new();

    machine.insert('a', vec![0]);
    machine.insert('b', vec![1]);
    machine.insert('b', vec![2]);

    machine
}

fn main() {
    // Main Machine Structure
    let mut machine: HashMap<char, Vec<i32>> = init_machine();

    // The main machine stack
    let mut index_pointer: i32 = 0;

    let w: &'static str = "abaa";

    let w_array = w.chars();

    for (index, chr) in w_array.enumerate() {
        print!("Running machine on: {} character...", chr);
        let chr_opt: Option<&Vec<i32>> = machine.get(&chr);
        if let None = chr_opt {
            println!("\nThis character is not inside the machines alphabet!\nEND (faild)");
            break;
        }

        let transitions: &Vec<i32> = chr_opt.unwrap();

        for (i, v) in transitions.iter().enumerate() {
            index_pointer += 1
        }
    }

    // println!("Hello, world!");
}
