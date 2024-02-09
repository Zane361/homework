from contextlib import contextmanager
# 1


class MyContextManager:
    def __init__(self):
        self.data = []

    def append_data(self, item):
        self.data.append(item)

    def __enter__(self):
        return self

    def __exit__(self, error_type, error_value, traceback):
        if error_type is not None:  
            print("Xatolik ro'y berdi. Ma'lumotlar o'chirildi! ")
            self.data = []  
        else:
            print("Xatolik ro'y bermadi ")
            print("Ma'lumotlar:", self.data)


with MyContextManager() as cm:
    cm.append_data(1)
    cm.append_data(2)
    # Pastdagi kod xatolik uchun. Ishlatish uchun commentdan chiqaring
    # raise ValueError("Xatolik")
    cm.append_data(3)


# 2


@contextmanager
def my_context_manager():
    data = []
    try:
        yield data
    except Exception as e:
        print("Xatolik ro'y berdi. Ma'lumotlar o'chirildi! ")
        data.clear()  
    else:
        print("Xatolik ro'y bermadi ")
        print("Ma'lumotlar:", data)

with my_context_manager() as cm:
    cm.append(1)
    cm.append(2)
    # Pastdagi kod xatolik uchun. Ishlatish uchun commentdan chiqaring
    # raise ValueError("Xatolik")
    cm.append(3)