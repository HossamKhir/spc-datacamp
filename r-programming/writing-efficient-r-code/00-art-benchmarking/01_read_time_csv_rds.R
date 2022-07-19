# How long does it take to read movies from CSV?
system.time(read.csv("../data/movies.csv"))

# How long does it take to read movies from RDS?
system.time(readRDS("../data/movies.rds"))
