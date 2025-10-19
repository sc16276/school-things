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

def main():
   print('Simple Calculator')
   print('1) Add 2) Subtract 3) Multpily 4) Divide 0) Exit')
 while True:
     choice = input('Choose (1/2/3/4 or 0): ').strip()
     if choice == '0':
       print(' Bye!' ); break
     if choice not in {'1', '2', '3', '4'}:
        print('Invalid choice.'); continue
     x = get_number('First number: ')
     y = get_number('Second number: ')
     if choice == '1': print('Result:', add(x, y))
     elif choice == '2': print('Result:', subtract(x, y))
     elif choice == '3': print('Result:', multiply(x, y))
     elif choice == '4': print ('Result:', divide (x, y))

if_name__ == '__main__':
 main ()
