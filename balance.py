def isBalanced(expr):
    stack = []

    for char in expr:
        if char in ["(","["]:
            stack.append(char)
        else:
            if not stack:
                return False
            curr_char = stack.pop()
            if curr_char == '(':
                if char != ")":
                    return False
            if curr_char == '{':
                if char != "}":
                    return False
            if curr_char == '[':
                if char != "]":
                    return False
                
    if stack:
        return False
    return True
 


expr = "[()][(()]"
if isBalanced(expr):
    print("Balanced")
else:
    print("Not Balanced")