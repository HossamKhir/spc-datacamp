login <-
  sapply(
    c(
      "2022-05-03 10:18:04 UTC",
      "2022-05-08 09:14:18 UTC",
      "2022-05-08 12:21:51 UTC",
      "2022-05-08 12:37:24 UTC",
      "2022-05-10 21:37:55 UTC"
    ),
    as.POSIXct
  )

logout <-
  sapply(
    c(
      "2022-05-03 10:56:29 UTC",
      "2022-05-08 09:14:52 UTC",
      "2022-05-08 12:35:48 UTC",
      "2022-05-08 13:17:22 UTC",
      "2022-05-10 22:08:47 UTC"
    ),
    as.POSIXct
  )

# Calculate the difference between login and logout: time_online
time_online <- logout - login

# Inspect the variable time_online
time_online

# Calculate the total time online
sum(time_online)

# Calculate the average time online
mean(time_online)
