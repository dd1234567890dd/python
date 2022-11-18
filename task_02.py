
city = ["Moscow", "Rio", "New York"]
population = [
    ["Moscow", 12.6],
    ["Rio", 6.8],
    ["New York", 8.3]
]
print('население '+ str(population[1][0]) + " - " + str(population[1][1]) + " миллионов человек")

# Хорошо!
# Вот еще варианты

# Решение 1 с функцией
def total_sun(lst):
    total = 0

    for i in lst:
        total += i[1]

    return total

# Решение 2 с функцией в одну строку
def total_sum(lst):
    return sum([i[1] for i in lst])

print(total_sum(population))
