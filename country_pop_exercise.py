##########################################################
#                   Country Population                   #
########################################################## 

d = {'China': 143, 'India': 136, 'USA': 32, 'Pakistan': 21}

def print_country():
    for k, v in d.items():
        print(f'{k}==>{v}')

def add_country(country):
    if country not in d:
        population = int(input(f'Please enter population for {country}\n'))
        d[country] = population
        print(f'{country} added')
    else:
        print(f'{country} already exists')
        
def remove_country(country):
    if country in d:
        del d[country]
        print(f'{country} removed')
    else:
        print(f'{country} does not exist')
        
def query_country(country):
    if country in d:
        print(f'{country} population is {d[country]}')
    else:
        print(f'{country} does not exist')
        
command = input("Please enter any for this commands 'print, add, remove, query'\n")
command = command.lower()

if command == 'print':
    print_country()
elif command == 'add':
    country = input("Please enter country name\n")
    add_country(country)
elif command == 'remove':
    country = input("Please enter country name\n")
    remove_country(country)
elif command == 'query':
    country = input("Please enter country name\n")
    query_country(country)
else:
    print("Invalid command")