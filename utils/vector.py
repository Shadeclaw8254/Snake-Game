from __future__ import annotations

class Vector:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __add__(self, other) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)
    
    def __neg__(self) -> Vector:
        return Vector(-self.x, -self.y)
    
    def __mul__(self, other) -> Vector:
        if type(other) == Vector:
            return Vector(self.x * other.x, self.y * other.y)
        
        elif type(other) in (int, float):
            return Vector(self.x * other, self.y * other)
        
        else:
            raise ValueError(f"Vector cannot be multiplied by {type(other)}")
    
    def __truediv__(self, other) -> Vector:
        if type(other) == Vector:
            return Vector(self.x / other.x, self.y / other.y)
        
        elif type(other) in (int, float):
            return Vector(self.x / other, self.y / other)
        
        else:
            raise ValueError(f"Vector cannot be divided by {type(other)}")
    
    def __divmod__(self, other) -> Vector:
        if type(other) == Vector:
            return Vector(self.x % other.x, self.y % other.y)
        
        elif type(other) in (int, float):
            return Vector(self.x % other, self.y % other)
        
        else:
            raise ValueError(f"Vector cannot be divided by {type(other)}")
    
    def __floordiv__(self, other) -> Vector:
        if type(other) == Vector:
            return Vector(self.x // other.x, self.y // other.y)
        
        elif type(other) in (int, float):
            return Vector(self.x // other, self.y // other)
        
        else:
            raise ValueError(f"Vector cannot be divided by by {type(other)}")
    
    def __abs__(self) -> Vector:
        return Vector(abs(self.x), abs(self.y))
    
    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"
    
    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y
    
    def __ne__(self, other) -> bool:
        return self.x != other.x or self.y != other.y
