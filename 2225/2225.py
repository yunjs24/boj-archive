print(__import__('math').comb(
    *map(int,(
        lambda n,k:[n+k-1,k-1])(*map(int,input().split()))
    )
)%1000000000)