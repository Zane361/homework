class Weekdays:
    days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
    counter = 0
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.counter < len(self.days):
            result = self.days[self.counter]
            self.counter += 1
            return result
        raise StopIteration
    

class Months:
    months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
    counter = 0
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.counter < len(self.months):
            result = self.months[self.counter]
            self.counter += 1
            return result
        raise StopIteration


class Users:
    users= []
    counter = 0

    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.users.append(self)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.counter < len(self.users):
            result = self.users[self.counter]
            self.counter += 1
            return result
        raise StopIteration
    
