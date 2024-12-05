from puzzle_data import *
from time import time
import re

def elapsed_time(start_time):
    return f"{round(time() - start_time, 8)}s\n"

class Page():
    def __init__(self) -> None:
        self.always_before = set()
        self.always_after = set()

class Puzzle():
    def __init__(self,input_text):
        self.input_text = input_text
        self.input_list = input_text.strip().split('\n')
        self.instructions = []
        self.pages = {}
        self.updates = []
        self.incorrect_updates = []
        
        for row in self.input_list:
            if "|" in row:
                instruction = row.split('|')
                self.instructions.append(instruction)
                page = int(instruction[0])
                before = int(instruction[1])
                try:
                    self.pages[page].always_before.add(before)
                except:
                    self.pages[page] = Page()
                    self.pages[page].always_before.add(before)
                
                try:
                    self.pages[before].always_after.add(page)
                except:
                    self.pages[before] = Page()
                    self.pages[before].always_after.add(page)
                                
            elif "," in row:
                update = [int(x) for x in row.split(',')]
                self.updates.append(update)
    
    def process_new_input(self):           
        self.input_list = self.input_text.strip().split('\n')
        
    def p1(self):
        self.p1_solution = 0
        for update in self.updates:
            index = 0
            update_valid = True
            while index < len(update) and update_valid == True:
                page = update[index]
                afters = set(update[index+1:])
                if self.pages[page].always_before.issuperset(afters) == False:
                    update_valid = False
                    self.incorrect_updates.append(update)
                index += 1
            
            if update_valid == True:
                middle_index = (len(update) // 2)
                self.p1_solution += update[middle_index]
            
        return True

    def p2(self):
        self.p2_solution = 0
        self.page_numbers = list(self.page_numbers)
        
        for update in self.incorrect_updates:
            index = 0
            while index < len(update):
                page = update[index]  # get page
                afters = set(update[index+1:]) # get afters
                if self.pages[page].always_before.issuperset(afters) == False: # if the set is out of order,
                    invalid_pages = list(afters.difference(self.pages[page].always_before)) #  find the invalid pages
                    for page in invalid_pages:
                        update.remove(page)
                        update.insert(index,page)
                else:
                    index += 1
            

            middle_index = (len(update) // 2)
            self.p2_solution += update[middle_index]

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