def fibonacci(getal): 
    getallen_lijst = [0, 1]
    for i in range(2, aantal):
        volgende_getal = getallen_lijst[-1] + getallen_lijst[-2]
        getallen_lijst.append(volgende_getal)
    return getallen_lijst

aantal = 10
fibonacci_uitkomst = fibonacci(aantal)
print(fibonacci_uitkomst)

