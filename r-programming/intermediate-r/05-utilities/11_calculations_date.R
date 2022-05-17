day1 <- as.Date("2022-04-29")
day2 <- as.Date("2022-05-01")
day3 <- as.Date("2022-05-06")
day4 <- as.Date("2022-05-12")
day5 <- as.Date("2022-05-17")

# Difference between last and first pizza day
day5 - day1

# Create vector pizza
pizza <- c(day1, day2, day3, day4, day5)

# Create differences between consecutive pizza days: day_diff
day_diff <- diff(pizza)

# Average period between two consecutive pizza days
mean(day_diff)
