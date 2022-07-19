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

# Set the number of games to play
no_of_games <- 1e5

## Time serial version
system.time(serial <- sapply(1:no_of_games, function(i)
  play()))

## Set up cluster
cl <- makeCluster(4)
clusterExport(cl, "play")

## Time parallel version
system.time(par <- parSapply(cl, 1:no_of_games, function(i)
  play()))

## Stop cluster
stopCluster(cl)
