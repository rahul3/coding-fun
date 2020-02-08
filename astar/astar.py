import copy

def get_input_map():
    input_map = [[False, False, False, False],
            [True, True, False, True],
            [False, False, False, False],
            [False, False, False, False]]
    return input_map

class Node(object):
    
    def __init__(self, input_node, target_node):
        """Initalizing"""
#         print(f"Input node is {input_node}, target node is {target_node}")
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
        return hash(self.__key())
    
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
        
        
    def get_next_steps(self, coords, input_map: "list of lists") -> "list of Node objects":
        """
            Gets the value of possible options for the next step
        """
        options = []
        final_options = []
        left, right, top, bottom = "None"
        rows, cols = self.get_dimensions(input_map)
        left = (coords[0], coords[1]-1) if coords[1]-1 >= 0 else "None"
        right = (coords[0], coords[1]+1) if coords[1]+1 <= cols else "None"
        top = (coords[0]-1, coords[1]) if coords[0]-1 >= 0 else "None"
        bottom = (coords[0]+1, coords[1]) if coords[0]+1 <= rows else "None"
        
#         print(f"Current Coordinates {coords}")
#         print(f"left: {left}\t right: {right}\t top: {top}\t bottom: {bottom}")
        options = set([left, right, top, bottom])
        try:
            options.remove("None")
        except KeyError:
            pass
#         print(f"Options are {options}")
        
        if not options:
            return []
        
        for option in options:
            if option is not "None":
                final_options.append(Node(option, self.get_target()))
                
        # Over writing options
        options = [x.coords for x in final_options]
        if final_options:
            final_options = [node for node in final_options if node.is_valid(get_input_map())]
        
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
        self.cameFrom = {}
        
        self.iterations = 0
        
    def reconstruct_path(cameFrom: dict, current) -> list:
        total_path = current
        coordinates = [x.coords for x in cameFrom.keys()]
        while current in coordinates:
            current = cameFrom[current].coords
            total_path.insert(0, current)
            
        return total_path
        
        
    def astar(self, start_node=None, end_node=None):
        """ A Star algorithm"""
        self.start = self.start if start_node is None else start_node
        print(f"Current node is: {self.start}")
        self.end = self.target if end_node is None else end_node
        self.current = Node(self.start, self.end)
        self.visited_nodes.append(self.current)
        
        min_score = 0
        flag = 0
        
        self.cameFrom[self.current] = self.current.score
        print(f"Came from dict is {[x.coords for x in self.cameFrom.keys()]}")
        """node immediately preceding it on the cheapest path from start to n currently known."""
        self.cameFrom_nodes = [x for x in self.cameFrom.keys()]
        
        if self.start == self.end:
            flag = 1
            print(f"Destination Reached")

        elif flag == 0:
            while self.visited_nodes:
#                 self.iterations += 1 # testing code
#                 if self.iterations >= 4: # testing code
#                     break # testing code
                    
                for node in self.cameFrom_nodes:
                    if node.is_valid(self.input_map):
                        next_steps = node.get_next_steps(self.current.coords, self.input_map)
                        
                        if next_steps:
                            steps_scores = [x.score for x in next_steps if x not in self.visited_nodes]
                            if not steps_scores:
                                return 0
                            print(f"steps_scores is {steps_scores}")
                            min_score = min(steps_scores)
                            
                        next_nodes = [x for x in next_steps if x.score==min_score and x not in self.visited_nodes]
                        print(f"Next options are {[x.coords for x in next_nodes]}")
                            
                        if next_nodes:
                            print(f"Next node is {next_nodes[0].coords}")
                            self.cameFrom[next_nodes[0]] = next_nodes[0].score
                            print(f"Visted Nodes so far is {[x.coords for x in self.visited_nodes]}")
                            print("**********ITERATION END************\n")
                            if self.start == self.end:
                                break
                            self.astar(next_nodes[0].coords, self.end)
                
        return [x.coords for x in self.visited_nodes]

if __name__ == "__main__":
    a = AStar()
    a.astar()