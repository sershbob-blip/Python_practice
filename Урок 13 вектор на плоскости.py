class MyVector:
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def __add__ (self, other):
        return MyVector (self.x + other.x, self.y + other.y)

    def __sub__(self,other):
        return MyVector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return MyVector(self.x * other, self.y * other)

    def __rmul__ (self, other):
        return MyVector (self. x * other, self. y * other)

    def __str__ (self):
        return 'MyVector ({}, {})'.format (self.x, self.y)



v1 = MyVector (-2, 5)

v2 = MyVector (3, -4)

v_sum = v1 + v2

print (v_sum) # MyVector (1, 1)

v_mul = v1 * 1.5

print (v_mul) # MyVector (-3.0, 7.5)

v_rmul = -2 * v1

print (v_rmul) # MyVector (4, -10)