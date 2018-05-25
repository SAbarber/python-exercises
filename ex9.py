#  
Instructions 
We will be using the code from the last exercise to check to see if there's a win or not. 

Please follow the instructions and DON'T DELETE THE COMMENTS.  

This may take a little bit more time and some modifying to get your code to work. 

 1. Add this to the top of your code so that the user knows how to play.

print ("TIC TAC TOE board. Rows and Columns starting from 1,1")
print ("Game board is printed each time to show progress!")

2. Now we want to print the game board  
def print_game(game):
    print ("\n")
    for i in range(3):
        print (str(game[i]) + "\n")

3. Use your CheckWin function from the last exercise now. Make sure your function can check to see if there's a draw or not too! 

 4. We want to take the user input like 1, 2 and split it into the corresponding rows and columns.     Put this IN the while loop.  
spot = input("Enter the row,column in same format as given: ")
spot = spot.split(",") # This will remove the comma

5. Python starts at zero right? Our user doesn't know that so let's make it easy for them.  
row = int(spot[0]) -1    
column = int(spot[1]) -1

6. Going to create an if statement to check to see who's turn it is. Our count should be at zero.  
if count%2==0:
   print ("\nPlayer 1's Turn!")
   if game[row][column] == 0:  # Make sure the spot is blank
     game[row][column] = 'X'   # if it's blank, mark an X
   else:
     print ("Try Again!")      # if it's not blank, try again
     count-=1   # this will reset the counter, so you can try again
   print_game(game)  # print your new game board
        
    else:
        # Now do the same thing for player 2 as you did for player 1
        # Player 2 is an 'O' 
    
    #Increase your count

    #check for a win using your function that you created
    
    
    
    
# Declare the blank game           
game=[[0,0,0], 
      [0,0,0],
      [0,0,0]]
      
count = 0

# create the print gameboard function


#Ask the user what size of game board do they want to print?
board_size = int(input("What size of game board? "))
for x in range(board_size):
  print(' '"---" * board_size)
  print("|   " * (board_size + 1))
print(' '"---" * board_size)
def print_game(game):
    print ("\n")
    for i in range(3):
        print (str(game[i]) + "\n")

# Insert the checkWin function here.

def winner():
  if 'X' == game[0][0] == game[0][1] == game[0][2]:
    return ("Player 1 is the winner")
  if 'X' == game[1][0] == game[1][1] == game[1][2]:
    return ("Player 1 is the winner")
  if 'X' == game[2][0] == game[2][1] == game[2][2]:
    return ("Player 1 is the winner")
  if 'X' == game[0][0] == game[1][0] == game[2][0]:
    return ("Player 1 is the winner")
  if 'X' == game[0][1] == game[1][1] == game[2][1]:
    return ("Player 1 is the winner")
  if 'X' == game[0][2] == game[1][2] == game[2][2]:
    return ("Player 1 is the winner")
  if 'X' == game[0][0] == game[1][1] == game[2][2]:
    return ("Player 1 is the winner")
  if 'X' == game[0][2] == game[1][1] == game[2][0]:
    return ("Player 1 is the winner")
  if 'O' == game[0][0] == game[0][1] == game[0][2]:
    return ("Player 2 is the winner")
  if 'O' == game[1][0] == game[1][1] == game[1][2]:
    return ("Player 2 is the winner")
  if 'O' == game[2][0] == game[2][1] == game[2][2]:
    return ("Player 2 is the winner")
  if 'O' == game[0][0] == game[1][0] == game[2][0]:
    return ("Player 2 is the winner")
  if 'O' == game[0][1] == game[1][1] == game[2][1]:
    return ("Player 2 is the winner")
  if 'O' == game[0][2] == game[1][2] == game[2][2]:
    return ("Player 2 is the winner")
  if 'O' == game[0][0] == game[1][1] == game[2][2]:
    return ("Player 2 is the winner")
  if 'O' == game[0][2] == game[1][1] == game[2][0]:
    return ("Player 2 is the winner")  
  else:
    return("No Winner")

#-Now lets start the game
#Insert the code from Step 4
print("Player 1's turn")
while True:
  spot = input("Enter the row, column in same format as given: ")
  spot = spot.split(",") # This will remove the comma
  row = int(spot[0]) -1
  column = int(spot[1]) -1
  if count%2==0:
    print ("\nPlayer 1's Turn!")
    if game[row][column] == 0:  # Make sure the spot is blank
       game[row][column] = 'X'   # if it's blank, mark an X
    else:
       print ("Try Again!")      # if it's not blank, try again
       count-=1   # this will reset the counter, so you can try again
    print_game(game)  # print your new game board
                              
  else:
    print ("\nPlayer 2's Turn!")
    if game[row][column] == 0:  # Make sure the spot is blank
       game[row][column] = 'O'   # if it's blank, mark an X
    else:
       print ("Try Again!")      # if it's not blank, try again
       count-=1   # this will reset the counter, so you can try again
    print_game(game)  # print your new game board
  count+=1
  print(winner())
  if 'X' == winner():
    break
  elif 'O' == winner():
    break

    
    
    
    
    
    
    
