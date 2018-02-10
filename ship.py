from random import random, randint

#def vars
hit_board= []
enemy_board = []
player_board = []
#make your board 
for i in range(10):
    hit_board.append(["0"] * 10)
    enemy_board.append(["0"] * 10)
    player_board.append(["0"] * 10)
    

#board printing function
def print_board(board, title):
    print(title + "\n")
    count = 0
    print("   A B C D E F G H I J ")
    for row in board:
        print(str(count) + " |" + " ".join(row))
        count += 1
    print("\n")

def print_all_boards():
    print_board(hit_board, "Hit Board")
    print_board(enemy_board, "Enemy Board")
    print_board(player_board, "Your Board")

#print your board 
print_board(hit_board, "Hit Board")


#print enemy board (doesn't print becasue player isn't supposed to be able to see enemy board)
#print_board(enemy_board, "Enemy Board")

#ship creation
class ship():
    def __init__(self, name, size, player):
        self.length = size
        self.name = name
        self.direction = (int)(random() * 2) * 90
        self.positions = []
        self.lives = size
        
        if player == 1:
            no_empty_space = True
            while no_empty_space:
                no_empty_space = False
                
                print("Ship name is " + self.name + ". Ship length is " +  str(self.lives) + ".")
    
                col = "z"
                while not ((ord(col) > 64 and ord(col) < 75) or (ord(col) > 96 and ord(col) < 107)): 
                    col = input("Enter column letter of ship: ")
                    if not col.isalpha():
                        print("Sorry input no valid, please enter a column letter ('A' though 'j'): ")
                        col = "z"
                if ord(col) > 96 and ord(col) < 107:
                    col = ord(col) - 97                    
                elif ord(col) > 64 and ord(col) < 91:
                    col = ord(col) - 65
                print("col number " + str(col))
                    
                     
                row = 11
                while 0 > row or row > 9: 
                    row = input("Enter row number of ship: ")
                    if row.isalpha():
                        print("Sorry, that is not a valid input. Please input a number")
                        row = -1
                    else:
                        row = int(row)
                
                a = 1
                while a != 0 and a != 90 and a != 180 and a != 270:  
                    a = input("Enter direction degree: (0 (right), 90 (down), 180 (left), 270 (up)):  ")
                    if not a.isdigit():
                        print("That is not a valid input.")
                        a = -1
                    else:
                        a = int(a)
                        
                self.direction = a                 
                    
                
                #down
                if self.direction == 90:
                    for i in range(self.length):
                        if  row + i > 9:
                            no_empty_space = True
                            break
                        if player_board[row + i][col] == "1":
                            no_empty_space = True    
                            break
                #left
                elif self.direction == 0:
                    
                    for i in range(self.length):
                        
                        if  col + i > 9:
                            no_empty_space = True
                            break
                        if player_board[row][col + i] == "1":
                            no_empty_space = True
                            break
                    print(no_empty_space)
                elif self.direction == 180:
                    for i in range(self.length):
                        print(self.length)
                        if  col - i < 0:
                            no_empty_space = True
                            break
                        if player_board[row][col - i] == "1":
                            no_empty_space = True
                            break            
                
                elif self.direction == 270:
                   
                    for i in range(self.length):
                        if  row - i < 0:
                            no_empty_space = True
                            break
                        
                        if player_board[row - i][col] == "1":
                            no_empty_space = True
                            break          
                
                if no_empty_space == True:
                    print("Sorry, your ship can't fit there. Please place it in a different spot")    
                        
            if self.direction == 90:
            
            #down
            
                for i in range(self.length):
                    player_board[row + i][col] = "1"
                    self.positions.append((row + i, col)) 
            elif self.direction == 0:
                    
                #right
                    
                for i in range(self.length):
                    player_board[row][col + i] ="1"
                    self.positions.append((row, col + i))
                        
            elif self.direction == 270:
                
                #up
                    
                for i in range(self.length):
                    player_board[row - i][col] = "1"
                    self.positions.append((row + i, col)) 
                
            elif self.direction == 180:
                    
                #left
                    
                for i in range(self.length):
                    player_board[row][col - i] = "1"
                    self.positions.append((row, col + i))
            
        elif player == 2:
            
            row = 0
            col = 0
            no_empty_space = True
            while no_empty_space:
                no_empty_space = False
          
                #choose random position
                #check each space after based on direction
                #vertical
                if self.direction == 90:
                    row = randint(0, (len(hit_board) - 1) - self.length)
                    col = randint(0, (len(hit_board[0]) - 1))
                    for i in range(self.length):
                        if enemy_board[row + i][col] == "1":
                            no_empty_space = True    
                        break
                #horizontal
                elif self.direction == 0:
                    row = randint(0, (len(hit_board) - 1))
                    col = randint(0, (len(hit_board[0]) - 1) - self.length)
                    for i in range(self.length):
                        if enemy_board[row][col + i] == "1":
                            no_empty_space = True
                            break
                    
                        
            if self.direction == 90:
            
            #down
            
                for i in range(self.length):
                    enemy_board[row + i][col] = "2"
                    self.positions.append((row + i, col)) 
            elif self.direction == 0:
                    
                #left
                    
                for i in range(self.length):
                    enemy_board[row][col + i] ="2"
                    self.positions.append((row, col + i))
                        
            elif self.direction == 270:
                
                #up
                    
                for i in range(self.length):
                    enemy_board[row - i][col] = "2"
                    self.positions.append((row + i, col)) 
                
            elif self.direction == 180:
                    
                #right
                    
                for i in range(self.length):
                    enemy_board[row][col + i] ="2"
                    self.positions.append((row, col + i))
            
