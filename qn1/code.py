class Solution:
    def isValid(self, s: str) -> bool:
        # Stack to keep track of opening brackets
        stk = []
        # Mapping of closing to opening brackets
        mapping = {')': '(', '}': '{', ']': '['}
        
        # Iterate through each character in the string
        for c in s:
            # If it's an opening bracket, push it onto the stack
            if c in "({[":
                stk.append(c)
            else:
                # If it's a closing bracket, check the stack
                if not stk:  # Stack is empty, no matching opening bracket
                    return False
                if stk[-1] != mapping[c]:  # Top of stack doesn't match current closing bracket
                    return False
                stk.pop()  # Pop the matching opening bracket
        
        # After processing all characters, check if stack is empty
        return len(stk) == 0
