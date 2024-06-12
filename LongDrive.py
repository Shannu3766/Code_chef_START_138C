for i in range(int(input())):
    a,b=map(int,input().split())
    print((10*(b-a)+(100-b)-1)//(100-b))