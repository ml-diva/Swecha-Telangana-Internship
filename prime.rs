
fn is_prime(n: u32) -> bool {
    if n < 2 
    {
        return false;
    }
    for i in 2..(n / 2 + 1) 
    {
        if n % i == 0
        {
            return false;
        }
    }
    true
}

fn main() {
    for num in 1..1001 {
        if is_prime(num) {
            println!("{}", num);
     }
    }
}
