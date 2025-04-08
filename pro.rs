struct Programmer {
name: String,
branch:String,
College: String,
rollno: u32,
year: String

}
fn main() {
let value = Programmer {
	name: String::from("ANUHYA BELLAMKONDA"),
	branch: String::from("CSE(AIML)"),
	College: String::from("Nalla Malla Reddy Engineering College"),
	rollno: 608,
	year:String::from("3rd year"),

};
println!("{} of {} bearing StudentID {} of {} in {}",
	value.name,
	value.branch,
	value.rollno,
	value.year,
	value.College,
	);
}
