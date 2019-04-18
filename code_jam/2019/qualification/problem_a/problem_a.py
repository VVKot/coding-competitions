rr = lambda: input().strip()
rri = lambda: int(rr())

def solve(num):
    str_num = str(num)
    a, b = "", ""
    for ch in str_num:
        if ch == "4":
            a += "3"
            b += "1"
        else:
            a += ch
            b += "0"
    return int(a), int(b)

T = rri()
for tc in range(1, T+1):
    N = rri()
    a, b = solve(N)
    print("Case #{}: {} {}".format(tc, a, b))
