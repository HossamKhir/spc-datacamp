# Initial code
n <- 100
total <- 0
x <- runif(n)
for (i in 1:n)
  total <- total + log(x[i])

# Rewrite in a single line. Store the result in log_sum
log_sum <- sum(log(x))
