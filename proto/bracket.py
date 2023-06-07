import numpy as np
from option import Result, Option, Ok, Err

class Item:
    name: str
    def __init__(self, name:str) -> None:
        self.name=name

    def preview(self):
        print(self.name)

    def __str__(self) -> str:
        return self.name

class Comparison:
    left: Item
    right: Item
    result: Option
    def __init__(self, left, right) -> None:
        self.result = None
        self.left = left
        self.right = right
        pass
    
    def resolve(self):
        print("1.",end=""); self.left.preview()
        print("2.",end=""); self.right.preview()
        user_choice = ""
        while user_choice not in ["1","2"]:
            user_choice = input("Which do you prefer? (1/2): ")
            if user_choice == "1":
                self.result = Ok(self.left)
            elif user_choice == "2":
                self.result = Ok(self.right)
        
    
class ByeComparison(Comparison):

    def __init__(self, item) -> None:
        super().__init__(item, None)
        self.result = Ok(item)

    def resolve(self):
        # Already resolved
        pass
    

class Bracket:
    in_size:int
    out_size:int
    candidates:list
    comparisons:list
    def __init__(self, in_size:int, out_size:int, candidates:list) -> None:
        self.in_size=in_size
        self.out_size=out_size
        assert self.in_size > self.out_size
        assert len(candidates) == in_size
        self.candidates = candidates
        self.build_comparisons()

    def build_comparisons(self):
        self.comparisons = []
        for i in range(0,self.in_size,2):
            print(f"Comparing {i} to {i+1}")
        

class FirstBracket(Bracket):
    comps:int # number of eliminations/comparisons
    byes:int # number of byes
    def __init__(self, in_size: int, candidates: list) -> None:
        base = np.ceil(np.log2(in_size))
        out_size = 2**(base-1)
        self.comps = (int) (in_size-out_size) # how many we need to eliminate
        self.byes = in_size - 2*self.comps # how many we have leftover to pass straight to next bracket
        super().__init__(in_size, out_size, candidates)

    def build_comparisons(self):
        self.comparisons = []
        for i in range(0, self.comps*2, 2):
            left = self.candidates[i]
            right = self.candidates[i+1]
            print(f"Comparing {left} to {right}")
            self.comparisons.append(Comparison(left, right))
        byes_start = self.comps*2
        for i in range(byes_start, byes_start+self.byes):
            left = self.candidates[i]
            print(f"Giving bye to {left}")
            self.comparisons.append(ByeComparison(left))
    
if __name__ == "__main__":
    FirstBracket(14,range(14))
    Bracket(16,8,range(16))