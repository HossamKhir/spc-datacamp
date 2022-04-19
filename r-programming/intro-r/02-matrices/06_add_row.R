# Construct star_wars_matrix
box_office <- c(460.998, 314.4, 290.475, 247.900, 309.306, 165.8)
region <- c("US", "non-US")
titles <- c("A New Hope", 
            "The Empire Strikes Back", 
            "Return of the Jedi")

star_wars_matrix <- matrix(box_office, 
                           nrow = 3, byrow = TRUE,
                           dimnames = list(titles, region))
box_office <- c(474.5, 552.5, 310.7, 338.7, 380.3, 468.5)
titles <- c("The Phantom Menace", "Attack of the Clones", "Revenge of the Sith")

star_wars_matrix2 <- matrix(box_office,
                            nrow = 3, byrow=T,
                            dimnames = list(titles, region))

# star_wars_matrix and star_wars_matrix2 are available in your workspace
star_wars_matrix  
star_wars_matrix2 

# Combine both Star Wars trilogies in one matrix
all_wars_matrix <- rbind(star_wars_matrix, star_wars_matrix2)