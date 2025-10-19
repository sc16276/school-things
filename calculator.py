def add (x, y): return x + y
def subtraxt(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else 'Error: Division by zero' 

def get_numer(prompt):
    while True:
      try:
         return float(input(prompt))
       execpt ValueError:
          print('Please enter a valid number.')
