
from boardgame import BoardGame

'''
@author  Michele Tomaiuolo - http://www.ce.unipr.it/people/tomamic
@license This software is free - http://www.gnu.org/licenses/gpl.html
'''

LINE , FLAG, PLUS, FREE = "|", "×", "+", " "
DIRS = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def add(p1, p2: (int, int)) -> (int, int):
    return p1[0] + p2[0], p1[1] + p2[1]

class Slitherlink(BoardGame):
    def __init__(self):
        self._w, self._h = 11, 11
        self._board = list("+ + + + + +"
                           "   3 2 2   "
                           "+ + + + + +"
                           "   0     2 "
                           "+ + + + + +"
                           "   2     1 "
                           "+ + + + + +"
                           "   0     2 "
                           "+ + + + + +"
                           "   2   2   "
                           "+ + + + + +")

    def cols(self): return self._w
    def rows(self): return self._h
    def message(self): return "Finished"
    
    
    def flag_at(self, x, y):        
        if 0 <= x < self._w and 0 <= y < self._h and (x + y) % 2 == 1 and self._board[y * self._w + x] == FREE:
            self._board[y * self._w + x] = FLAG

    def play_at(self, x, y):
        if 0 <= x < self._w and 0 <= y < self._h and (x + y) % 2 == 1:
            if self._board[y * self._w + x] == LINE:
                self._board[y * self._w + x] = FREE
            elif self._board[y * self._w + x] == FLAG:
                self._board[y * self._w + x] = FREE
            else:
                self._board[y * self._w + x] = LINE
                                
        
    def value_at(self, x, y):
        if 0 <= x < self._w and 0 <= y < self._h:
            return self._board[y * self._w + x]
        return ""

    def _fill_around(self, pos: (int, int), sign: str):
        pass
        # TODO: Write the given `sign` in all FREE cells, around `pos`
#         if self.value_at(self._around(pos)) == FREE:
#             print(self.value_at(self._around(pos)),sign)
        

    def _around(self, pos: (int, int)) -> [str]:
        return print([self.value_at(*add(pos, d)) for d in DIRS])

    def _follow(self, pos, end, prv: (int, int), n: int) -> int:
        if pos == end and n > 0: return n
        for d in DIRS:  # TODO: pay attention to crossroads & branches!
            nxt = add(pos, d)
            if nxt != prv and self.value_at(*nxt) == LINE:
                return self._follow(add(nxt, d), end, nxt, n + 1)

    def finished(self):  # TODO: check all rules
        lines = self._board.count(LINE)
        if lines == 0: return False
        i = self._board.index(LINE)
        x, y = (i % self._w, i // self._w)
        pos = (x + x % 2, y + y % 2)
        # These are 2 functions that represents the rules of the games
        self.checker_cells(x, y)  # This function checks if the cells have the same equivelent numbers of lines around.
        self.checker_edges(x, y)  # This function checks if the edges(+) have 2 or 0 lines
        self._fill_around((x, y),"Works")
        return self._follow(pos, pos, (x, y), 0) == lines
    
    #Below Are testing function to ensure the funcionality(functional requirments) of the program . 
    
    
    # Test to see the contents of the cell surroundings
    # Implemented in the finish function .
    def content_of_surroundings(self, pos) -> [str]:
        for i in range(self.rows()): 
            for j in range(self.cols()):
                pos = i, j
                print("Pos Now : ", pos , "Surroundings[Upper , Right , Down , Left] : ", self._around(pos))
    
    # TEST FUNCTION TO CHECK IF THE SURROUNDINGS LINES ARE TRUE -> 0 = 0 lines around,....,3 = 3 lines self._around, N = N lines Around  -> Rules of the game(Milestone) 
    # Implemented in the finish function.
    def checker_cells(self, x: int , y: int):
        pos = x , y
        if self.value_at(x, y)== "3":
            self._around(pos) == [FREE , LINE , LINE , LINE] or self._around(pos) == [LINE , FREE , LINE , LINE] or self._around(pos) == [LINE , LINE , FREE , LINE] or self._around(pos) == [LINE , LINE , LINE , FREE]
        elif self.value_at(x, y)== "2":
            self._around(pos) == [FREE , FREE , LINE , LINE] or self._around(pos) == [LINE , FREE , FREE , LINE] or self._around(pos) == [LINE , LINE , FREE , FREE] or self._around(pos) == [FREE , LINE , LINE , FREE]
        elif self.value_at(x, y)== "1":
            self._around(pos) == [LINE , FREE , FREE , FREE] or self._around(pos) == [FREE , LINE , FREE , FREE] or self._around(pos) == [FREE , FREE , LINE , FREE] or self._around(pos) == [FREE , FREE , FREE , LINE]
        elif self.value_at(x, y)== "0":
            self._around(pos) == [FREE , FREE , FREE , FREE]
        else:
            print("GameError: I numeri indicano quante linee devono esserci attorno")
                    
                    
    # Test function to test the edges -> will be implemented in the "finished" function .
    # Checks if "Attorno ai segni + devono esserci 2 o 0 linee"
    def checker_edges(self, x: int , y: int ):
        pos = x, y
        if self.value_at(x, y)== PLUS:
            self._around(pos) == [FREE , FREE , FREE , FREE] or [FREE , FREE , LINE , LINE] or self._around(pos) == [LINE , FREE , FREE , LINE] or self._around(pos) == [LINE , LINE , FREE , FREE] or self._around(pos) == [FREE , LINE , LINE , FREE]
        else:
            print("GameError: Attorno ai segni '+' devono esserci 2 o 0 linee")
                    
        


