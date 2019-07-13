def diff_strings_rec(source, target, dp={}):
    dp_key = (source, target)
    if dp_key in dp:
        return dp[dp_key]
    if not source and not target:
        result = []
        dp[dp_key] = (0, result)
        return dp[dp_key]
    if not source:
        result = ["+" + ch for ch in target]
        dp[dp_key] = (len(target), result)
        return dp[dp_key]
    if not target:
        result = ["-" + ch for ch in source]
        dp[dp_key] = (len(source), result)
        return dp[dp_key]
    if source[0] == target[0]:
        result = [source[0]]
        num_edits, edits = diff_strings_rec(source[1:], target[1:], dp)
        result.extend(edits)
        dp[dp_key] = (num_edits, result)
        return dp[dp_key]
    else:
        num_edits_del, edits_del = diff_strings_rec(source[1:], target, dp)
        num_edits_ins, edits_ins = diff_strings_rec(source, target[1:], dp)
        if num_edits_ins < num_edits_del:
            result = ["+" + target[0]]
            result.extend(edits_ins)
            dp[dp_key] = (num_edits_ins + 1, result)
            return dp[dp_key]
        else:
            result = ["-" + source[0]]
            result.extend(edits_del)
            dp[dp_key] = (num_edits_del + 1, result)
            return dp[dp_key]


def diffBetweenTwoStrings(source, target):
    _, edits = diff_strings_rec(source, target)
    return edits
