from input import *
from sample import *
import argparse
from time import time
import json
import math

DAY = 2

P1_SAMPLE_SOLUTION = 2

P2_SAMPLE_SOLUTION = 4

def elapsed_time(start_time):
    return f"{round(time() - start_time, 8)}s\n"

class Puzzle():
    def __init__(self,input_text):
        self.input_text = input_text
        self.input_list = input_text.strip().split('\n')
                
    def p1(self):
        self.p1_solution = 0
        for row in self.input_list:
            row_safe = True
            row = row.split()
            row = [ int(x) for x in row ]
            
            sort_check_asc, sort_check_desc = row.copy(), row.copy()
            unique_check = list(set(row))
            unique_check.sort()
            sort_check_asc.sort()
            sort_check_desc.sort(reverse=True)
            
            if  (row not in [ sort_check_asc, sort_check_desc]) or (sort_check_asc != unique_check):
                row_safe = False
            else:
                for i in range(0,(len(row) - 1)):
                    if row[i] - row[i+1] in [-3, -2, -1, 1, 2, 3]:
                        continue
                    else:
                        row_safe = False
                        break
            if row_safe == True:
                self.p1_solution += 1
                
        return True

    def p2(self):
        self.p2_solution = 0
        rows = []
        safe_rows = []
        for row in self.input_list:
            this_row = { "original": [ int(x) for x in row.split() ]} # get the original row
            this_row["candidates"] = []
                  
            # check if original row is safe
            this_row["asc"] = this_row["original"].copy().sort()
            this_row["desc"] = this_row["original"].copy().sort(reverse=True)
            this_row["unique"] = list(set(this_row["original"])).sort()
                        
            #if row is safe, add it to rows.
            if (this_row["original"] in [this_row["asc"], this_row["desc"]]) and (this_row['asc'] == this_row['unique']):
                rows.append(this_row)
                #print(f"ROW ADDED: {this_row['original']} VALID")
            #elif the row is not safe, check for candidate replacements.
            elif (this_row["original"] not in [this_row["asc"], this_row["desc"]]) or (this_row['asc'] != this_row['unique']):
                for i in range(0,len(this_row['original'])):
                    candidate = this_row["original"][0:i] + this_row["original"][i+1:]
                    candidate_asc = candidate.copy()
                    candidate_asc.sort()
                    candidate_desc = candidate.copy()
                    candidate_desc.sort(reverse=True)
                    candidate_unique = list(set(candidate))
                    candidate_unique.sort()
                    
                    if (candidate in [candidate_asc, candidate_desc]) and (candidate_asc == candidate_unique):
                        if candidate not in this_row["candidates"]:
                            this_row["candidates"].append(candidate)
                # if candiates are found, add the row and candidates to rows
                if len(this_row["candidates"]) > 0:
                    rows.append(this_row)
                    #print(f"ROW ADDED: {this_row['original']} INVALID BUT SAFE CANDIDATES {this_row['candidates']} FOUND")
                else:
                    pass
                    #print(f"ROW DISCARDED: {this_row['original']} INVALID AND NO SAFE CANDIDATES FOUND")

        # Check safe and candidate rows
        for row in rows:
            row_safe = True
            if len(row["candidates"]) == 0:
                for i in range(0,(len(row["original"]) - 1)):
                    if row["original"][i] - row["original"][i+1] in [-3, -2, -1, 1, 2, 3]:
                        continue
                    else:
                        row_safe = False
                        break
                if row_safe == True:
                    safe_rows.append(row)
            else:
                for candidate in row["candidates"]:
                    row_safe = True
                    for i in range(0,(len(candidate) - 1)):
                        if candidate[i] - candidate[i+1] in [-3, -2, -1, 1, 2, 3]:
                            continue
                        else:
                            row_safe = False
                            break
                    if row_safe == True:
                        if row not in safe_rows:
                            safe_rows.append(row)
                
        self.p2_solution = len(safe_rows)
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