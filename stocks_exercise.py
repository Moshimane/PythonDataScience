d = { 'info': [600,630,620], 'ril': [1430,1490,1567],
     'mtl': [234,180,160]}

def calculate_average(ls):
    return round(sum(ls) / len(ls),2)

def print_stocks():
    for k, v in d.items():
        print(f'{k} ==> {v} ==> {calculate_average(v)}')
        
def add_stock(stock):
    if stock[0] not in d:
        d[stock[0]] = [stock[1]]
        print(f'{stock[0]} has been added')
    else:
        d[stock[0]].append(stock[1])
        print(f'{stock[0]} has been updated with {stock[1]}')

command = input("Please enter one of the following commands 'print, add': \n")
command = command.lower()

if command == 'print':
    print_stocks()
elif command == 'add':
    stock = input("Please enter stock name and price\n")
    stock1 = stock.split(',')
    add_stock((stock1[0],int(stock1[1]))) 