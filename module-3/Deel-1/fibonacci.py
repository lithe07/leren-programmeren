def fibonacci(n):
    """ Bereken de Fibonacci-reeks tot het n-de getal en retourneer de reeks."""
    fib_sequence = [0, 1]  # Initialisatie van de Fibonacci-reeks met de eerste twee getallen

    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])  # Voeg het volgende Fibonacci-getal toe aan de reeks

    return fib_sequence

def golden_ratio(fib_sequence):
    """ Bereken de gulden snede op basis van de laatste twee getallen uit de Fibonacci-reeks."""
    if len(fib_sequence) >= 2:
        last_two_numbers = fib_sequence[-2:]  # Selecteer de laatste twee getallen uit de Fibonacci-reeks
        golden_ratio = last_two_numbers[-1] / last_two_numbers[-2]  # Bereken de gulden snede
        return golden_ratio
    else:
        return "Fibonacci-reeks heeft niet genoeg getallen voor het berekenen van de gulden snede."

# Vraag de gebruiker om het aantal getallen in de Fibonacci-reeks in te voeren
n = int(input("Voer het aantal getallen in de Fibonacci-reeks in: "))

# Bereken de Fibonacci-reeks
fib_seq = fibonacci(n)

# Toon de Fibonacci-reeks
print("De Fibonacci-reeks:")
print(fib_seq)

# Bereken en toon de gulden snede
golden_ratio_value = golden_ratio(fib_seq)
print("De gulden snede op basis van de laatste twee getallen uit de Fibonacci-reeks is:", golden_ratio_value)
