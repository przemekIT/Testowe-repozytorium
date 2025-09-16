from functools import lru_cache


@lru_cache(maxsize=None)
def count_paths(n, m, start_n: int=1, start_m: int=1):
    if start_n == n and start_m == m:
        return 1
    if start_n > n or start_m > m:
        return 0
    
    return count_paths(n, m, start_n+1, start_m) + count_paths(n, m, start_n, start_m+1)
    
print(count_paths(4,4))