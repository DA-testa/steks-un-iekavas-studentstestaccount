class Bracket:
    def __init__(self, char, position):
        self.char = char
        self.position = position


def are_matching(left, right):
    matching_pairs = {"(": ")", "[": "]", "{": "}"}
    return left in matching_pairs and right == matching_pairs[left]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next_char in enumerate(text):
        if next_char in "([{":
            opening_brackets_stack.append(Bracket(next_char, i))
        elif next_char in ")]}":
            if not opening_brackets_stack:
                return i, "Unmatched closing bracket: {}".format(next_char)
            top = opening_brackets_stack[-1]
            if not are_matching(top.char, next_char):
                return i, "Expected {}, but found {}".format(
                    matching_pairs[top.char], next_char
                )
            opening_brackets_stack.pop()
    if opening_brackets_stack:
        top = opening_brackets_stack[-1]
        return top.position, "Unmatched opening bracket: {}".format(top.char)
    return -1, "Success"


def main():
    while True:
        try:
            lines = []
            while True:
                line = input()
                if line == "I'm done":
                    break
                lines.append(line)
            text = "".join(lines)
            mismatch, error_message = find_mismatch(text)
            if mismatch == -1:
                print("No mismatches found")
            else:
                print("Mismatch at position {}: {}".format(mismatch + 1, error_message))
        except (EOFError, KeyboardInterrupt):
            print("\nExiting program")
            break


if __name__ == "__main__":
    main()
