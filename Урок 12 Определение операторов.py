class Time:

    def __init__(self, minutes, seconds):
        self. minutes = minutes
        self.seconds = seconds

    def __add__(self, other):
        m = self. minutes + other. minutes
        s = self.seconds + other.seconds
        m += s // 60
        s = s % 60
        return Time(m, s)
    
    def __str__(self):
        return '{}:{}'.format(self.minutes, self.seconds)

    # def __iadd__(self, other):
    #     m = self.minutes + other.minutes
    #     s = self.seconds + other.seconds
    #     m += s//60
    #     s = s % 60
    #     self.minutes = m
    #     self.seconds = s
    #     return self

    # def info(self):
    #     return '{}:{}'.format(self. minutes, self.seconds)

    def __repr__(self):
        return 'Time ({}, {})'.format (self. minutes, self.seconds)


t1 = Time(5,50)

print(t1)  # 5:50
print(repr(t1)) # Time (5, 50)

# t2 = Time(3,20)

# print(t2) # 3:20


# t3 = t1 + t2

# print(t3) # 9:10