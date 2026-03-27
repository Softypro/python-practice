# ===== INTERMEDIATE FUNCTION CONCEPTS =====

# 1. DECORATORS - Functions that modify other functions
# =====================================================
def repeat(times):
    """Decorator that repeats function execution"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for _ in range(times):
                result = func(*args, **kwargs)
                results.append(result)
            return results
        return wrapper
    return decorator

@repeat(times=3)
def greet(name):
    return f"Hello, {name}!"

# Test it:
# print(greet("Alice"))  # Returns ['Hello, Alice!', 'Hello, Alice!', 'Hello, Alice!']


# 2. CLOSURES - Inner functions that capture outer scope
# ========================================================
def make_multiplier(factor):
    """Returns a function that multiplies by factor"""
    def multiplier(x):
        return x * factor
    return multiplier

double = make_multiplier(2)
triple = make_multiplier(3)

# Test it:
# print(double(5))  # 10
# print(triple(5))  # 15


# 3. HIGHER-ORDER FUNCTIONS - Functions that take/return functions
# ==================================================================
def apply_operation(func, a, b):
    """Takes a function and applies it to two numbers"""
    return func(a, b)

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

# Test it:
# print(apply_operation(add, 3, 4))        # 7
# print(apply_operation(multiply, 3, 4))   # 12


# 4. *args and **kwargs - Variable-length arguments
# ===================================================
def flexible_function(*args, **kwargs):
    """Accepts any number of positional and keyword arguments"""
    print(f"Args (positional): {args}")
    print(f"Kwargs (keyword): {kwargs}")
    
    # Sum all positional arguments
    total = sum(args) if args else 0
    return total

# Test it:
# print(flexible_function(1, 2, 3, 4, name="Bob", age=30))
# Args: (1, 2, 3, 4)
# Kwargs: {'name': 'Bob', 'age': 30}
# Returns: 10


# 5. TYPE HINTS - Document parameter and return types
# =====================================================
def calculate_discount(price: float, discount_percent: int) -> float:
    """
    Calculate the final price after discount.
    
    Args:
        price: Original price (float)
        discount_percent: Discount percentage (int)
    
    Returns:
        Final price after discount (float)
    """
    return price * (1 - discount_percent / 100)

# Test it:
# print(calculate_discount(100, 20))  # 80.0


# 6. LAMBDAS - Anonymous inline functions
# =========================================
numbers = [1, 2, 3, 4, 5]

# Square each number
squared = list(map(lambda x: x ** 2, numbers))
# print(squared)  # [1, 4, 9, 16, 25]

# Filter even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
# print(evens)  # [2, 4]


# 7. FUNCTION COMPOSITION - Combine multiple functions
# ======================================================
def compose(f, g):
    """Combines two functions: returns f(g(x))"""
    return lambda x: f(g(x))

def add_five(x):
    return x + 5

def multiply_by_two(x):
    return x * 2

# Compose: multiply by 2, then add 5
operation = compose(add_five, multiply_by_two)
# print(operation(3))  # (3 * 2) + 5 = 11


# ===== TRY THESE OUT =====
if __name__ == "__main__":
    print("=== Decorator ===")
    print(greet("Bob"))
    
    print("\n=== Closures ===")
    print(f"double(5) = {double(5)}")
    print(f"triple(5) = {triple(5)}")
    
    print("\n=== Higher-Order Functions ===")
    print(f"add(3, 4) = {apply_operation(add, 3, 4)}")
    print(f"multiply(3, 4) = {apply_operation(multiply, 3, 4)}")
    
    print("\n=== *args and **kwargs ===")
    flexible_function(1, 2, 3, name="Alice", score=95)
    
    print("\n=== Type Hints ===")
    print(f"$100 with 20% off = ${calculate_discount(100, 20)}")
    
    print("\n=== Lambdas ===")
    print(f"Squared: {squared}")
    print(f"Evens: {evens}")
    
    print("\n=== Function Composition ===")
    print(f"operation(3) = {operation(3)}")
