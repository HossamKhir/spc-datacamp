source('./05_use_sapply.R')
# Definition of basics()
basics <- function(x) {
  c(min = min(x),
    mean = mean(x),
    max = max(x))
}

# Apply basics() over temp using vapply()
vapply(temp, basics, numeric(3))

# Definition of the basics() function
basics <- function(x) {
  c(min = min(x), mean = mean(x), median = median(x), max = max(x))
}

# Fix the error:
vapply(temp, basics, numeric(4))