enemy_ships = []
# enemy ships
enemy_ships.append(ship("Submarine", 3, 2))
enemy_ships.append(ship("Cruiser", 3, 2))
enemy_ships.append(("Air Craft Carrier", 5, 2))
enemy_ships.append(ship("Battleship", 4, 2))
enemy_ships.append(ship("Distoryer", 2, 2))
    
#print_board(enemy_board, "Enemy board")
#player ships
player_ships = []
    
print_board(player_board, "Your board")
    
player_ships.append(ship("Submarine", 3, 1))
    
print_board(player_board, "Your board")
    
player_ships.append(ship("Cruiser", 3, 1))
    
print_board(player_board, "Your board")

player_ships.append(ship("Air Craft Carrier", 5, 1))
    
print_board(player_board, "Your board")
    
player_ships.append(ship("Battleship", 4, 1))
    
print_board(player_board, "Your board")
    
player_ships.append(ship("Distoryer", 2, 1))


def main():
    while len(enemy_ships) > 0 and len(player_ships) > 0:
        print_board(hit_board, "Hit Board")
        print_board(player_board, "Your Board")
        
        #print stuff
        
        print("How you will attack evil enemy.")
        col = "z"
        while not ((ord(col) > 64 and ord(col) < 75) or (ord(col) > 96 and ord(col) < 107)): 
            col = input("Enter column letter of target: ")
            if not col.isalpha():             
                print("Sorry input not valid, please enter a column letter ('A' though 'J'): ")
                col = "z"
        if ord(col) > 96 and ord(col) < 107:
            col = ord(col) - 97                    
        elif ord(col) > 64 and ord(col) < 91:
            col = ord(col) - 65
        print("col number " + str(col))
                    
                     
        row = 11
        while 0 > row or row > 9: 
            row = input("Enter row number of target: ")
            if row.isalpha():
                print("Sorry, that is not a valid input. Please input a number")
                row = -1
            else:
                row = int(row)
        place_hitable = False
        
        if hit_board[row][col] == 1:
            print("You already fired there.")
            continue
        hit = False
        for ship in enemy_ships:
            for position in ship.positions:
                if row == position[0] and col == position[1]:
                   hit = True
                   ship.lives -= 1
                   if ship.lives == 0:
                        print(ship.name + "sink.")
                        for section in ship.position:
                            hit_board[section[0]][section[1]] = "D"
                            
        
        if hit == False:
            print("You have lanched a missle at row " + row + " and column " + col + ". You have not hit a ship.")
        else:
            print("You have hit a ship")
            
main()
        
        
            
    

