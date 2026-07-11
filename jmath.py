"""
J-MATH Core Library
A computational implementation of the non-Archimedean J-MATH Framework.

This library defines the 2D finite-infinite operational plane, treating
infinities and infinitesimals not as limits, but as algebraic coordinates.
It strictly follows the axioms of J-Numbers (a + bJ) and the Universal 
Golden Formula (UGF) for function, sequence, and series evaluation.

Author: AishDhillon008
"""

class JNum:
    """
    Represents a J-Number in the form: a + bJ
    Where 'a' is the finite real part, and 'bJ' is the infinite/infinitesimal part.
    """
    def __init__(self, a, b=0):
        self.a = float(a)
        self.b = float(b)

    def __str__(self):
        """String representation maintaining J-MATH notation."""
        if self.b == 0:
            return f"{self.a}"
        if self.a == 0:
            return f"{self.b}J" if self.b != 1 else "J"
        
        sign = "+" if self.b >= 0 else "-"
        b_val = abs(self.b) if abs(self.b) != 1 else ""
        return f"{self.a} {sign} {b_val}J"

    def __repr__(self):
        return f"JNum({self.a}, {self.b})"

    def __eq__(self, other):
        """Equality definition based on origin/history preservation."""
        if isinstance(other, (int, float)):
            other = JNum(other, 0)
        return self.a == other.a and self.b == other.b

    def __add__(self, other):
        """
        Addition Axiom: Component-wise addition.
        (a + bJ) + (c + dJ) = (a + c) + (b + d)J
        """
        if isinstance(other, (int, float)):
            other = JNum(other, 0)
        return JNum(self.a + other.a, self.b + other.b)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            other = JNum(other, 0)
        return JNum(self.a - other.a, self.b - other.b)

    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            other = JNum(other, 0)
        return JNum(other.a - self.a, other.b - self.b)

    def __mul__(self, other):
        """
        Multiplication Axiom: Piecewise conditions.
        Handles the Absolute Zero reduction properties.
        """
        if isinstance(other, (int, float)):
            other = JNum(other, 0)

        # Condition 1: If y = 0 + 0J (Absolute Zero) -> Yields b
        if other.a == 0 and other.b == 0:
            return JNum(self.b, 0)
            
        # Condition 2: If x = 0 + 0J (Absolute Zero) -> Yields d
        elif self.a == 0 and self.b == 0:
            return JNum(other.b, 0)
            
        # Condition 3: Standard J-plane multiplication expansion
        else:
            new_a = self.a * other.a
            new_b = (self.a * other.b) + (self.b * other.a) + (self.b * other.b)
            return JNum(new_a, new_b)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __pow__(self, power):
        """
        Exponential Axiom for Pure Infinity (J).
        J^n = J (for n > 0)
        J^0 = 1
        J^n = 0 (for n < 0)
        """
        # Handling Pure J (0 + 1J) logic
        if self.a == 0 and self.b == 1:
            if power > 0:
                return JNum(0, 1)   # J
            elif power == 0:
                return JNum(1, 0)   # 1
            elif power < 0:
                return JNum(0, 0)   # 0
                
        # For generalized numbers, evaluate iteratively (for positive integers)
        if isinstance(power, int) and power > 0:
            result = JNum(1, 0)
            for _ in range(power):
                result = result * self
            return result
            
        raise NotImplementedError("Fractional/Complex J-powers require further topological expansion.")


# ==========================================
# J-MATH FRAMEWORK CONSTANTS
# ==========================================

ABSOLUTE_ZERO = JNum(0, 0)
ABSOLUTE_INFINITY = JNum(0, 1)
J = ABSOLUTE_INFINITY  # Standard shorthand


# ==========================================
# UNIVERSAL GOLDEN FORMULA (UGF) ENGINES
# ==========================================

def evaluate_function(f_0, f_1):
    """
    Evaluates a standard function F(x) at infinity using the UGF.
    F(J) = F(0) + [F(1) - F(0)]J
    """
    change = f_1 - f_0
    return JNum(f_0, change)

def evaluate_sequence(a_0, a_1):
    """
    Evaluates the infinite-th term of a sequence a_n.
    a_J = a_0 + (a_1 - a_0)J
    """
    change = a_1 - a_0
    return JNum(a_0, change)

def evaluate_series(a_0, a_1):
    """
    Evaluates the infinite sum of a series S_n = sum(a_k).
    S_J = a_0 + a_1*J
    """
    return JNum(a_0, a_1)
