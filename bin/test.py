arr = [[2, 0, 0, 4],
       [0, 4, 2, 0],
       [0, 0, 4, 2],
       [8, 0, 0, 0]]

# Determine the direction of the shift (left, right, up, or down)
direction = "left"

# Iterate over each row of the array and move the cells in the desired direction
for row in arr:
    # Move cells to the left
    if direction == "left":
        # Remove any zeros in the row
        row = [cell for cell in row if cell != 0]
        # Add zeros to the end of the row
        row += [0] * (4 - len(row))
    # Move cells to the right
    elif direction == "right":
        # Remove any zeros in the row
        row = [cell for cell in row if cell != 0]
        # Add zeros to the beginning of the row
        row = [0] * (4 - len(row)) + row
    # Move cells up
    elif direction == "up":
        # Transpose the array
        arr = [[row[i] for row in arr] for i in range(4)]
        # Remove any zeros in the row
        row = [cell for cell in row if cell != 0]
        # Add zeros to the end of the row
        row += [0] * (4 - len(row))
        # Assign the new row back to the column
        for i in range(4):
            arr[i][row_index] = row[i]
        # Transpose the array back to its original shape
        arr = [[arr[i][j] for i in range(4)] for j in range(4)]
    # Move cells down
    elif direction == "down":
        # Transpose the array
        arr = [[row[i] for row in arr] for i in range(4)]
        # Remove any zeros in the row
        row = [cell for cell in row if cell != 0]
        # Add zeros to the beginning of the row
        row = [0] * (4 - len(row)) + row
        # Assign the new row back to the column
        for i in range(4):
            arr[i][row_index] = row[i]
        # Transpose the array back to its original shape
        arr = [[arr[i][j] for i in range(4)] for j in range(4)]

# Replace the cells that have been shifted with zeros
for i in range(4):
    for j in range(4):
        if arr[i][j] == None:
            arr[i][j] = 0

print (arr)