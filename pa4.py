# File: pa4.py
# Author:     
# Date: 
# Description: 

def solve(size, filename):
    """
    Solves the Sudoku problem specified in input file filename.
    The size of the problem is size.  (For example, for a 9 x 9 Sudoku,
    size is 9.)
    Returns a tuple of size 2.  The first element is a nested list containing
    the solution to the problem (row is the first index, col the second).
    The second element of the tuple is the number of nodes in the state space
    tree that were generated by your solution.
    """
    SUDOKU_OFFSET = 1



    #part 1-->parse data into a 2d matrix
    sudoku_array_return = load_sudoku_array(filename,SUDOKU_OFFSET)
    sudoku_array = sudoku_array_return[0]
    dimension = sudoku_array_return[1]

    #part 2 --> set up recursion and solve
    possible_x = set()
    possible_y = set()
    pass


def solve_recursive(x,y,sudoku_array,sudoku_offset, possible_x, possible_y,possible_square,num_nodes,dimension_sqrt):
    """
    This method is the recursive method for solve
    @params
        x and y are both ints which are cordinates
        sudoku_array is the array at this current step
        sudoku_offset is the offset into our list from our game
        possible_x is a set with all possible vals for our val to be based on column
        possible_y is a set with all possible vals for our val to be based on row
        possible_square is a set with all possible vals for our val to be based on sub square
        num_nodes are nodes so far to solve problem
        dimension_sqrt is an int which gets square root of the dimensions used for the possible_square
    This method will return a tuple with sudoku_array as index 0 and num nodes as index 1
    """

    list_len = len(sudoku_array)

    #last iteration
    #when x==list_len and y==1 we will iterate that time and call with y=0
    if(x==list_len and y==0):
        return sudoku_array,num_nodes
    
    


def load_sudoku_array(filename,sudoku_offset):
    """
    This method creates the sudoku array.
    It returns an array where the pre-defined values are at their x,y cordinates.
        If there is no current val at that location then there is None at that cordinate
    """
    #dictionary where key is the tuple location and val is the value at that location
    locations = get_locations(filename)

    #find max row and col value by searching locations
    dimension = get_dimension(locations)
    sudoku_array = []
    for i in range(dimension):
        inner_array = []
        for j in range(dimension):
            try:
                val = locations[i+sudoku_offset,j+sudoku_offset]
                inner_array.append(val)
            except:
                inner_array.append(None)
        sudoku_array.append(inner_array)
    return sudoku_array,dimension




def get_locations(filename):
    """
    This method is a helper method to load_sudoku_array to find pre defined locaitons
    It returns a dictonary  where key is the tuple location and val is the value at that location
    """
    locations = {}
    with open(filename, 'r') as f:
        for line in f:
            line_list = line.split()
            locations[int(line_list[0]),int(line_list[1])] = int(line_list[2])
    return locations

def get_dimension(locations):
    """
    This method finds the dimension to later be used for creating 2D array in Solve
    locations is dict where key is the tuple location and val is the value at that location
    """  
    dimension = 0
    for pair in locations.keys():
        if(pair[0]>dimension):
            dimension = pair[0]
    return dimension

if __name__ == "__main__":
    SIZE = 9
    FILENAME = "p1.txt"
    solution = solve(SIZE, FILENAME)
    # if not solution[0]:
    #     print("No solution")
    # else:
    #     print(solution[0])
    # print(f"Nodes generated = {solution[1]}")