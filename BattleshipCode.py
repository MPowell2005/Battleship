'''
Author: Michael Powell
Narrative: This program allows the user to play Battleship.
    
Features:
    - The size of the board is customizable.
    - The number of ships is customizable.
    - The program reports the number of turns left in the game.
    - The program reports the status of the board with 'X' for miss and 'H' for hit.
    - The program asks for the coordinates from the user.
    - The program tells the user what happened (hit or miss).
    - At the beginning of the game, the program prints the location of the players' ships, represented by emojis.
    - The program plays a sound for hitting a ship.
    - Try and excepts are used extensively to ensure the user inserts appropriate values.
    - There is a 'play again' option.

@author: mpowell23@gcds.net
'''

# Import Box
from playsound import playsound
import emoji
import random


def gameboard(board):
    '''
        Summary:
        This function prints the board as it is updated.
        
        Parameter(s):
        Board (2-D array): Any of the red or blue boards.
        
        Returns:
        Printed board.
    '''
    
    for row in board :
        print(row)


def ship_randomizer(board_size, ship_number) :
    '''
        Summary:
        This function randomizes the positions of the ships defined in a list.
        
        Parameter(s):
        board_size (list): A list that contains the number of rows and columns of the board.
        
        Returns:
        taken_positions_ship (list): The list that defines the positions of the ships on a given board.
    '''
    
    counter = 1                                                                                             # Define a counter equal to 1
    taken_positions_ship = []                                                                               # Define a list that consists of the taken positions by the ships
    
    while counter <= ship_number :                                                                          # Run a while loop equal to the number of ships on the board.
        while True:                                                                                         
            row = random.randint(0, board_size[0] - 1)                                                      # Randomizes an integer from 0 to the number of rows that is equal to ship's row position
            column = random.randint(0, board_size[1] - 1)                                                   # Randomizes an integer from 0 to the number of columns that is equal to ship's column position
            
            if (row, column) in taken_positions_ship :                                                      # If the coordinate is already taken, repeat the while True loop
                continue
            
            else :                                                                                          # If the coordinate is not taken, append the coordinate into the list, add 1 one to the counter, and break the while True loop
                taken_positions_ship.append((row, column))
                counter = counter + 1
                break
    
    return taken_positions_ship                                                                             # Return taken_positions_ship once finished


def player_input_coordinate(type_coordinate, board_size_position, board_size) :
    '''
        Summary:
        This function asks the user for a coordinate to attack their opposition.
        
        Parameter(s):
        type_coordinate (string): A string that is either equal to a "row" or "column."
        board_size_position (integer): A parameter that is equal to the appropriate index of board_size.
        board_size (list): A list that contains the number of rows and columns of the board.
        
        Returns:
        coordinate (integer): The coordinate the user selected.
    '''
    
    while True :
        # Asking the user for the coordinate
        coordinate = input('Please select the ' + type_coordinate + ' where you want to attack team BLUE.\n')
        coordinate = coordinate.strip()                                                                     # Strip all added spaces after and before the input
        
        try :
            coordinate = int(coordinate)                                                                    # Convert the coordinate into an integer
            
            if coordinate < 0 or coordinate > board_size[board_size_position] - 1:                          # If the coordinate does not belong in the board, continue the while True loop
                print('Please select a ' + type_coordinate + ' between 0 and ' + str(board_size[board_size_position] - 1) + '.')
                continue
            
            else :                                                                                          # If the coordinate belongs in the board, break the while True loop
                break
        except :                                                                                            # If the coordinate cannot be converted into an integer, continue the while True loop
            print('Please select a ' + type_coordinate + ' between 0 and ' + str(board_size[board_size_position] - 1) + '.')
            continue
        
    return coordinate                                                                                       # Return the coordinate once finished


def board_create(board_size, board):
    '''
        Summary:
        This function creates a BattleShip board given an empty list and its size.
        
        Parameter(s):
        board_size (list): A list that contains the number of rows and columns of the board.
        board (list): An empty list.
        
        Returns:
        board (list): A manipulated 2-d array.
    '''
    
    counter_row = 1                                                                                         # Define a counter for the rows
    while counter_row <= board_size[0] :                                                                    # Run the loop equal to the number of rows indicated in board_size
        counter_column = 1                                                                                  # Define a counter for the columns
        temp_list = []                                                                                      # Define an empty list used for appending purposes
        
        while counter_column <= board_size[1] :                                                             # Run the loop equal to the number of columns indicated in board_size
            temp_list.append('-')                                                                           # Append a hyphen into the list
            counter_column = counter_column + 1                                                             # Add 1 to the counter for columns
            
        board.append(temp_list)                                                                             # Append temp_list into board, which contains a row
        counter_row = counter_row + 1                                                                       # Add 1 to the counter for rows
    
    return board                                                                                            # Return the board once finished

 
