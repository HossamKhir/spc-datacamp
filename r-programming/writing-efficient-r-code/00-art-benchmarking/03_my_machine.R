install.packages("benchmarkme")
# Load the benchmarkme package
library("benchmarkme")

# Assign the variable ram to the amount of RAM on this machine
ram <- get_ram()
ram

# Assign the variable cpu to the cpu specs
cpu <- get_cpu()
cpu
