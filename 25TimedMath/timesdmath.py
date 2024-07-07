import random 
import time

OPERATORS = ["+","-"]
MIN_OPERAND = 3
MAX_OPERAND = 10
TOTAL_PROBLEMS = 2

def genarate_prob():
    left = random.randint(MIN_OPERAND,MAX_OPERAND)
    right = random.randint(MIN_OPERAND,MAX_OPERAND)

    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)

    answer = eval(expr)
  
    return expr,answer


wrong = 0
input("Press enter to start : ")
print("--------------------------")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr,answer = genarate_prob()
    while True:
        guess = input(f"problem #{i+1}: {expr} = ")
        if str(answer) == guess:
            break
        wrong += 1
end_time = time.time()
total_time = end_time -start_time

print("----------------------------")
print(f"Nice work! You finish in {total_time:.2f}, seconds.")