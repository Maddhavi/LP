R1=int(input("Enter the num of rows: "))

rows = R1
for i in range(rows):
    for j in range(i):
        print(i, end=' ')
    print('')
