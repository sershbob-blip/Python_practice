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

    def __iadd__(self, other):
        m = self.minutes + other.minutes
        s = self.seconds + other.seconds
        m += s//60
        s = s % 60
        self.minutes = m
        self.seconds = s
        return self

    def info(self):
        return '{}:{}'.format(self. minutes, self.seconds)


t1 = Time(5, 50)
print(t1.info())  # 5:50

t2 = Time(3, 20)
print(t2.info())  # 3:20

print(id(t1))

t3 = t1 + t2
print(t3.info())  # 9:10

print(id(t1))

print(t1)