def main() :
    
    # Game Description
    print('This program allows the user to play BattleShip against the computer with a variety of settings.\n')
    
    play_again = 'yes'                                                                                      # Set a variable called 'play_again' equal to 'yes'
    while play_again == 'yes' :                                                                             # Run the loop while play_again is equal to 'yes'
        # Game Variable Definitions
        turn_number = 10                                                                                    # Turn_number defines the turn number of the game 
        win = 0                                                                                             # Win defines if the game will run.
        
        # Defining the red board variables
        taken_positions_red = []                                                                            # Taken_positions_red defines the turns that have been taken by red
        counter_red = 0                                                                                     # Counter_red defines the number of ships that red has taken out
        board_red = []                                                                                      # Board_red is an empty list
        
        # Defining the blue board variables
        taken_positions_blue = []                                                                           # Taken_positions_blue defines the turns that have been by blue
        counter_blue = 0                                                                                    # Counter_blue defines the number of ships that blue has taken out
        board_blue = []                                                                                     # Board_blue is an empty list
        
        # Asking the user for the board size
        while True :
            board_size = input('What size board do you want in the game (type: row by column)?\n')
            board_size = board_size.strip()                                                                 # Strip all added spaces after and before the input
            
            try :
                board_size = board_size.split(' by ')                                                       # Split the 'row by column' into a list: [row, column]
                
                try :
                    counter_element = 1                                                                     # Define a counter
                    repeat = 'no'                                                                           # Define a variable called 'repeat' equal to 'no'
                    
                    while counter_element <= 2 :                                                            # Run the counter two times in order to convert each element into an integer, then break the while True loop
                        board_size[counter_element - 1] = int(board_size[counter_element - 1]) 
                        if board_size[counter_element - 1] <= 0 :                                           # If the number of rows or number of columns is an integer but less than or equal to zero, set 'repeat' equal to 'yes'
                            repeat = 'yes'
                            break
                        else :                                                                              # Otherwise, add 1 to the counter
                            counter_element = counter_element + 1
                    
                    if repeat == 'yes' :
                        print('Please insert a positive integer by a positive integer. One of your integers is less than or equal to 0.')
                        continue
                    
                    else :
                        break
                
                except :                                                                                    # If the elements could not be converted into an integer, continue the while True loop
                    print('Please insert a positive integer by a positive integer. One of your sizes is not an integer.')
                        
            except :                                                                                        # If the list could not be split, continue the while True loop
                print('Please insert a positive integer by a positive integer. Follow the directions shown in the question.')
        
        # Calculating the number of spaces available on the board
        spaces = board_size[0] * board_size[1]
        
        # Asking the user for the number of ships
        while True :
            ship_number = input('How many ships do you want in the game?\n')
            ship_number = ship_number.strip()                                                               # Strip all added spaces after and before the input
            
            try :
                ship_number = int(ship_number)                                                              # Convert the ship_number into an integer
                
                if ship_number <= 0 or ship_number > spaces :                                               # If the ship_number is less than or equal to zero or is greater than the number of spaces available on the board, continue the while True loop
                    print('Please insert a positive integer less than or equal to the number of spaces available on the board (spaces = ' + str(spaces) + ').')
                    continue 
                
                else :                                                                                      # Otherwise, break the while True loop
                    break
            
            except :                                                                                        # If the ship_number cannot be converted into an integer, continue the while True loop
                print('Please insert a positive integer less than or equal to the number of spaces available on the board (spaces = ' + str(spaces) + ').')
                continue
        
        # Determining the coordinates where red has ships
        taken_positions_ship_red = ship_randomizer(board_size, ship_number)
        
        # Determining the coordinates where blue has ships
        taken_positions_ship_blue = ship_randomizer(board_size, ship_number)
        
        # Creating an aesthetic board for red
        board_red_aesthetic = []                                                                            # Define an empty list for red
        board_red_aesthetic = board_create(board_size, board_red_aesthetic)                                 # Use the board_create function to create an aesthetic board for red
        
        counter_indice_row = 0                                                                              # Insert a number at the end of each row that indicates the row's position
        for row in board_red_aesthetic :
            row.append(str(counter_indice_row))
            counter_indice_row = counter_indice_row + 1
            
        indice_column_list = []                                                                             # Insert a list of numbers that indicate the column's position before the first row
        counter_indice_column = 1
        while counter_indice_column <= int(board_size[1]) :
            indice_column_list.append(str(counter_indice_column - 1))
            counter_indice_column = counter_indice_column + 1
        board_red_aesthetic.insert(0, indice_column_list)
        
        for coordinate in taken_positions_ship_red :                                                        # Insert a ship using the emoji import at each ship coordinate found in taken_positions_ship_red
            board_red_aesthetic[coordinate[0] + 1][coordinate[1]] = emoji.emojize(':ship:')
       
        print('\nThe program has randomized your ships to produce the following board:')                    # Print the aesthetic board
        gameboard(board_red_aesthetic)
        
        # Creating a board for red to use in the game
        board_red = board_create(board_size, board_red)
        
        # Creating a board for blue to use in the game
        board_blue = board_create(board_size, board_blue)
        
        
        # Running the game
        while win == 0 and turn_number <= 10 and turn_number > 0:                                           # Run the loop when win is equal to zero and the number of turns is less than or equal to 10
            # TURN RED
            print('\nYou have ' + str(turn_number) + ' turns remaining.')                                   # Update the user on the turn number and whose turn it is
            print('It is turn RED.')
            
            # Selecting the coordinate for RED against BLUE
            while True :
                # Row Selection
                type_coordinate = 'row'
                board_size_position = 0                                                                     
                row = player_input_coordinate(type_coordinate, board_size_position, board_size)                                                     
                
                # Column Selection
                type_coordinate = 'column'
                board_size_position = 1
                column = player_input_coordinate(type_coordinate, board_size_position, board_size)                          
                
                # Ensuring the coordinate is not taken
                if (row, column) in taken_positions_blue :                                                  # Continue the while True loop if the coordinate has already been selected
                    print('Please select a coordinate that has not already been taken.')
                    continue
                
                else :                                                                                      # Break the while True loop and append the coordinate into a list if it has not been selected
                    taken_positions_blue.append((row, column))                                              
                    break
            
            # The case if a ship has been hit
            if (row, column) in taken_positions_ship_blue :
                print('Red has HIT a blue ship.')                                                           # Update the user that red has hit a blue ship
                counter_red = counter_red + 1                                                               # Add one to red's counter
                board_blue[row][column] = 'H'                                                               # Put a 'H' on the board to symbolize a 'HIT'
                playsound('/Users/mpowell23/eclipse-workspace/CS-II Code/BattleShip/battleship sound.wav')  # Play the hit sound
            
            # The case if a ship has been missed
            else :
                print('Red has MISSED a blue ship.')                                                        # Update the user that red has missed a blue ship
                board_blue[row][column] = 'X'                                                               # Put a 'X' on the board to symbolize a 'MISS'
            
            # Printing the BLUE's board after RED's turn
            gameboard(board_blue)
            
            # Determining if RED won
            if counter_red == ship_number :
                print('Red has eliminated all of the blue ships.')
                win = 'red'
                break
        
        
            # Turn BLUE
            print('It is turn BLUE.')                                                                       # Update the user that it is blue's turn
            
            # Row and Column Selection for the Computer
            while True :
                row = random.randint(0, board_size[0] - 1)                                                  # The row = the random import to randomize an integer from 0 to the number of rows
                column = random.randint(0, board_size[1] - 1)                                               # The column = the random import to randomize an integer from 0 to the number of columns
                
                if (row, column) in taken_positions_red :                                                   # If the row and the column are in taken_positions, repeat the while True loop
                    continue
                
                else :                                                                                      # Else, break the while True loop
                    taken_positions_red.append((row, column))
                    break 
            
            # The case if a ship has been hit
            if (row, column) in taken_positions_ship_red :
                print('Blue has HIT a red ship')                                                            # Update the user that blue has hit a red ship
                counter_blue = counter_blue + 1                                                             # Add one to blue's counter
                board_red[row][column] = 'H'                                                                # Put a 'H' on the board to symbolize a 'HIT'
                playsound('/Users/mpowell23/eclipse-workspace/CS-II Code/BattleShip/battleship sound.wav')  # Play the hit sound
            
            # The case if a ship has been missed
            else :
                print('Blue has MISSED a red ship.')                                                        # Update the user that blue has hit a red ship
                board_red[row][column] = 'X'                                                                # Put a 'X' on the board to symbolize a 'MISS'
            
            # Printing the board for RED after BLUE's turn
            gameboard(board_red)
            
            # Determining if BLUE won
            if counter_blue == ship_number :
                print('Blue eliminated all of the red ships.')        
                win = 'blue'
                break  
            
            
            # Turn_counter update
            turn_number = turn_number - 1
        
        
        # Win Determination
        if win == 'red' :                                                                                   # Print a congratulations message to team red if that team won
            print('\nRed has won the game. Congratulations to team red.\n')
        
        elif win == 'blue' :                                                                                # Print a congratulations message to team blue if that team won
            print('\nBlue has won the game. Congratulations to team blue.\n')                                   
        
        else :                                                                                              # Print a message that states both teams resulted in a tie
            print('\nThe game has resulted in a tie because the players have exceeded the number of turns selected.\n')
        
        
        # Play Again Option
        while True :
            play_again = input('Do you want to use the program again (yes or no)?\n')                       # Ask the user if they want to use the program again
            play_again = play_again.strip()                                                                 # Strip all additional spaces before and after the input
            play_again = play_again.lower()                                                                 # Make the answer have all lower case characters
            
            if play_again == 'yes' or play_again == 'y' :                                                   # If the user says 'yes' or 'y,' repeat the program
                print('The program will restart.\n')
                break
            
            elif play_again == 'no' or play_again == 'n' :                                                  # If the user says 'no' or 'n,' quit the program
                print('The program has ended. Thanks for playing.')
                break
            
            else :                                                                                          # If the user does not insert a 'yes' or 'no' answer, repeat the while True loop
                print('Please insert a "yes" or "no" answer.')
                continue


if __name__ == '__main__':
    main() 