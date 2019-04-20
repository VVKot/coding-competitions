def calculate_suffix_sums(grants):
    N = len(grants)
    result = [None] * N
    for i in range(N-1, -1, -1):
        num = grants[i]
        if i == N-1:
            result[i] = (num, num)
        else:
            _, prev = result[i+1]
            total = num + prev
            result[i] = (num, total)
    return result

def calculate_grants_cap(grants_array, new_budget):
    N = len(grants_array)
    for i in range(1, N):
        curr_grant, total = grants_array[i]
        new_total = total + curr_grant * i
        if new_total <= new_budget:
            diff = (new_budget-new_total) / float(i)
            result = curr_grant + diff
            return result
    return 1.0 * new_budget / float(N)


def find_grants_cap(grants_array, new_budget):
    if not grants_array:
        return 0
    if sum(grants_array) < new_budget:
        return max(grants_array)
    grants_array.sort(reverse=True)
    grants = calculate_suffix_sums(grants_array)
    return calculate_grants_cap(grants, new_budget)
