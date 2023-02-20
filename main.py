
def find_mismatch(text):
    stack = []
    brackets = {")": "(", "]": "[", "}": "{"}
    for i, char in enumerate(text):
        if char in brackets.values():
            stack.append(char)
        elif char in brackets.keys():
            if not stack or brackets[char] != stack.pop():
                return i + 1
    return stack[0][1] + 1 if stack else "Success"



def main():
    text = input()
    if "I" in text:
        text = input()
        mismatch = find_mismatch(text)
        print(mismatch)


if _name_ == "_main_":
    main()
