astro <-
  c(
    spring = "20-Mar-2015",
    summer = "25-Jun-2015",
    fall = "23-Sep-2015",
    winter = "22-Dec-2015"
  )

meteo <-
  c(
    spring = "March 1, 15",
    summer =    "June 1, 15",
    fall = "September 1, 15",
    winter = "December 1, 15"
  )

# Convert astro to vector of Date objects: astro_dates
astro_dates <- as.Date(astro, "%d-%b-%Y")

# Convert meteo to vector of Date objects: meteo_dates
meteo_dates <- as.Date(meteo, "%B %d, %y")

# Calculate the maximum absolute difference between astro_dates and meteo_dates
max(abs(astro_dates - meteo_dates))