from src.Pizza import Pizza as pizza


def allPizza():
    try:
        file = open('PizzaList.txt', 'r')
    except FileNotFoundError:
        print('ERROR! File not found!')
    else:
        pizzaTypes = dict()
        i = 1
        for line in file:
            listLine = line.split(' ')
            name = listLine[0]
            toppings = [listLine[1], listLine[2], listLine[3]]
            size = [listLine[4], listLine[5], listLine[6]]
            price = {'S': float(listLine[7]),
                     'M': float(listLine[8]),
                     'L': float(listLine[9].rstrip('\n'))}
            pizzaTypes[i] = pizza(name, toppings, 0, size, price)
            i += 1

        file.close()

        return pizzaTypes
