l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = [0]*(len(l1)+len(l2))

for i in range(len(l3)):
    for k in range(2):
        k += i
        l3[i] = l1[i]
        l3[k] = l2[k - i]
print(l3)