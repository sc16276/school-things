def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return x / y if y != 0 else 'Error: Division by zero'
def power(x, y): return x ** y

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print('Anna kelvollinen numero.')

def main():
    print('Yksinkertainen laskin')
    print('1) Yhteenlasku  2) Vähennyslasku  3) Kertolasku  4) Jakolasku  5) Potenssi  0) Lopeta')
    while True:
        choice = input('Valitse (1/2/3/4/5 tai 0): ').strip()
        if choice == '0':
            print('Heippa!')
            break
        if choice not in {'1','2','3','4','5'}:
            print('Virheellinen valinta.')
            continue
        x = get_number('Ensimmäinen numero: ')
        y = get_number('Toinen numero: ')
        if choice == '1':
            print('Tulos:', add(x, y))
        elif choice == '2':
            print('Tulos:', subtract(x, y))
        elif choice == '3':
            print('Tulos:', multiply(x, y))
        elif choice == '4':
            print('Tulos:', divide(x, y))
        elif choice == '5':
            print('Tulos:', power(x, y))

if __name__ == '__main__':
    main()
