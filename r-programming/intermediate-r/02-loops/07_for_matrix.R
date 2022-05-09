ttt <-
  matrix(c("O", NA, "X", NA, "O", "O", "X", NA, "X"),
         nrow = 3,
         byrow = T)

# define the double for loop
for (i in 1:nrow(ttt)) {
  for (j in 1:ncol(ttt)) {
    print(paste("On row ",
                i,
                " and column ",
                j,
                " the board contains ",
                ttt[i, j]))
  }
}
