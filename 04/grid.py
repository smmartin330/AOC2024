#
# advent of code functions i keep using over and over...
#

import numpy


class Grid:
    def __init__(self, raw_grid) -> None:
        """takes in the input data (a list of strings) and converts it to a 2D array (a list of lists). provides functionality to search the grid easily. provide raw_grid (the puzzle input processed as a list)

        Args:
            raw_grid (list): the puzzle data for processing.
            
        values:
            self.gridmap (list): a 2D array. (x,y) is found at self.gridmap[y][x]
            self.gridmap_t (list): the 2D array transposed along axes so that (x,y) is found at self.gridmap[x][y]
            self.unique_values (list): all unique values found in the grid
            self.height (int): the height of the grid (how many rows)
            self.width (int): the width of the grid (how many columns)
            self.every_node (list): a list of every node that can be used for elimination of possibilities.
        """
        self.gridmap = []
        self.unique_values = {}
        for row in raw_grid:
            this_row = []
            for char in row:
                this_row.append(char)
                if char not in self.unique_values:
                    self.unique_values[char] = []
            self.gridmap.append(this_row)

        self.gridmap_t = numpy.transpose(self.gridmap).tolist()
        self.height = len(self.gridmap)
        self.width = len(self.gridmap_t)
        self.every_node = []
        for x in range(0, self.width):
            for y in range(0, self.height):
                self.every_node.append((x, y))

    def g_rot90(self,rotations,rot_t=False):
        self.gridmap = numpy.rot90(self.gridmap,rotations).tolist()
        if rot_t == True:
            self.gridmap_t = numpy.transpose(self.gridmap).tolist()
        
    def pos(self, coordinate, x_offset=0, y_offset=0):
        """Returns the value either at a particular coordinate or at a particular offset from that coordinate.

        Args:
            coordinate (list): the coordinate itself
            x_offset (int, optional): the x-offset to the coordinate. negative values to the left, positive to the right. Defaults to 0.
            y_offset (int, optional): the y-offset to the coordinate. negative values towards the top, positive towards the bottom. Defaults to 0.

        Returns:
            list: the position and the value found. 
        """
        x, y = coordinate[0] + x_offset, coordinate[1] + y_offset
        return [(x,y), self.gridmap[y][x]]

    def pos_set(self, coordinate, new, x_offset=0, y_offset=0):
        """set the value at a coordinate

        Args:
            coordinate (list): the coordinate itself
            new (str): the new value to set
            x_offset (int, optional): the x-offset to the coordinate. negative values to the left, positive to the right. Defaults to 0.
            y_offset (int, optional): the y-offset to the coordinate. negative values towards the top, positive towards the bottom. Defaults to 0.

        Returns:
            bool: confirmation of success (needs error handling.)
        """
        x, y = coordinate[0] + x_offset, coordinate[1] + y_offset
        self.gridmap[y][x] = new
        self.gridmap_t[x][y] = new
        return True
    
    def adj(self, coordinate) -> "dict":
        """provides a dictionary of all adjacents, including diagonals, and their values.

        Args:
            coordinate (list): the coordinate itself

        Returns:
            dict: the adjacent coordinates and their values. 
        """
        x, y = coordinate[0], coordinate[1]
        adj = {}
        adj_x = list(range(max(0, x - 1), min(self.width, x + 2)))
        adj_y = list(range(max(0, y - 1), min(self.height, y + 2)))
        for _x in adj_x:
            for _y in adj_y:
                if (_x, _y) != (x, y):
                    adj[(_x, _y)] = self.gridmap[_y][_x]

        return adj

    def adj_card(self, coordinate) -> "dict":
        """returns a dictionary of only cardinally adjacent coordinates and their values.

        Args:
            coordinate (list): the origin coordinate

        Returns:
            dict: the cardinally adjacent coordinates and their values. 
        """
        x, y = coordinate[0], coordinate[1]
        adj_card = {}

        if x > 0:
            adj_card[(x - 1, y)] = self.gridmap[y][x - 1]
        if x < self.width - 1:
            adj_card[(x + 1, y)] = self.gridmap[y][x + 1]
        if y > 0:
            adj_card[(x, y - 1)] = self.gridmap[y - 1][x]
        if y < self.height - 1:
            adj_card[(x, y + 1)] = self.gridmap[y + 1][x]

        return adj_card
    
    def adj_x(self, coordinate) -> "dict":
        """returns a dictionary of the horizontal adjacencies

        Args:
            coordinate (list): the origin coordinate

        Returns:
            dict: the horizontally adjacent coordinates and their values. 
        """
        x, y = coordinate[0], coordinate[1]
        adj_x = {}

        if x > 0:
            adj_x[(x - 1, y)] = self.gridmap[y][x - 1]
        if x < self.width - 1:
            adj_x[(x + 1, y)] = self.gridmap[y][x + 1]

        return adj_x
    
    def adj_y(self, coordinate) -> "dict":
        """returns a dictionary of vertically adjacent coordinates and their values.

        Args:
            coordinate (list): the origin coordinate

        Returns:
            dict: the vertically adjacent coordinates and their values. 
        """
        x, y = coordinate[0], coordinate[1]
        adj_y = {}

        if y > 0:
            adj_y[(x, y - 1)] = self.gridmap[y - 1][x]
        if y < self.height - 1:
            adj_y[(x, y + 1)] = self.gridmap[y + 1][x]

        return adj_y
    
    def scan_grid(self) -> "dict":
        """populates the unique_values dictionary with all the locations of all the unique characters.
        
        Args: 
            Self for the grid.

        Returns:
            dict: a dict containing each unique character as a key and a list of found locations as a value.
        """
        for y in range(0,self.height):
            for x in range(0,self.width):
                self.unique_values[self.gridmap_t[x][y]].append((x,y))
        
        return True

    # right/east = x + 1  |  left/west = x - 1
    # down/south = y + 1  |  up/north = y - 1
    def look_east(self,search_pos):
        search_x,search_y = search_pos[0],search_pos[1]
        try:
            coordinate = (search_x + 1, search_y)
            if coordinate[0] < 0 or coordinate[1] < 0:
                return False,False
            lookup = self.gridmap[search_y][search_x + 1]
            return coordinate, lookup
        except:
            return False, False

    def look_west(self, search_pos):
        search_x,search_y = search_pos[0],search_pos[1]
        try:
            coordinate = (search_x - 1, search_y)
            if coordinate[0] < 0 or coordinate[1] < 0:
                return False,False
            lookup = self.gridmap[search_y][search_x - 1]
            return coordinate, lookup
        except:
            return False, False
        
    def look_north(self, search_pos):
        search_x,search_y = search_pos[0],search_pos[1]
        try:
            coordinate = (search_x, search_y - 1)
            if coordinate[0] < 0 or coordinate[1] < 0:
                return False,False
            lookup = self.gridmap[search_y - 1][search_x]
            return coordinate, lookup
        except:
            return False, False
        
    def look_south(self, search_pos):
        search_x,search_y = search_pos[0],search_pos[1]
        try:
            coordinate = (search_x, search_y + 1)
            if coordinate[0] < 0 or coordinate[1] < 0:
                return False,False
            lookup = self.gridmap[search_y + 1][search_x]
            return coordinate, lookup
        except:
            return False, False

    def look_northeast(self, search_pos):
        search_x,search_y = search_pos[0],search_pos[1]
        try:
            coordinate = (search_x + 1, search_y - 1)
            if coordinate[0] < 0 or coordinate[1] < 0:
                return False,False
            lookup = self.gridmap[search_y - 1][search_x + 1]
            return coordinate, lookup
        except:
            return False, False

    def look_southeast(self, search_pos):
        search_x,search_y = search_pos[0],search_pos[1]
        try:
            coordinate = (search_x + 1, search_y + 1)
            if coordinate[0] < 0 or coordinate[1] < 0:
                return False,False
            lookup = self.gridmap[search_y + 1][search_x + 1]
            return coordinate, lookup
        except:
            return False, False

    def look_northwest(self, search_pos):
        search_x,search_y = search_pos[0],search_pos[1]
        try:
            coordinate = (search_x - 1, search_y - 1)
            if coordinate[0] < 0 or coordinate[1] < 0:
                return False,False
            lookup = self.gridmap[search_y - 1][search_x - 1]
            return coordinate, lookup
        except:
            return False, False

    def look_southwest(self, search_pos):
        search_x,search_y = search_pos[0],search_pos[1]
        try:
            coordinate = (search_x - 1, search_y + 1)
            if coordinate[0] < 0 or coordinate[1] < 0:
                return False,False
            lookup = self.gridmap[search_y + 1][search_x - 1]
            return coordinate, lookup
        except:
            return False, False

    def look_vertical(self, search_pos):
        look = {
            "N": self.look_north(search_pos),
            "S": self.look_south(search_pos),
        }
        return look

    def look_horizontal(self,search_pos):
        look = {
            "E": self.look_east(search_pos),
            "W": self.look_west(search_pos),
        }
        return look

    def look_around(self,search_pos):
        look = {
            "N": self.look_north(search_pos),
            "S": self.look_south(search_pos),
            "E": self.look_east(search_pos),
            "W": self.look_west(search_pos),
            "NE": self.look_northeast(search_pos),
            "NW": self.look_northwest(search_pos),
            "SE": self.look_southeast(search_pos),
            "SW": self.look_southwest(search_pos),
        }        
        return look