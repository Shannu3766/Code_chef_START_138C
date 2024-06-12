def solution():
    n, q = list(map(int, input().split()))
    a = list(map(lambda x: int(x)-1, input().split()))
    p_x = [list(map(lambda x: int(x)-1, input().split())) for _ in range(q)]
    cnt = [0]*n
    total = 0
    for x in a:
        cnt[x] += 1
        total += cnt[x]
    result = []
    for p, x in p_x:
        total -= cnt[a[p]]
        cnt[a[p]] -= 1
        a[p] = x
        cnt[a[p]] += 1
        total += cnt[a[p]]
        result.append(total)
    return "\n".join(map(str, result))

print(solution())