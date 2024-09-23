n =  int(input("Enter the size of the pattern:"))

row = 0
while row < n:
    for i in range(n):
        print("*", end='')
    print()
    row+=1
