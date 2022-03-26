#                       3/26/22


# single line comment
print("Hello World")
"""
multi-line comment?
"""

#                        Football Points
"""
Create a function that takes the number of wins, draws and losses and calculates the number of points a football team has obtained so far.

wins get 3 points
draws get 1 point
losses get 0 points
Examples
football_points(3, 4, 2) ➞ 13

football_points(5, 0, 2) ➞ 15

football_points(0, 0, 1) ➞ 0
Notes
Inputs will be numbers greater than or equal to 0.

"""

def football_points(wins, draws, losses):
	w = wins * 3
	d = draws * 1
	l = losses * 0
	total = w + d + l
	print(total)
  #or
	return (wins * 3) + draws

football_points(3, 4, 2) # 13
print("--------------------")
football_points(5, 0, 2) # 15
print("--------------------")
football_points(0, 0, 1) # 0
