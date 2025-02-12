solution.py



# High-level solution

# step 1: we use two queues to store indices of R and D

#  step 2:  always compare the value of the first items in each queue, 
# the queue with bigger index will be banned, which means poped out;
#  then the smaller index will be updated to index+ len(senate) and append to the tail of the queue


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
    	queue_d = []
    	queue_r =[]
    	l = len(senate)
    	# step 1:seperate two team members
    	for i in range(l):
    		if senate[i]=="R":
    			queue_r.append(i)
    		else:
    			queue_d.append(i)

    	# compare
    	while (len(queue_d)>0) and (len(queue_r)>0):
    		d_1st = queue_d.pop(0)
    		r_1st =queue_r.pop(0)
    		if d_1st > r_1st:
    			#  then d will be banned, r will be appended to the end of the queue
    			queue_r.append(r_1st+l)
    		else:
    			queue_d.append(d_1st+l)

    	return "Dire" if len(queue_d) else "Radiant"





    	

        