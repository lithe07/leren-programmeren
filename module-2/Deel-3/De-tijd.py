uur = 1

while uur <= 24:
    if uur <= 12:
        print(f'{uur} AM')
    else:
        min_12_uren = uur - 12
        print(f'{min_12_uren} PM')

    uur += 1
