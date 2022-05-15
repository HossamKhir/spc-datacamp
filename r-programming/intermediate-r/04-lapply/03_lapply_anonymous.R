source("./02_lapply_user_def.R")
split_low

# Transform: use anonymous function inside lapply
# select_first <- function(x) {
#   x[1]
# }
names <- lapply(split_low, function(x) {
  x[1]
})

# Transform: use anonymous function inside lapply
# select_second <- function(x) {
#   x[2]
# }
years <- lapply(split_low, function(x) {
  x[2]
})
