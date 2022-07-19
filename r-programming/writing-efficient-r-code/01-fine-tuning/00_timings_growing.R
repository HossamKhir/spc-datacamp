growing <- function(n) {
  x <- NULL
  for (i in 1:n)
    x <- c(x, rnorm(1))
  x
}

# Use <- with system.time() to store the result as res_grow
system.time(res_grow <- growing(n = 30000))
