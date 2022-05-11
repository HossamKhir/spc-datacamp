# Create a function pow_two()
pow_two <- function(n){
  n * n
}

# Use the function
pow_two(12)

# Create a function sum_abs()
sum_abs <- function(a, b){
  abs(a) + abs(b)
}

# Use the function
sum_abs(-2, 3)

# Define the function hello()
hello <- function(){
  print("Hi there!")
  TRUE
}

# Call the function hello()
hello()

# Finish the pow_two() function
pow_two <- function(x, print_info = T) {
  y <- x ^ 2
  if (print_info)
  {
    print(paste(x, "to the power two equals", y))
  }
  return(y)
}
