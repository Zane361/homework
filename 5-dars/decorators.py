from random_problem import problem_creator
import time


# 1)
def checker(func):
    def wrapper(*args):
        if problem_creator():
            return func(*args)
        else:
            return None
    return wrapper


# 2)
def check(func):
    def wrapper(*args):
        if problem_creator():
            return func(*args)
        else:
            raise ValueError('Xatolik')
    return wrapper


# 3)


def time_returner(func):
    def wrapper(*args):
        start_time = f"{time.ctime()} {time.time()}"
        result = func(*args)
        end_time = f"{time.ctime()} {time.time()}"
        return f"{result} \nFunksiya ishga tushgan vaqt: {start_time} \nFunskiya ishlashni tugatgan vaqt: {end_time}"
    return wrapper


# 4)


def time_between(func):
    def wrapper(*args):
        start_time = time.time()
        result = func(*args)

        time.sleep(3)
        # Yuqoridagini funksiyani tekshirish uchun yoqing

        end_time = time.time()
        return f"{result} \nFunksiya {round(end_time - start_time)} soniya ishladi"
    return wrapper