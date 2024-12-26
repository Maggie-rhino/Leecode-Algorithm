# class Solution(object):
#     def compress(self, chars):
#         """
#         :type chars: List[str]
#         :rtype: int
#         """

chars =["a","a","b","b","c","c","c"]

previous =""
preffix =0
l =0
idx =0
while True:
    if idx > len(chars)-1:
        break
    current =chars[idx]
    if previous ==current:
        l +=1
    else:
        # save the previous 
        if previous !="":
            if l ==1:
                chars =[previous] +chars
                preffix +=1
            else:
                chars[preffix] = previous
                l_s = len(str(l))
                for i in range(preffix+1,l_s):
                    chars[i] = str(l)[i-preffix-1]
                preffix = l_s+1
            idx = idx + preffix
            l=0
        previous =current
    idx +=1

print(preffix)
print(chars)            

                 