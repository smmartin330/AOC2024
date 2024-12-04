from puzzle_data import *
from time import time
import re
import numpy
from grid import Grid

def elapsed_time(start_time):
    return f"{round(time() - start_time, 8)}s\n"

class Puzzle():
    def __init__(self,input_text):
        self.input_text = input_text
        self.input_list = input_text.strip().split('\n')

        self.valid_words = ['XMAS', 'SAMX']
        self.all_x = []
        
        self.grid = Grid(self.input_list)
        
        self.grid.scan_grid()
        
        pass
        
    def process_new_input(self):           
        self.input_list = self.input_text.strip().split('\n')
        
    def p1(self):
        self.found_words = []
        
        for found_x in self.grid.unique_values['X']:          
            search = self.grid.adj(found_x)
            for found_m,value in search.items():
                if value == "M":
                    this_candidate = {"coordinates": [found_x,found_m], "direction": ""}
                    x_delta = found_x[0] - found_m[0]
                    y_delta = found_x[1] - found_m[1]
                    if y_delta == -1:
                        this_candidate["direction"] += "S"
                    elif y_delta == 1:
                        this_candidate["direction"] += "N"
                    if x_delta == -1:
                        this_candidate["direction"] += "E"
                    elif x_delta == 1:
                        this_candidate["direction"] += "W"
                    
                    match this_candidate["direction"]:
                        case "N":
                            check_a = self.grid.look_north(found_m)
                            if check_a[1] == "A":
                                check_s = self.grid.look_north(check_a[0])
                                if check_s[1] == "S":
                                    this_candidate["coordinates"].append(check_a[0])
                                    this_candidate["coordinates"].append(check_s[0])
                                    self.found_words.append(this_candidate)                                
                        case "S":
                            check_a = self.grid.look_south(found_m)
                            if check_a[1] == "A":
                                check_s = self.grid.look_south(check_a[0])
                                if check_s[1] == "S":
                                    this_candidate["coordinates"].append(check_a[0])
                                    this_candidate["coordinates"].append(check_s[0])
                                    self.found_words.append(this_candidate)
                        case "E":
                            check_a = self.grid.look_east(found_m)
                            if check_a[1] == "A":
                                check_s = self.grid.look_east(check_a[0])
                                if check_s[1] == "S":
                                    this_candidate["coordinates"].append(check_a[0])
                                    this_candidate["coordinates"].append(check_s[0])
                                    self.found_words.append(this_candidate)
                        case "W":
                            check_a = self.grid.look_west(found_m)
                            if check_a[1] == "A":
                                check_s = self.grid.look_west(check_a[0])
                                if check_s[1] == "S":
                                    this_candidate["coordinates"].append(check_a[0])
                                    this_candidate["coordinates"].append(check_s[0])
                                    self.found_words.append(this_candidate)
                        case "NE":
                            check_a = self.grid.look_northeast(found_m)
                            if check_a[1] == "A":
                                check_s = self.grid.look_northeast(check_a[0])
                                if check_s[1] == "S":
                                    this_candidate["coordinates"].append(check_a[0])
                                    this_candidate["coordinates"].append(check_s[0])
                                    self.found_words.append(this_candidate)
                        case "NW":
                            check_a = self.grid.look_northwest(found_m)
                            if check_a[1] == "A":
                                check_s = self.grid.look_northwest(check_a[0])
                                if check_s[1] == "S":
                                    this_candidate["coordinates"].append(check_a[0])
                                    this_candidate["coordinates"].append(check_s[0])
                                    self.found_words.append(this_candidate)
                        case "SE":
                            check_a = self.grid.look_southeast(found_m)
                            if check_a[1] == "A":
                                check_s = self.grid.look_southeast(check_a[0])
                                if check_s[1] == "S":
                                    this_candidate["coordinates"].append(check_a[0])
                                    this_candidate["coordinates"].append(check_s[0])
                                    self.found_words.append(this_candidate)
                        case "SW":
                            check_a = self.grid.look_southwest(found_m)
                            if check_a[1] == "A":
                                check_s = self.grid.look_southwest(check_a[0])
                                if check_s[1] == "S":
                                    this_candidate["coordinates"].append(check_a[0])
                                    this_candidate["coordinates"].append(check_s[0])
                                    self.found_words.append(this_candidate)

        self.p1_solution = len(self.found_words)
        return True

    def p2(self):
        self.found_words = []
        for found_a in self.grid.unique_values['A']:          
            northeast = self.grid.look_northeast(found_a)
            northwest = self.grid.look_northwest(found_a)
            southeast = self.grid.look_southeast(found_a)
            southwest = self.grid.look_southwest(found_a)

            pair_1 = [northeast[1],southwest[1]]
            pair_2 = [northwest[1],southeast[1]]
            valid_pairs = [['M', 'S'], ['S','M']]
            if pair_1 in valid_pairs and pair_2 in valid_pairs:
                self.found_words.append(found_a)
            
        self.p2_solution = len(self.found_words)

        return True

def main():
    if P1_SAMPLE_SOLUTION:            
        print("PART 1\nTesting Sample...\n")
        start_time = time()
        sample = Puzzle(input_text=P1_SAMPLE_INPUT)
        sample.p1()
        if P1_SAMPLE_SOLUTION == sample.p1_solution:
            print("Sample correct.")
        else:
            print(f"Sample failed; Expected {P1_SAMPLE_SOLUTION}, got {sample.p1_solution}")
        print(f"Elapsed time {elapsed_time(start_time)}")
        if PUZZLE_INPUT:
            puzzle = Puzzle(input_text=PUZZLE_INPUT)
            puzzle.p1()
            print("Processing Input...\n")
            start_time = time()
            print(f'SOLUTION: {puzzle.p1_solution}')
            print(f"Elapsed time {elapsed_time(start_time)}")
        
    if P2_SAMPLE_SOLUTION:
        print("PART 2\nTesting Sample...\n")
        start_time = time()
        if P2_SAMPLE_INPUT != False:
            sample.input_text = P2_SAMPLE_INPUT
            sample.process_new_input()
        sample.p2()
        if P2_SAMPLE_SOLUTION == sample.p2_solution:
            print("Sample correct.")
        else:
            print(f"Sample failed; Expected {P2_SAMPLE_SOLUTION}, got {sample.p2_solution}")
        print(f"Elapsed time {elapsed_time(start_time)}")
        if PUZZLE_INPUT:
            print("Processing Input...\n")
            start_time = time()
            puzzle.p2()
            print(f'SOLUTION: {puzzle.p2_solution}')
            print(f"Elapsed time {elapsed_time(start_time)}")
    
if __name__ == "__main__":
    main()