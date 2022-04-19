# all_wars_matrix is available in your workspace
all_wars_matrix

# Estimate the visitors
visitors <- all_wars_matrix/5

# Print the estimate to the console
print(visitors)

ticket_prices_matrix <- matrix(
  c(5, 5, 6, 6, 7, 7, 4, 4, 4.5, 4.5, 4.9, 4.9),
  byrow = T,
  nrow = 6,
  dimnames = list(rownames(all_wars_matrix), colnames(all_wars_matrix))
)

# all_wars_matrix and ticket_prices_matrix are available in your workspace
all_wars_matrix
ticket_prices_matrix

# Estimated number of visitors
visitors <- all_wars_matrix/ticket_prices_matrix

# US visitors
us_visitors <- visitors[,1]

# Average number of US visitors
print(mean(us_visitors))