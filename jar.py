class Jar:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current_size = 0

    def __str__(self):
        return '🍪' * self.current_size
        ...

    def deposit(self,n):
        if self.current_size + n > self.capacity:
            raise ValueError("Deposit exceeds jar capacity")
        self.current_size += n
        ...

    def withdraw(self, n):
        if n > self.current_size:
            raise ValueError("Withdrawal exceeds jar current size")
        self.current_size -= n
        ...

    @property
    def size(self):
        return self.current_size
        ...

    @size.setter
    def size(self,current_size):
        if current_size < 0:
            raise ValueError
        if current_size > self.capacity:
            raise ValueError
        self.current_size = current_size


def main():
    if __name__ == '__main__':
        main()

