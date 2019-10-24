
fn avg(nums:&[f64])->f64{
    let sum = sum(nums);
    let len = len(nums);
    sum/len
}
fn sum(nums:&[f64])-> f64{
    let mut res=0f64;
    for i in nums.iter(){
        res += i;
    }
    res
}
fn len(nums:&[f64]) -> f64{
    let mut res = 0f64;
    for _i in nums.iter(){
        res += 1f64;
    }
    res
}

fn main(){
    let nums=[100f64;10];
    print!("{}",avg(&nums));
}