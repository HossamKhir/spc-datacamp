source("./04-dataframes/03_create_dataframe.R")

# Print out diameter of Mercury (row 1, column 3)
print(planets_df[1, 3])

# Print out data for Mars (entire fourth row)
print(planets_df[4,])

# Select first 5 values of diameter column
print(planets_df[1:5,'diameter'])
