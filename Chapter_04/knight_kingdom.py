import sys

n = str(sys.stdin.readline())

# 8가지 방법
dxs = [-2,-2,2,2,-1,-1,1,1]
dys = [-1,1,-1,1,-2,2,2,-2]

def can_go(x,y):
    return x<=8 and x>=1 and y<=8 and y>=1

list_n = list(n)

x = list_n[1]
y = list_n[0]

# print(ord(y)-ord('a')+1)

cnt = 0

for dx, dy in zip(dxs,dys):
    nx = int(x)+dx
    ny = ord(y)-ord('a')+1+dy

    if can_go(nx,ny):
        cnt+=1

print(cnt)





