
from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next_char in enumerate(text, 1):
        if next_char in "([{":
            opening_brackets_stack.append(Bracket(next_char, i))
        elif next_char in ")]}":
            if not opening_brackets_stack:
                return i
            top = opening_brackets_stack.pop()
            if not are_matching(top.char, next_char):
                return i
    if opening_brackets_stack:
        return opening_brackets_stack[0].position
    return "Success"


def main():
    text = input()
    mismatch = find_mismatch(text)
    if mismatch == "Success":
        print(mismatch)
    else:
        print(mismatch)


if _name_ == "_main_":
    main()
