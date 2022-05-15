temp <- list(
  c(3, 7, 9, 6, -1),
  c(6, 9, 12, 13, 5),
  c(4, 8, 3,-1,-3),
  c(1, 4, 7, 2,-2),
  c(5, 7, 9, 4, 2),
  c(-3, 5, 8, 9, 4),
  c(3, 6, 9, 4, 1)
)

# Use lapply() to find each day's minimum temperature
lapply(temp, min)

# Use sapply() to find each day's minimum temperature
sapply(temp, min)

# Use lapply() to find each day's maximum temperature
lapply(temp, max)

# Use sapply() to find each day's maximum temperature
sapply(temp, max)
