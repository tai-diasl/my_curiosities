"""
At 8 years old, Marcelo is taller than his friend João, who was also 8 years old.
Marcelo is 1.20 tall, while his friend João was 1.05.
But Marcelo grows 0.5/year and João grows 0.7/year.
How old will they be when John becomes taller than Marcelo?
"""

marcelos_height = 1.20
joaos_height = 1.05
marcelos_annual_growth = 0.05
joaos_annual_growth = 0.07
age = 8

while marcelos_height >= joaos_height:
    print(f"At {age} years old:")
    print("Marcelo: {:.2f}".format(marcelos_height))
    print("João: {:.2f}".format(joaos_height))
    print()
    marcelos_height = marcelos_height + marcelos_annual_growth
    joaos_height = joaos_height + joaos_annual_growth
    age = age + 1

print(f"At {age} years old, João will become taller than Marcelo.")
print("Marcelo will be {:.2f} tall.".format(marcelos_height))
print("João will be {:.2f} tall.".format(joaos_height))
