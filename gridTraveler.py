import time

#normal recursive approach
def normal_gridTraveler(row,column):
	if row == 1 and column == 1 : #Final grid
		return 1
	if row == 0 or column == 0 : #Out of grid / Further steps are not possible  
		return 0
	downstep = normal_gridTraveler(row-1,column) #moving downwards
	rightstep= normal_gridTraveler(row,column-1) #moving right side of the grid
	return downstep+rightstep   #For find total possible steps

def DP_gridTraveler(row,column,memo={}) :  #memo is a dictionary ,this will store an intermediate subproblems
	key = str(row)+","+str(column)   #Unique key for memo
	rkey= str(column)+","+str(row)	 #Unique key for memo  ,gridTraveler(n,m) = gridTraveler(m,n)
	if key in memo:					 #Check if already DP_gridTraveler(n,m) solved or not
		return memo[key]			 #If true return solved answer
	if rkey in memo:			
		return memo[rkey]
	if row == 1 and column == 1:	#Final grid
		return 1
	if row == 0 or column == 0:		#Out of grid / Further steps are not possible
		return 0
	downstep =DP_gridTraveler(row-1,column,memo)
	rightstep=DP_gridTraveler(row,column-1,memo)
	memo[key] = memo[rkey]= downstep+rightstep
	return memo[key]


if __name__=="__main__":
	start = time.time()
	steps = normal_gridTraveler(10,10)
	print("Total steps : %d : Time Taken : %s"%(steps,str(time.time()-start)))

	start = time.time()
	steps = DP_gridTraveler(10,10)
	print("Total steps : %d : Time Taken : %s"%(steps,str(time.time()-start)))


'''
Total steps : 48620 : Time Taken : 0.12
Total steps : 48620 : Time Taken : 0.0
'''