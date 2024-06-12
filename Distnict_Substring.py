# cook your dish here
def is_k_terms_reachable(total, terms_needed):
    sum_so_far, count, next_increment = 1, 1, 3
    
    while sum_so_far <= total:
        sum_so_far += next_increment
        count += 1
        next_increment += 1
    
    return count - 1 >= terms_needed

test_cases = int(input())
for _ in range(test_cases):
    total, terms_needed = map(int, input().split())
    result = "YES" if is_k_terms_reachable(total, terms_needed) else "NO"
    print(result)