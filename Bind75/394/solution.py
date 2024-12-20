
s ="3[z]2[2[y]pq4[2[jk]e1[f]]]ef"

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
                current_string =previous_string + current_string*current_num
            else:
                # means only the char
                current_string +=char
        return current_string