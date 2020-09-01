package largestTimeFromDigits

import (
	"fmt"
)

func largestTimeFromDigits(A []int) string {
	possiblePermutations := permutations(A)
	maxTime := -1

	for _, permutation := range possiblePermutations {
		hours := permutation[0]*10 + permutation[1]
		minutes := permutation[2]*10 + permutation[3]
		if hours < 24 && minutes < 60 {
			maxTime = Max(maxTime, hours*60+minutes)
		}
	}

	if maxTime == -1 {
		return ""
	} else {
		return fmt.Sprintf("%02d:%02d", maxTime/60, maxTime%60)
	}
}

func Max(x, y int) int {
	if x < y {
		return y
	}
	return x
}

func permutations(arr []int) [][]int {
	var helper func([]int, int)
	res := [][]int{}

	helper = func(arr []int, n int) {
		if n == 1 {
			tmp := make([]int, len(arr))
			copy(tmp, arr)
			res = append(res, tmp)
		} else {
			for i := 0; i < n; i++ {
				helper(arr, n-1)
				if n%2 == 1 {
					tmp := arr[i]
					arr[i] = arr[n-1]
					arr[n-1] = tmp
				} else {
					tmp := arr[0]
					arr[0] = arr[n-1]
					arr[n-1] = tmp
				}
			}
		}
	}
	helper(arr, len(arr))
	return res
}
