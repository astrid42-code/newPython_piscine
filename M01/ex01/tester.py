from array2D import slice_me

family = [[1.80, 78.4],
            [2.15, 102.7],
            [2.10, 98.5],
            [1.88, 75.2]]

print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))


# Expected output:
# $> python test_array2D.py
# My shape is : (4, 2)
# My new shape is : (2, 2)
# [[1.8, 78.4], [2.15, 102.7]]
# My shape is : (4, 2)
# My new shape is : (1, 2)
# [[2.15, 102.7]] > depart de la position 1 arret a la position -2 en partant de la fin, sans le prendre en compte (donc position 1)