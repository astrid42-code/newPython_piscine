from ft_calculator import calculator

a = [5, 10, 2]
b = [2, 4, 3]
calculator.dotproduct(a, b)
calculator.add_vec(a, b)
calculator.sous_vec(a, b)

# Expected output:
#  python tester.py
# Dot product is: 56
# > addition of products of the list elements : 5*2 + 4*10 + 2*3 = 56
# Add Vector is : [7.0, 14.0, 5.0]
# Sous Vector is: [3.0, 6.0, -1.0]
