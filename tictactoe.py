"""
Author: Tahmid Mehdi
Determines winner of tic-tac-toe game
"""

# initialize row which will hold 13 13-length strings representing the board
row = []

# Determines the winner of a tic-tac-toe game with a 2D list r
# Parameters: r is a listof(str) where str has 13 characters. The kth letter in
# the jth item of r represents the letter in row j, column k
# Returns: char
def determineWinner(r):
# check if a letter occupies all elements in any row
   for j in range(13):
       rowMatches = 1
       for k in range(12):
           if r[j][k] == r[j][k+1]:
               rowMatches = rowMatches+1
           else:
               break
            
       if rowMatches == 13:
           return r[j][0]
# check if a letter occupies all elements in any column
   for k in range(13):
       colMatches = 1
       for j in range(12):
           if r[j][k] == r[j+1][k]:
               colMatches = colMatches+1
           else:
               break
            
       if colMatches == 13:
           return r[0][k]
# check if a letter occupies all diagnal entries (topleft-bottomright)
   diagMatches = 1
   for l in range(12):
       if r[l][l] == r[l+1][l+1]:
           diagMatches = diagMatches+1
       else:
           break

   if diagMatches == 13:
       return r[0][0]
# check if a letter occupies all diagnal entries (topright-bottomleft)
   diagMatches = 1
   for l in range(12):
       if r[l][12-l] == r[l+1][12-(l+1)]:
           diagMatches = diagMatches+1
       else:
           break

   if diagMatches == 13:
       return r[0][12]

# accept user input
board = input()
# store strings in row
for i in range(0, 169, 13):
    row.append(board[i: i+13])

winner = determineWinner(row)
print("Player {} won.".format(winner))
