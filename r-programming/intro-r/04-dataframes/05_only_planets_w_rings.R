source("./04-dataframes/03_create_dataframe.R")

# Select the rings variable from planets_df
rings_vector <- planets_df$rings

# Print out rings_vector
print(rings_vector)

# Adapt the code to select all columns for planets with rings
planets_df[rings_vector,]

# Select planets with diameter < 1
subset(planets_df, subset= diameter<1)
