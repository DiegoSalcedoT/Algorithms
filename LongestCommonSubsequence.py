# Dynamic Programming applied to Longest Common Subsequence

dna_1 = "ACCTGCTAGTA"
dna_2 = "TTACGAGTACT"

def longest_common_subsequence(string_1, string_2):
  print(f"Finding longest common subsequence of {string_1} and {string_2}")

  grid = [[0 for col in range(len(string_1) + 1)] for row in range(len(string_2) + 1)]

  for row in range(1, len(string_2) + 1):
     #print("Comparing: {0}".format(string_2[row - 1]))
     for col in range(1, len(string_1) + 1):
      #print("Against: {0}".format(string_1[col - 1]))
      if string_1[col - 1] == string_2[row - 1]:
        grid[row][col] = grid[row - 1][col - 1] + 1
      else:
        grid[row][col] = max(grid[row - 1][col], grid[row][col - 1])

  for row_line in grid:
    print(row_line)

  col = len(string_1)
  row = len(string_2)

  Match = []
  while col + row > 0:
    if grid[row][col] > max(grid[row][col - 1], grid[row - 1][col]):
      Match.append(string_1[col - 1])
    elif grid[row - 1][col] > grid[row][col - 1]:
      col += 1
    elif grid[row - 1][col] < grid[row][col - 1]:
      row += 1
    col -= 1
    row -= 1
  return "".join(Match[::-1])

print(longest_common_subsequence(dna_1, dna_2))
