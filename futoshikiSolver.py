def print_square(square):
  print('')
  for row in square:
    print(row[::-1])
  print('')


def find_unassigned(square):
  for i in range(N):
    for j in range(N):
      if square[i][j] == 0:
        return i, j

  return -1, -1


def is_valid(square, r, c, value):
  # Check if the value is already present in the row or column
  for i in range(N):
    if square[r][i] == value or square[i][c] == value:
      return False

  # Check the 2 x 2 sub square
  ulRow = (r // 2) * 2
  ulCol = (c // 2) * 2
  for i in range(2):
    for j in range(2):
      if square[ulRow + i][ulCol + j] == value:
        return False

  # Check inequalities
  inequalities = [(2, 3), (4, 8), (11, 12), (16, 15), (9, 10), (10, 14),
                  (14, 13)]

  for inequality in inequalities:
    cell1, cell2 = inequality
    r1, c1 = (cell1 - 1) // N, (cell1 - 1) % N
    r2, c2 = (cell2 - 1) // N, (cell2 - 1) % N

    if square[r1][c1] != 0 and square[r2][c2] != 0 and square[r1][c1] > square[
        r2][c2]:
      return False

  return True


def solve(square):

  # Find the next unassigned variable
  r, c = find_unassigned(square)

  # If there is no unassigned variable, solution
  # has been found
  if r == -1 and c == -1:
    print_square(square)
    exit(0)

  # Consider its possible assignments
  for value in range(1, N + 1):

    # If the possible solution is valid, explore
    # from that point forward
    if is_valid(square, r, c, value):
      square[r][c] = value
      solve(square)

  # If we reach here, we never found a solution,
  # clear the assignment and backtrack
  square[r][c] = 0


# Main
N = 4

square = [[0 for i in range(N)] for i in range(N)]
print_square(square)

solve(square)
