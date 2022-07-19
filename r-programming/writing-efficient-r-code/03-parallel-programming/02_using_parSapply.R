play <- function() {
  total <- no_of_rolls <- 0
  while (total < 10) {
    total <- total + sample(1:6, 1)
    
    # If even. Reset to 0
    if (total %% 2 == 0)
      total <- 0
    no_of_rolls <- no_of_rolls + 1
  }
  no_of_rolls
}

library("parallel")
# Create a cluster via makeCluster (2 cores)
cl <- makeCluster(2)

# Export the play() function to the cluster
clusterExport(cl, "play")

# Re-write sapply as parSapply
res <- parSapply(cl, 1:100, function(i)
  play())

# Stop the cluster
stopCluster(cl)
