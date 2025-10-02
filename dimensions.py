# TUPLAS: listas imutaveis

dimensions = (200,50)

print(dimensions[0])
print(dimensions[1])

print("Percorrendo a tupla com laço for:")
print("Print original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)

print("Modified dimensions:")
for dimension in dimensions:
    print(dimension)
