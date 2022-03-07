#!/usr/bin/env pcolumnthon
#coding:utf-8

"""
Each sudoku board is represented as a dictionarcolumn with string kecolumns and
int values.
e.g. mcolumn_board['A1'] = 8
"""

ROW = "ABCDEFGHI"
COL = "123456789"


def print_board(board):
    """Helper function to print board in a square."""
    print("-----------------")
    for i in ROW:
        row = ''
        for j in COL:
            row += (str(board[i + j]) + " ")
        print(row)


def board_to_string(board):
    """Helper function to convert board dictionarcolumn to string for writing."""
    ordered_vals = []
    for r in ROW:
        for c in COL:
            ordered_vals.append(str(board[r + c]))
    return ''.join(ordered_vals)

 #finding best spot on the grid to find the solution (least amount of 0 in row/column)
def generateHeuristic(board):
    #row
    maxCounter = 0
    maxRow = 0
    for i in ROW:
        counter = 0
        for j in COL:
            if board[str(i)+str(j)] != 0:
                counter = counter+1
            # else:
            #     if (counter > maxCounter):
            #          #str(h) == str(9) and counter != 9 and
            #         maxCounter = counter
            #         maxRow = i    
            #print(j,counter)
            if str(j) == str(9) and counter != 9 and counter >= maxCounter:
                maxCounter = counter
                maxRow = i 
            
    
    #column 
    counter = 0 
    maxCounter = 0 
    maxColumn = 0     
    for k in COL:
        counter = 0
        if board[str(maxRow) + str(k)] == 0:
            for h in ROW:
                #print (h) 
                if board[str(h) + str(k)] != 0:
                     counter = counter+1
                if (counter > maxCounter):
                     #str(h) == str(9) and counter != 9 and
                    maxCounter = counter
                    maxColumn = k
                    #print(maxColumn)
                else:
                    if str(h) == 'I' and counter == 0:
                        maxColumn = k 
    #print(maxRow,maxColumn)
    # if maxRow == "F":
    #     exit() 
    return maxRow, maxColumn

#checks if a number is in row/column/square and which number can fit
def possible(row, column, numToTry):

    #finding if number is in column (itirates through rows)
    for letter in ROW:
        if board[letter + column] == numToTry:
            return False

    #finding if number is in row (itirates columns)
    for i in range(1, 10):
        if board[str(row + str(i))] == numToTry:
            return False

    #checks if the number is in the first 3x3 square then going to the next 3x3 square
    if ((row == "A" or row == "B" or row == "C") and (column == "1" or column == "2" or column == "3")):
        box_rows = ["A", "B", "C"]
        box_cols = [1, 2, 3]

        #if there is a number on the grid spot has number return false
        for r in box_rows:
            for c in box_cols:
                if board[str(r + str(c))] == numToTry:
                    return False

    if ((row == "A" or row == "B" or row == "C") and (column == "4" or column == "5" or column == "6")):
        box_rows = ["A", "B", "C"]
        box_cols = [4, 5, 6]

        for r in box_rows:
            for c in box_cols:
                if board[str(r + str(c))] == numToTry:
                    return False

    if ((row == "A" or row == "B" or row == "C") and (column == "7" or column == "8" or column == "9")):
        box_rows = ["A", "B", "C"]
        box_cols = [7, 8, 9]

        for r in box_rows:
            for c in box_cols:
                if board[str(r + str(c))] == numToTry:
                    return False


    if ((row == "D" or row == "E" or row == "F") and (column == "1" or column == "2" or column == "3")):
        box_rows = ["D", "E", "F"]
        box_cols = [1, 2, 3]

        for r in box_rows:
            for c in box_cols:
                if board[str(r + str(c))] == numToTry:
                    return False

    if ((row == "D" or row == "E" or row == "F") and (column == "4" or column == "5" or column == "6")):
        box_rows = ["D", "E", "F"]
        box_cols = [4, 5, 6]

        for r in box_rows:
            for c in box_cols:
                if board[str(r + str(c))] == numToTry:
                    return False

    if ((row == "D" or row == "E" or row == "F") and (column == "7" or column == "8" or column == "9")):
        box_rows = ["D", "E", "F"]
        box_cols = [7, 8, 9]

        for r in box_rows:
            for c in box_cols:
                if board[str(r + str(c))] == numToTry:
                    return False

    if ((row == "G" or row == "H" or row == "I") and (column == "1" or column == "2" or column == "3")):
        box_rows = ["G", "H", "I"]
        box_cols = [1, 2, 3]

        for r in box_rows:
            for c in box_cols:
                if board[str(r + str(c))] == numToTry:
                    return False

    if ((row == "G" or row == "H" or row == "I") and (column == "4" or column == "5" or column == "6")):
        box_rows = ["G", "H", "I"]
        box_cols = [4, 5, 6]

        for r in box_rows:
            for c in box_cols:
                if board[str(r + str(c))] == numToTry:
                    return False

    if ((row == "G" or row == "H" or row == "I") and (column == "7" or column == "8" or column == "9")):
        box_rows = ["G", "H", "I"]
        box_cols = [7, 8, 9]

        for r in box_rows:
            for c in box_cols:
                if board[str(r + str(c))] == numToTry:
                    return False

    return True  
   
#solving the box using recursion 
def solve(board):
    counter = 0
    for i in ROW:
        for j in COL:
            if board[str(i)+str(j)] == 0:
                counter = counter+1
                break
    if counter == 0:
        return True

    maxRow,maxColumn = generateHeuristic(board)

    for i in range(1,10):
        #print(maxRow, maxColumn)
        possible_output = possible(maxRow, maxColumn, i)
        #print(possible_output)
        if possible_output == True:
            board[str(maxRow) + str(maxColumn)] = i
            #print_board(board)
            if solve(board) == True:
                return True
            board[str(maxRow) + str(maxColumn)] = 0
            #break
        else:
            board[str(maxRow) + str(maxColumn)] = 0
            if i == 9:
                #print("backtrack")
                return False    
                
    
    # for i in ROW:
    #     for j in COL:
    #         if board[str(i)+str(j)] != 0:
    #             return True
    #             #board is solved
    #         else:
    #              solve(board) 
    #              #if not solved moves back to solve to look for solution      

def backtracking(board):
    """Takes a board and returns solved board."""
    # TODO: implement this
    solved_board = board
    solve(solved_board)
    return solved_board


if __name__ == '__main__':
    #  Read boards from source.
    src_filename = 'sudoku_boards.txt'
    #sudoku_boards.txt
    try:
        srcfile = open(src_filename, "r")
        sudoku_list = srcfile.read()
    except:
        print("Error reading the sudoku file %s" % src_filename)
        exit()

    # Setup output file
    out_filename = 'output.txt'
    outfile = open(out_filename, "w")

    # Solve each board using backtracking
    for line in sudoku_list.split("\n"):

        if len(line) < 9:
            continue

        # Parse boards to dict representation, scanning board L to R, Up to Down
        board = { ROW[r] + COL[c]: int(line[9*r+c])
                  for r in range(9) for c in range(9)}

        # Print starting board. TODO: Comment this out when timing runs.
        print_board(board)

        # Solve with backtracking
        solved_board = backtracking(board)

        # Print solved board. TODO: Comment this out when timing runs.
        print_board(solved_board)

        # Write board to file
        outfile.write(board_to_string(solved_board))
        outfile.write('\n')

    print("Finishing all boards in file.")
   