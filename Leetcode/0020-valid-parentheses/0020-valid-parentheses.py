class Solution(object):
    def isValid(self, s):
        stack = []
        top = -1
        for i in range(len(s)):
            curr = s[i]
            if(len(stack) > 0):
                if(curr == ")" and stack[top] == "("):
                    stack.pop(top)
                    top -= 1
                elif(curr == "]" and stack[top] == "["):
                    stack.pop(top)
                    top -= 1
                elif(curr == "}" and stack[top] == "{"):
                    stack.pop(top)
                    top -= 1
                else:
                    stack.append(curr)
                    top += 1
            else:
                stack.append(curr)
                top += 1
            
            # print(curr, top)
            # print(stack)

        if(len(stack) == 0):
            return True
        else:
            return False