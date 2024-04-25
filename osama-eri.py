def round_quarter(amount):
    if amount > 10:
        return round(amount)    
    else:
        remainder = amount % 0.25
        if remainder < 0.125:
            return amount - remainder
        else:
            return amount + (0.25 - remainder)
# Voorbeeldgebruik:
print(round_quarter(1.90))  # Output: 9.75
print(round_quarter(11.89)) # Output: 12
