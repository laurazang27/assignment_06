# calculate_factorial.R
# R implementation of factorial with input validation and documentation
##' Calculate factorial of a non-negative integer
##'
##' This function returns n! for a non-negative integer n. It performs input
##' validation and uses an iterative loop to avoid deep recursion for larger n.
##'
##' @param n numeric or integer. Must be a non-negative integer.
##' @return integer factorial value of n.
##' @examples
##' calculate_factorial(5)
##' #> 120
##' @export
calculate_factorial <- function(n) {
  if (length(n) != 1 || !is.finite(n)) {
    stop("n must be a single finite numeric value", call. = FALSE)
  }
  if (n < 0) {
    stop("n must be non-negative", call. = FALSE)
  }
  if (n != as.integer(n)) {
    stop("n must be an integer value", call. = FALSE)
  }
  n <- as.integer(n)
  if (n == 0L) return(1L)
  result <- 1L
  for (i in seq_len(n)) {
    result <- result * i
  }
  return(result)
}

# Example usage (uncomment to run):
# print(calculate_factorial(5))  # 120
