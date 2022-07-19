is_double = c(F, T, T)

# Example data
is_double

# Define the previous solution
move <- function(is_double) {
  if (is_double[1] & is_double[2] & is_double[3]) {
    current <- 11 # Go To Jail
  }
}

# Define the improved solution
improved_move <- function(is_double) {
  if (is_double[1] && is_double[2] && is_double[3]) {
    current <- 11 # Go To Jail
  }
}

# microbenchmark both solutions
# Very occassionally the improved solution is actually a little slower
# This is just random chance
microbenchmark(move(is_double), improved_move(is_double), times = 1e5)
