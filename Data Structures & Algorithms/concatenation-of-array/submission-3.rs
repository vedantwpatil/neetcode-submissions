impl Solution {
    pub fn get_concatenation(nums: Vec<i32>) -> Vec<i32> {
        let length = nums.len(); 
        let mut ans = vec![0; 2*length];

        for i in 0..length{
            ans[i] = nums[i];
            ans[i+length] = nums[i];
        }
        ans
    }
}
