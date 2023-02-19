# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):

        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i + 1))

        if next in ")]}":
            if(not opening_brackets_stack or not are_matching(opening_brackets_stack[-1:][0].char, next) ):
                print(i + 1)
                return False
            
            opening_brackets_stack.pop()
    
    if(opening_brackets_stack):
        print(i+1)
    
    return not opening_brackets_stack

def main():
    text = input()
    mismatch = find_mismatch(text)
    if(mismatch):
        print("Success")

if __name__ == "__main__":
    main()
