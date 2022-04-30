source("./04-dataframes/03_create_dataframe.R")

# Use order() to create positions
positions <-  order(planets_df$diameter)

# Use positions to sort planets_df
planets_df[positions,]
