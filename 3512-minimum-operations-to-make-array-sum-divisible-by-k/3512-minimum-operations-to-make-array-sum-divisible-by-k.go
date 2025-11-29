func minOperations(nums []int, k int) int {
    sum := 0
    for i := 0; i<len(nums); i++ {
        sum+=nums[i]
    }
    return sum%k
}