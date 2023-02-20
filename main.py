def are_matching(left, right):
    matching_pairs = {"(": ")", "[": "]", "{": "}"}
    return left in matching_pairs and right == matching_pairs[left]

def find_mismatch(text):
    stack = []
    for i, c in enumerate(text, 1):
        if c in '([{':
            stack.append((c, i))
        elif c in ')]}':
            if not stack or not are_matching(stack.pop()[0], c):
                return i
    return 'Success' if not stack else stack[0][1]

if 'I' in input():
    print(find_mismatch(input()))
