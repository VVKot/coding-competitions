package largestTimeFromDigits

func repeatedSubstringPattern(s string) bool {
	sLen := len(s)
	for i := 1; i <= sLen/2; i++ {
		if sLen%i != 0 {
			continue
		}
		var candidate string
		for j := 0; j < sLen/i; j++ {
			candidate += s[:i]
		}
		if candidate == s {
			return true
		}
	}
	return false
}
