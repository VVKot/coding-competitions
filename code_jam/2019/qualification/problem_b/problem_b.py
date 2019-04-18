rr = lambda: input().strip()
rri = lambda: int(rr())

def solve(path):
    result = ""
    for ch in path:
        if ch == "S":
            result += "E"
        else:
            result += "S"
    return result

T = rri()
for tc in range(1, T+1):
    P = rri()
    path = rr()
    res = solve(path)
    print("Case #{}: {}".format(tc, res))
