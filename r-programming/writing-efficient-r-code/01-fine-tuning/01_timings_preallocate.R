pre_allocate <- function(n) {
  x <- numeric(n) # Pre-allocate
  for (i in 1:n)
    x[i] <- rnorm(1)
  x
}

# Use <- with system.time() to store the result as res_allocate
n <- 30000
system.time(res_allocate <- pre_allocate(n))
