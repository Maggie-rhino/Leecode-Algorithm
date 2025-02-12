

# the thought is that:
#  store all the previous string in the stack,
#  the stack may contains more than one item; each pair is (previous_string, repeat_number);
#  once we meet the "]", it means we get one small pattern, and need to store it into the stack
class Solution:
    def decodeString(self, s: str) -> str:
        stack =[]
        current_num =0
        current_string =""
        for char in s:
            if char.isdigit():
                current_num = current_num*10 + int(char)
            elif char =="[":
                # means we meet to a new compression, and we need to save the previous result
                stack.append((current_string,current_num))
                current_string =""
                current_num =0
            elif char =="]":
                #  means one compression is end, and we need to decode it
                previous_string, repeat_num = stack.pop()
                current_string =previous_string + current_string*repeat_num
            else:
                # means only the char
                current_string +=char
            print(stack, current_string)
        return current_string
    

s = "3[a]2[bc]"

solution = Solution()
current_string = solution.decodeString(s)
print(current_string)  # expect "aaabcbc"

