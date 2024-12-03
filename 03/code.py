from puzzle_data import *
from time import time
import re

def elapsed_time(start_time):
    return f"{round(time() - start_time, 8)}s\n"

class Puzzle():
    def __init__(self,input_text):
        self.input_text = input_text
        self.input_list = input_text.strip().split('\n')
    
    def process_new_input(self):           
        self.input_list = self.input_text.strip().split('\n')
        
    def p1(self):
        self.p1_solution = 0
        for row in self.input_list:
            pattern = "mul\([0-9]*,[0-9]*\)"
            valid_instructions = re.findall(pattern,row)
            for instruction in valid_instructions:
                numbers = instruction[4:-1].split(',')
                self.p1_solution += (int(numbers[0]) * int(numbers[1]))
            
        return True

    def p2(self):
        self.p2_solution = 0
        instructions = True
        for row in self.input_list:
            pattern = "(mul\([0-9]*,[0-9]*\))|(do\(\))|(don\'t\(\))"
            valid_instructions = re.findall(pattern,row)            
            for instruction in valid_instructions:
                if instruction[2] == "don't()":
                    instructions = False
                elif instruction[1] == "do()":
                    instructions = True
                else:
                    if instructions == True:
                        numbers = instruction[0][4:-1].split(',')
                        self.p2_solution += (int(numbers[0]) * int(numbers[1]))

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