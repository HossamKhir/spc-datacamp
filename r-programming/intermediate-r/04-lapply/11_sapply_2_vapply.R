source("./05_use_sapply.R")
# Convert to vapply() expression
vapply(temp, max, numeric(1))

# Convert to vapply() expression
vapply(temp, function(x, y) {
  mean(x) > y
}, y = 5, logical(1))
