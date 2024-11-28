class Jar:
    def __init__(self, capacity=12):
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer.")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if not isinstance(n, int) or n <= 0:
            raise ValueError("The number of cookies to deposit must be a positive integer.")
        if self._size + n > self._capacity:
            raise ValueError("Exceeding jar capacity.")
        self._size += n

    def withdraw(self, n):
        if not isinstance(n, int) or n <= 0:
            raise ValueError("The number of cookies to withdraw must be a positive integer.")
        if self._size < n:
            raise ValueError("Not enough cookies in the jar.")
        self._size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Capacity must be a non-negative integer.")
        if value < self._size:
            raise ValueError("New capacity cannot be less than the current number of cookies.")
        self._capacity = value

    @property
    def size(self):
        return self._size
