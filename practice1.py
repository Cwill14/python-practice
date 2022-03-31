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


#            Convert cents into change

def convert(cents):
	money = {
		"dollar": 0,
		"quarter": 0,
		"dime": 0,
		"nickel": 0,
		"penny": 0,
	}

	while cents > 0:
		if cents >= 100:
			money["dollar"] += 1
			cents -= 100
		elif cents >= 25:
			money["quarter"] += 1
			cents -= 25
		elif cents >= 10:
			money["dime"] += 1
			cents -= 10
		elif cents >= 5:
			money["nickel"] += 1
			cents -= 5
		elif cents >= 1:
			money["penny"] += 1
			cents -= 1
		# print(f"cents = {cents}")

	answer = []
	for x in money:
		if money[x] == 1:
			answer.append(f"1 {x}")
		elif money[x] > 1:
			if x == "penny":
				answer.append(f"{money[x]} pennies")
			else:
				answer.append(f"{money[x]} {x}s")

	return answer
	
print(57, convert(57))
print(24, convert(24))
print(111, convert(111))
print(99, convert(99))
print(326, convert(326))


#											3/30/22

"""
Basic Calculator
Create a function that takes two numbers and a mathematical operator + - / * and will perform a calculation with the given numbers.

Examples
calculator(2, "+", 2) ➞ 4

calculator(2, "*", 2) ➞ 4

calculator(4, "/", 2) ➞ 2
Notes
If the input tries to divide by 0, return: "Can't divide by 0!"


"""

def calculator(num1, operator, num2):
	if operator == "+":
		return num1 + num2
	elif operator == "-":
		return num1 - num2
	elif operator == "*":
		return num1 * num2
	elif operator == "/":
		if num2 == 0:
			return "Can't divide by 0!"
		return num1 / num2
	else:
		return "Invalid operator!"


print(calculator(2, "+", 2), "== 4") # 4
print(calculator(2, "*", 3), "== 6") # 4
print(calculator(4, "/", 2), "== 2") # 2
print(calculator(4, "/", 0), "== Can't divide by 0!") # 2
print(calculator(6, "x", 2), "== Invalid operator!") # 2
print(calculator(10, "/", 3), "== 3.333") # 2