print('input 6 integers')
num=list(map(int,input().split()))
num.sort()
print('after sorting the said integers',num)
print(*num)