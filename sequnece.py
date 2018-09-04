n = int(input("Enter the length of the sequence: ")) # Do not change this line

sum = 0
n1 = 1
n2 = 2
n3 = 3

for i in range (1, n+1):
    if i == 1:
        print(i)
        continue
    elif i == 2:
        print(i)
        continue
    elif i == 3:
        print(i)
        continue
    sum = n1 + n2 + n3
    n1 = n2
    n2 = n3
    n3 = sum
    print(sum)
