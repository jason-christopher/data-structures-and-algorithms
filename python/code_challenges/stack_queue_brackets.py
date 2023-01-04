from data_structures.stack import Stack


def multi_bracket_validation(string):
    stack, opened, closed = Stack(), ["{", "[", "("], ["}", "]", ")"]
    for x in string:
        stack.push(x) if x in opened else None
        if x in closed and not stack.is_empty():
            if opened.index(stack.pop()) != closed.index(x):
                return False
    if stack.is_empty():
        return True
    return False
