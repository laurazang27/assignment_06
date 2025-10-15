# calculate_factorial.R
# R equivalent of the factorial function (recursive)
calculate_factorial <- function(n) {
  if (n == 0) {
    return(1)
  } else {
    return(n * calculate_factorial(n - 1))
  }
}

# Example usage in R:
# print(calculate_factorial(5))  # 120
