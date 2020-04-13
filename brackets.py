open_list = ["[", "{", "("]
close_list = ["]", "}", ")"]

def check(myStr):
    stack = []
    for i in myStr:
        if i in open_list:
            #if you have an opening bracket, stuff it on the stack (first in, last out)
            stack.append(i)
            print("STACK FROM OPEN LIST", stack)
        elif i in close_list:
            pos = close_list.index(i)
            print("STACK FROM CLOSED LIST", stack)
            if ((len(stack) > 0) and (open_list[pos]== stack[len(stack) - 1])):
                stack.pop()
                print("...AND POPPED", stack)
            else:
                print("GAME OVER")
                return False
    if len(stack) == 0:
        return True

print("should be true", check("{[]{()}}"))
print("*****************************")
print("should be false", check("[{}{})(]"))