rolls = matrix(c(5, 4, 4, 3, 1, 3), ncol = 2)

# Example data
rolls

# Define the previous solution
app <- function(x) {
  apply(x, 1, sum)
}

# Define the new solution
r_sum <- function(x) {
  rowSums(x)
}

# Compare the methods
microbenchmark(app_sol = app(rolls),
               r_sum_sol = r_sum(rolls))
