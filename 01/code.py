from input import *
from sample import *
import argparse
from time import time
import json
import math

DAY = 1

P1_SAMPLE_SOLUTION = 11

P2_SAMPLE_SOLUTION = 31

def elapsed_time(start_time):
    return f"{round(time() - start_time, 8)}s\n"

class Puzzle():
    def __init__(self,input_text):
        self.input_text = input_text
        self.input_list = input_text.strip().split('\n')
                
    def p1(self):
        self.p1_solution = 0
        self.left_col, self.right_col = [],[]
        
        for entry in self.input_list:
            entries = entry.split()
            self.left_col.append(entries[0])
            self.right_col.append(entries[1])
            
        self.left_col.sort()
        self.right_col.sort()
        
        for i in range(0,len(self.left_col)):
            this_sum = int(self.left_col[i]) - int(self.right_col[i])
            if this_sum < 0:
                self.p1_solution -= this_sum
            else:
                self.p1_solution += this_sum
        
        return True

    def p2(self):
        self.p2_solution = 0
        for i in range(0,len(self.left_col)):
            score = int(self.left_col[i]) * int(self.right_col.count(self.left_col[i]))
            self.p2_solution += score
        return True

def main():
    parser = argparse.ArgumentParser(description=f'AOC2022 Puzzle Day { DAY }')
    parser.add_argument("-p", "--showpuzzle", help="Display Puzzle Text", action='store_true')
    parser.add_argument("-s", "--showsample", help="Display Sample Input", action='store_true')
    args = parser.parse_args()
    
    if args.showpuzzle:
        print(f"###############\nAOC 2022 DAY {DAY} PUZZLE TEXT\n###############")
        print(PUZZLE_TEXT)
    
    if args.showsample:
        print(f"###############\nAOC 2022 DAY {DAY} SAMPLE INPUT\n###############")
        print(SAMPLE_INPUT.strip())
        print(f"\n###############\nAOC 2022 DAY {DAY} P1 SAMPLE SOLUTION\n###############")
        print(P1_SAMPLE_SOLUTION)
        print(f"\n###############\nAOC 2022 DAY {DAY} P2 SAMPLE SOLUTION\n###############")
        print(P2_SAMPLE_SOLUTION)
    

    if P1_SAMPLE_SOLUTION:            
        print("PART 1\nTesting Sample...\n")
        start_time = time()
        sample = Puzzle(input_text=SAMPLE_INPUT)
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