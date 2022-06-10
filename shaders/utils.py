class vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """ Elementwise vector addition """
        return vec2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """ Elementwise vector subtraction """
        return vec2(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        """ Scale each vector element by a float """
        return vec2(self.x * other, self.y * other)

    def __truediv__(self, other):
        """ Scale each vector element by a float """
        return vec2(self.x / other, self.y / other)

    def __neg__(self):
        return vec2(-self.x, -self.y)

    def elements(self, elements):
        """ Emulate things like foo.xy using foo.elements("xy") """
        return elements(self, elements)

class vec3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        """ Elementwise vector addition """
        return vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        """ Elementwise vector subtraction """
        return vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        """ Scale each vector element by a float """
        return vec3(self.x * other, self.y * other, self.z * other)

    def __truediv__(self, other):
        """ Scale each vector element by a float """
        return vec3(self.x / other, self.y / other, self.z / other)

    def __neg__(self):
        return vec3(-self.x, -self.y, -self.z)

    def elements(self, elements):
        """ Emulate things like foo.xy using foo.elements("xy") """
        return elements(self, elements)

class vec3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        """ Elementwise vector addition """
        return vec3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        """ Elementwise vector subtraction """
        return vec3(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        """ Scale each vector element by a float """
        return vec3(self.x * other, self.y * other, self.z * other)

    def __truediv__(self, other):
        """ Scale each vector element by a float """
        return vec3(self.x / other, self.y / other, self.z / other)

    def __neg__(self):
        return vec3(-self.x, -self.y, -self.z)

    def elements(self, elements):
        """ Emulate things like foo.xy using foo.elements("xy") """
        return elements(self, elements)

def mix(a, b, c):
    """ Linearly interpolate between a and b, with c being the proportion of a """
    return a * c + b * (1.0 - c)

def clamp(x, low, high):
    """ Clamp the value x to between low and high """
    return min(max(x, low), high)