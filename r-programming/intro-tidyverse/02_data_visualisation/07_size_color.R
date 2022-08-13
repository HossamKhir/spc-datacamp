# Load the ggplot2 package as well
library(gapminder)
library(dplyr)
library(ggplot2)

# Create gapminder_1952
gapminder_1952 <- gapminder %>%
  filter(year == 1952)

# Add the size aesthetic to represent a country's gdpPercap
ggplot(gapminder_1952,
       aes(
         x = pop,
         y = lifeExp,
         color = continent,
         size = gdpPercap
       )) +
  geom_point() +
  scale_x_log10()
