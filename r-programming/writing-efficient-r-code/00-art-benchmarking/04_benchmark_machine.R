# Load the package
library("benchmarkme")

# Run the io benchmark
res <- benchmark_io(runs = 1, size = 5)

# Plot the results
plot(res)
