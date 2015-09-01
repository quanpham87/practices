print("practice stacks and queues")
#stack: first in last out
#queue: first in first out

# Q26
def q26(str):
    stack = []
    fail = False
    for i in str:
        if i == "(":
            stack.append(i)
        else:
            if len(stack) == 0:
                fail = True
                break
            else:
                stack.pop()
    
    if len(stack) > 0 or fail:
        print("Err")
    else:
        print("Pass")

q26("((()()))")
q26("(()()))")
q26("((()()))())")

# Q27
def q27(str):
    stack = []
    fail = False
    for i in str:
        if i == "(" or i == "{" or i == "[":
            stack.append(i)
        else:
            if len(stack) == 0:
                fail = True
                break
            else:
                check = stack.pop()
                if (i == "(" and check != ")") or (i == "{" and check != "}") or (i == "[" and check != "]"):
                    fail = True
                    break
    if len(stack) > 0 or fail:
        print("Err")
    else:
        print("Pass")

q27("[({}([])]")
q27("[({}([]))]")

# use 1 array to implement 3 stacks? single dimension or multiple? multiple is easy
# implement a min() function for a stack? easy: whenever u put it, compare to the local min