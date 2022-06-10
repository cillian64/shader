import builtins
import math


class vec:
    """ Generic vector of floats with any number of entries.  Designed to look
    and feel disconcertingly similar to the GLSL vec2/vec3/vec4 types. """

    def __init__(self, *values):
        self.values = tuple(float(x) for x in values)

    def __add__(self, other):
        """ Elementwise vector addition """
        assert len(self.values) == len(other.values)
        return vec(*(a + b for (a, b) in zip(self.values, other.values)))

    def __sub__(self, other):
        """ Elementwise vector subtraction """
        assert len(self.values) == len(other.values)
        return vec(*(a - b for (a, b) in zip(self.values, other.values)))

    def __mul__(self, other):
        """ Scale each vector element by a float """
        return vec(*(a * other for a in self.values))

    def __truediv__(self, other):
        """ Scale each vector element by a float """
        return vec(*(a / other for a in self.values))

    def __neg__(self):
        return vec(*(-a for a in self.values))

    def __eq__(self, other):
        assert len(self.values) == len(other.values)
        return all(a == b for (a, b) in zip(self.values, other.values))

    def elements(self, elements):
        """ Emulate things like foo.xy using foo.elements("xy") """
        # Check the elements string is valid

        # Only supported for scalar, vec2, vec3, vec4
        assert len(elements) >= 1 and len(elements) <= 4

        # Check element names are valid
        element_names = ['x', 'y', 'z', 'w']
        # Which element names are allowed for this size item
        valid = element_names[:len(self.values)]
        # Check all named elements are ok
        assert all(element in valid for element in elements)

        if len(elements) == 1:
            return self.values[element_names.index(elements)]
        else:
            values = (self.values[element_names.index(el)] for el in elements)
            return vec(*values)

    # Now do terrible things so you can actually write foo.xzy
    def __getattr__(self, name):
        # Work out which element names are valid, so we can raise
        # an AttributeError for anything else
        element_names = ['x', 'y', 'z', 'w']
        valid = element_names[:len(self.values)]
        elements_valid = all(element in valid for element in name)
        if len(name) >= 1 and len(name) <= 4 and elements_valid:
            return self.elements(name)
        else:
            raise AttributeError()

    def abs(self):
        """ Elementwise abs of the vector """
        return vec(*(abs(x) for x in self.values))

    def clamp(self, low, high):
        """ Elementwise clamp between low and high """
        return vec(*(min(max(x, low), high) for x in self.values))

    def fract(self):
        """ Return the fractional part of self, i.e. self - floor(self) """
        return self - self.floor()

    def floor(self):
        """ Elementwise round down to the nearest integer """
        return vec(*(math.floor(x) for x in self.values))

    def __str__(self):
        """ Stringify for printing """
        return "[" + ", ".join(str(x) for x in self.values) + "]"

    def norm(self):
        """ Return the l2-norm of this vector """
        return math.sqrt(sum(x ** 2 for x in self.values))



def vec2(*values):
    """ Shorthand for creating 2-vecs in GLSL style """
    assert(len(values) == 2)
    return vec(*values)


def vec3(*values):
    """ Shorthand for creating 3-vecs in GLSL style """
    assert(len(values) == 3)
    return vec(*values)


def vec4(*values):
    """ Shorthand for creating 4-vecs in GLSL style """
    assert(len(values) == 4)
    return vec(*values)


def mix(a, b, c):
    """ Linearly interpolate between a and b, with c being the proportion of a """
    return a * c + b * (1.0 - c)


def clamp(x, low, high):
    """ Clamp the value x to between low and high """
    if isinstance(x, vec):
        return x.clamp(low, high)
    else:
        return min(max(x, low), high)


def abs(value):
    """ Make a scalar positive or all the entries in a vec positive """
    if isinstance(value, vec):
        return value.abs()
    else:
        return builtins.abs(value)


def floor(value):
    """ Round down to the nearest integer """
    if isinstance(value, vec):
        return value.floor()
    else:
        return math.floor(value)


def fract(value):
    """ Return the fractional part of value, i.e. value - floor(value) """
    return value - floor(value)


def distance(a, b):
    """ Return the l2-distance between two points"""
    return (a - b).norm()



if __name__ == "__main__":
    print("Utils unit tests!!")

    def close(a, b):
        return builtins.abs(a - b) < 0.001

    # Test constructors and equality
    x = vec2(1.0, -2.0)
    assert x == vec(1.0, -2.0)
    x = vec3(1.0, -2.0, 3.0)
    assert x == vec(1.0, -2.0, 3.0)
    x = vec4(1.0, -2.0, 3.0, -5.0)
    assert x == vec(1.0, -2.0, 3.0, -5.0)
    assert vec(1.0, 2.0) != vec(1.0, 2.1)
    try:
        vec(1.0) != vec(1.0, 1.0)
        # This should not work.
        assert False
    except:
        pass

    # Check constructing with integers instead of floats works
    assert vec(1, 2, 3) == vec(1.0, 2.0, 3.0)

    # Test arithmetic
    assert vec(1.0, 2.0) + vec(3.0, 4.0) == vec(4.0, 6.0)
    assert vec(1.0, 2.0) - vec(0.0, 1.0) == vec(1.0, 1.0)
    assert vec(1.0, 2.0) * 2.0 == vec(2.0, 4.0)
    assert vec(1.0, 2.0) / 2.0 == vec(0.5, 1.0)
    assert -vec(1.0, 2.0) == vec(-1.0, -2.0)

    # Test other mathsy functions
    assert abs(vec(-1.0, 2.0)) == vec(1.0, 2.0)
    assert clamp(vec(-0.5, -10.0, 10.0), -1.0, 1.0) == vec(-0.5, -1.0, 1.0)
    assert floor(vec(1.0, 2.4, 3.9)) == vec(1.0, 2.0, 3.0)
    assert fract(vec(1.0, 2.5, 3.75)) == vec(0.0, 0.5, 0.75)
    assert close(distance(vec(1.0, 2.0), vec(3.0, 4.0)), 2.8284)

    # Test elements
    foo = vec(1.0, 2.0, 3.0, 4.0)
    assert foo.elements("xx") == vec(1.0, 1.0)
    assert foo.elements("yx") == vec(2.0, 1.0)
    assert foo.elements("zzyx") == vec(3.0, 3.0, 2.0, 1.0)
    assert foo.elements("xwxx") == vec(1.0, 4.0, 1.0, 1.0)
    assert foo.elements("y") == 2.0

    # Test the sugar interface to elements
    foo = vec(1.0, 2.0, 3.0, 4.0)
    assert foo.xx == vec(1.0, 1.0)
    assert foo.yx == vec(2.0, 1.0)
    assert foo.zzyx == vec(3.0, 3.0, 2.0, 1.0)
    assert foo.xwxx == vec(1.0, 4.0, 1.0, 1.0)
    assert foo.y == 2.0

    print("All passed")