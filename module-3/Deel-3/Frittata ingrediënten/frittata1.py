from recipe_lib import *
from frittata_ingredients import *

# -------- TITLE --------
print('=============== Frittata recept ===============')
# -------- INPUT --------
nr_persons = input_nr_persons("Voor hoeveel mensen wil je het recept maken? ")

# ----- CALCULATIONS ----
# calculate factor 

# calculate amount_eggs

# calculate amount_milk

# calculate amount_salt

# calculate amount_pepper

# calculate amount_oil

# calculate amount_onions

# calculate amount_garlics

# calculate amount_spinach

# calculate amount_paprikas

# calculate amount_cheese


# -------- OUTPUT -------
print('=============== Frittata recept ===============')
print(f'Ingrediënten voor {nr_persons} personen:')
print('-----------------------------------------------')
# print (formatted) all amounts and units combined with their ingrediënt descriptions
print(f"* {TXT_EGGS}")
# calculate amount_milk
print(f'* {UNIT_CUPS} {TXT_MILK}')
# calculate amount_salt
print(f"* {UNIT_TEASPOONS} {TXT_SALT}")
# calculate amount_pepper
print(f"* {UNIT_TEASPOONS} {TXT_PEPPER}")
# calculate amount_oil
print(f"* {UNIT_SPOONS} {TXT_OIL}")
# calculate amount_onions
print(f'* {TXT_ONIONS}')
# calculate amount_garlics
print(f'* {TXT_GARLICS}')
# calculate amount_spinach
print(f'* {UNIT_CUPS} {TXT_SPINACH}')
# calculate amount_paprikas
print(f'* {TXT_PAPRIKAS}')
# calculate amount_cheese
print(f"* {TXT_CUPS} {TXT_CHEESE}")
print('-----------------------------------------------')