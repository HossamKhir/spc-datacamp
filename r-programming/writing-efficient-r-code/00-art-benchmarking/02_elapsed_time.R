install.packages("microbenchmark")
# Load the microbenchmark package
library("microbenchmark")

# Compare the two functions
compare <- microbenchmark(read.csv("../data/movies.csv"),
                          readRDS("../data/movies.rds"),
                          times = 10)

# Print compare
compare
