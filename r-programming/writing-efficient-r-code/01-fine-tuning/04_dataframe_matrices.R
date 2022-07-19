df <- readRDS("../data/df.rds")
mat <- readRDS("../data/mat.rds")

library("microbenchmark")

# Which is faster, mat[, 1] or df[, 1]?
microbenchmark(mat[, 1], df[, 1])
