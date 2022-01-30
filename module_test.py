# Public method from module_test.py

def func(args):
    """Returns the doubled input value."""
    return 2*args

# This only happens when module_test.py is called directly (Run/Debug in editor):
# So you can write tests here
if __name__ == "__main__":
    arg = 42
    double_arg = func(arg)
    print(f"Evaluating func({arg}) as a test while running this file:", double_arg)