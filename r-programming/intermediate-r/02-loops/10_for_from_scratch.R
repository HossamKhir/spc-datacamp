# Pre-defined variables
rquote <- "r's internals are irrefutably intriguing"
chars <- strsplit(rquote, split = "")[[1]]

# Initialize rcount
rcount <- 0

# Finish the for loop
for (char in chars) {
  if (char == "u") {
    break
  }
  if (char == "r") {
    rcount <- rcount + 1
  }
}

# Print out rcount
rcount
