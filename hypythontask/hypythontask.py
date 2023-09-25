first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []

# Read the matrix
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

result = ''  # Initialize result as an empty string

# Process each column and concatenate alphanumeric characters with single spaces
result = ' '.join([''.join([' ' * (not c.isalnum() or (not result or result[-1] != ' ')) + c for c in col]) for col in zip(*matrix)])

print(result)
