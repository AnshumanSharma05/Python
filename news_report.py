"""Japan was hit by a huge Tsunami. Lives and properties were lost. Many were injured too. A news reporter has arrived to the spot to analyse and generate report  on the number of people alive , dead and injured. His report also has a statement seeking public to help the people in need. Can you help him to generate the report by writing a Python program ? 

Note:  

If the dead count or injured count or safe count entered by the user is a negative number, then display the message "Invalid input" and stop the program.
The statement for seeking help should be "Please help the people who are suffering!!!".  
Please refer the sample input and output for more clarifications.


Sample Input 1:

Dead Count:

2000

Injured Count:

3000

Safe Count:

10000

Sample Output 1:

TSUNAMI REPORT OF JAPAN

The number of people

Dead:2000

Injured:3000

Safe:10000

Please help the people who are suffering!!!



Sample Input 2:

Dead Count:

-2000

Sample Output 2:

Invalid input
"""
dead_count=int(input("Dead Count:"))
if(dead_count<0):
	print("Invalid input")
	exit()
injured_count=int(input("Injured Count:"))
if(injured_count<0):
	print("Invalid Input")
	exit()
safe_count=int(input("Safe Count:"))
if(safe_count<0):
	print("Invalid Count")
	exit()
print("TSUNAMI REPORT OF JAPAN")
print("The nnumber of people")
print("Dead: "+str(dead_count))
print("Injured: "+str(injured_count))
print("Safe: "+str(safe_count))	
print("Please help the people who are suffering!!!")