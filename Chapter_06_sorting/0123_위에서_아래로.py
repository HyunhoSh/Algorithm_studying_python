n = int(input())

m_list = []
for i in range(n):
    k = int(input())
    m_list.append(k)

for i in sorted(m_list,reverse=True):
    print(i, end=' ')