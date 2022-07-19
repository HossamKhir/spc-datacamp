library("parallel")

# dd <- readRDS("../data/dd.rds")
# Determine the number of available cores
detectCores()

# Create a cluster via makeCluster
cl <- makeCluster(2)

# Parallelise this code
parApply(cl, dd, 2, median)

# Stop the cluster
stopCluster(cl)
