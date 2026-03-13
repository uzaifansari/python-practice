# CREATING A 2D ARRAY/LIST
rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

matrix = []

for i in range(rows):
    row = []
    for j in range(columns):
        elem = input(f"Enter the element for Row {i+1}, Column {j+1}: ")
        row.append(elem)
    matrix.append(row)

for r in matrix:
    print(r)