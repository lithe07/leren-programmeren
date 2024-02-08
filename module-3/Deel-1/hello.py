def herhaalde_aanroep(num):
    zin = ''
    for  i in range(1, num + 1):
        zin += f"Hallo from function towen {i}!\n"
    return zin 


zebi = herhaalde_aanroep(69)
print(zebi)