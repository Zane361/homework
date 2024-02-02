import random
import operator

def problem_creator():
    operator_map = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul
    }
    random_num1 = random.randint(1, 10)
    random_num2 = random.randint(1, 10)
    random_oper = random.choice(list(operator_map.keys()))
    result = operator_map[random_oper](random_num1, random_num2)
    user_input = input(f"{random_num1} {random_oper} {random_num2} = ? ")
    try:
        user_input = float(user_input)
        return user_input == result
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return False