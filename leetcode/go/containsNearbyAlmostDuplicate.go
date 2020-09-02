package largestTimeFromDigits

func containsNearbyAlmostDuplicate(nums []int, k int, t int) bool {
	for i, num := range nums {
		for j := i + 1; j <= i+k; j++ {
			if j >= len(nums) {
				break
			}
			if Abs(num-nums[j]) <= t {
				return true
			}
		}
	}
	return false
}

func Abs(a int) int {
	if a < 0 {
		return -a
	}
	return a
}
