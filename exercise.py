import modules

value = input('Enter number greater than 1')
num = int(value)

def printtriangle(num):
    for i in range(num+1):
        for j in range(i):
            print('*', end="")
        print()
        
def calculate_area(a,b,shape):
    if shape == 'triangle':
        area = (a*b)/2
        print(f'Area of {a}x{b} triangle is {area}')
    elif shape == 'circle':
        area = 3.14*a*a
        print(f'Area of {a}x{a} circle is {area}')
    elif shape =='rectangle':
        area = a*b
        print(f'Area of {a}x{b} rectangle is {area}')
    else:
        print(f'Invalid shape {shape}')
        
printtriangle(num)

num2 = int(input('Enter positive number'))
shape = input('Enter name of shape')

calculate_area(num,num2,shape)

print(modules.factorial_calc(5))