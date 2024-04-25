import random, string

hf = random.randint(2, 6)
nummers = random.randint(4, 7)
special_characters = '@#$%&_?'
kl = 24 - hf - nummers - 3

random_hf = ''.join(random.choice(string.ascii_uppercase) for _ in range(hf))
random_kl = ''.join(random.choice(string.ascii_lowercase) for _ in range(kl))
random_characters = ''.join(random.choice(special_characters) for _ in range(3))
random_nummers = ''.join(random.choice('0123456789') for _ in range(nummers))

ww = random_hf + random_kl + random_characters + random_nummers
print(ww)



