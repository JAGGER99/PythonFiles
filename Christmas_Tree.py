def holidaybush(n):
    x = 1
    for i in range(n):
        print(' ' * n + '*' * x + ' ' * n)
        x+=2
        n-=1
        
        
holidaybush(5)