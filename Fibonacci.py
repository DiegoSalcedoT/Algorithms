# define the fibonacci() function below...
mem = {}
def fibonacci(n):
  if n in mem:
    return mem[n]
  if n == 1:
    print("returned 1")
    return 1
  if n == 0:
    print("returned 0")
    return 0
  print(f"called by {n} ---")
  sum = fibonacci(n-1) + fibonacci(n-2)
  mem[n] = sum
  return sum

print(fibonacci(10))
# set the appropriate runtime:
# 1, logN, N, N^2, 2^N, N!
print(mem)
