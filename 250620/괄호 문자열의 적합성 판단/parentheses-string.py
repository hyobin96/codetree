def is_correct(inputs):
    stack = []  
    
    for s in inputs:
        if s == '(':
            stack.append(s)
        
        else:
            if not stack:
                return False
            
            stack.pop()

    if not stack:
        return True

    return False
            
inputs = input()

if is_correct(inputs):
    print('Yes')

else:
    print('No')