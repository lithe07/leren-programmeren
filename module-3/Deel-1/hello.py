def get_function_town_string(num):
    result = ""
    for i in range(1, num + 1):
        result += f"Hello from function town {i}!\n"
    return result


result_3 = get_function_town_string(3)
result_7 = get_function_town_string(7)

print(result_3)
print(result_7)
