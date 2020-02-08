import copy

input_map = [[False, False, False, False],
            [True, True, False, True],
            [False, False, False, False],
            [False, False, False, False]]

class Node(object):
    
    def __init__(self, input_node, target_node):
        """Initalizing"""
        print(f"Input node is {input_node}, target node is {target_node}")
        self.coords = input_node
        self.target_coords = target_node
        self.score = self.heuristic(input_node, target_node)
        
    def __eq__(self, other):
        if isinstance(other, Node):
            return self.coords == other.coords
        return False
    
    def __gt__(self, other):
        if isinstance(other, Node):
            return self.score > other.score
        return False
    
    def __lt__(self, other):
        if isinstance(other, Node):
            return self.score > other.score
        return False
    
    def __key(self):
        return (self.coords, self.target_coords)

    def __hash__(self):
        return hash(self.__key__())
    
    def __getitem__(self, indx):
        p = copy.copy(self)
        p.coords = p.coords[indx]
        p.target_coords = p.target_coords[indx]
        return p
    
    
    def is_valid(self, input_map: "list of lists") -> bool:
        """
        Checking if the coordinate is a valid one i.e if we can step on it
        For the given problem, we can only step on a coordinate which is 'False'
        """
        if input_map[self.coords[0]][self.coords[1]] == False:
            return True
        else:
            return False
        
        
    def get_next_steps(self, input_map: "list of lists") -> "list of Node objects":
        """
            Gets the value of possible options for the next step
        """
        options = []
        final_options = []
        left, right, top, bottom = "None"
        rows, cols = self.get_dimensions(input_map)
        left = (self.coords[0]-1, self.coords[1]) if self.coords[0]-1 >= 0 else "None"
        right = (self.coords[0]+1, self.coords[1]) if self.coords[0]+1 <= cols else "None"
        top = (self.coords[0], self.coords[1]-1) if self.coords[1]-1 >= 0 else "None"
        bottom = (self.coords[0], self.coords[1]+1) if self.coords[1]+1 <= rows else "None"
        
        options = set([left, right, top, bottom])
        try:
            options.remove("None")
        except KeyError:
            pass
        
        for option in options:
            if option is not None:
                final_options.append(Node(option, self.get_target()))
                
        # Over writing options
        options = [x.coords for x in final_options]
        
        return final_options
    
    
    def heuristic(self, a: tuple, b: tuple) -> float:
        """ Heuristic for the A star algorithm """
        x1, y1 = a[0], a[1]
        x2, y2 = b[0], b[1]
        return ((x2 - x1)**2 + (y2 - y1)**2)**(1/2.0)

    
    def get_value(self, input_map: "list of lists", node=None) -> bool:
        """Get the value of the node in a list of lists"""
        if node is None:
            return input_map[self.coords[0]][self.coords[1]]
        else:
            return input_map[node.coords[0]][node.coords[1]]
        
        
    def get_target(self) -> tuple:
        "getter for target coordinates"
        return self.target_coords
    
    
    def get_dimensions(self, input_map: "list of lists") -> "rows(int), cols(int)":
        """Getting the dimensions of the list of lists as input"""
        rows = len(input_map)
        for row in input_map:
            cols = len(row)
            break
        return rows-1, cols-1
    
    def get_hscore(self):
        return self.score

class AStar(object):
    
    def __init__(self, input_map=None, initial=None, target=None):
        
        if input_map is None:
            self.input_map = [[False, False, False, False],
                                [True, True, False, True],
                                [False, False, False, False],
                                [False, False, False, False]]
            
        if initial is None:
            self.start = (2, 2)
            
        if target is not None:
            self.target = target
        else:
            self.target = (0, 0)
            
        self.visited_nodes = []  # all coordinates visited
        self.path = [] # traversal path
        
    def astar(self, start_node=None, end_node=None):
        """ A Star algorithm"""
        print(self.target)
        self.start = start_node if start_node is not None else self.start
        self.end = self.target if end_node is None else end_node
        self.current = Node(self.start, self.end)
        self.iterations = 0 # testing code
        self.visited_nodes.append(self.current)
        
        if self.start == self.end:
            print(f"Destination Reached {end_node}")
        else:
            while self.visited_nodes:
                self.iterations += 1 # testing code
                if self.iterations >= 4: # testing code
                    break # testing code
                    
                for node in self.visited_nodes:
                    if self.current.is_valid(input_map):
                        next_steps = self.current.get_next_steps(input_map)
                        
                        if next_steps:
                            for n_node in next_steps:
                                if n_node not in self.visited_nodes and n_node.is_valid(input_map):
                                    self.visited_nodes.append(n_node)
                                    break;
                            min_score = min([x.score for x in self.visited_nodes])
                            next_node = [x for x in self.visited_nodes if x.score==min_score]
                            if next_node:
                                print(f"Next node is {next_node}")
                                
                                
                            ### TO DO

        return [x.coords for x in self.visited_nodes]

a = AStar()
a.astar()