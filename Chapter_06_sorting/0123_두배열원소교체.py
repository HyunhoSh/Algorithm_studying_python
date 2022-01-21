n, k = map(int, input().split())


a_list = list(map(int,input().split()))
b_list = list(map(int, input().split()))

a_list.sort()
b_list.sort()

for i in range(k):
    minimum = a_list[i]
    maximum = b_list[-(i+1)]
    if minimum<maximum:
        a_list[i], b_list[-(i+1)] = b_list[-(i+1)], a_list[i]

result = 0
for i in a_list:
    result+=i

print(result) 
