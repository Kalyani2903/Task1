def calculateElectronicsGST(a, b):
    return (a + b) * 1.18


def calculateFashionGST(c, d):
    return (c + d) * 1.13


def calculateFoodGST(e):
    return e * 1.07


def totalBill(a, b, c, d, e):
    electronics = calculateElectronicsGST(a, b)
    fashion = calculateFashionGST(c, d)
    food = calculateFoodGST(e)

    return electronics + fashion + food


def calculateDiscountedBill(a, b, c, d, e):
    total = totalBill(a, b, c, d, e)
    discount = total * 0.20

    return total - discount


# Given test values
a = 100
b = 100
c = 100
d = 100
e = 100

# Calculate the bill
electronics = calculateElectronicsGST(a, b)
fashion = calculateFashionGST(c, d)
food = calculateFoodGST(e)

total = totalBill(a, b, c, d, e)
discount = total * 0.20
final_amount = calculateDiscountedBill(a, b, c, d, e)

# Display the output
print("Electronics Amount after GST: {:.2f}".format(electronics))
print("Fashion Amount after GST: {:.2f}".format(fashion))
print("Food Amount after GST: {:.2f}".format(food))
print("Total Bill after GST: {:.2f}".format(total))
print("Discount (20%): {:.2f}".format(discount))
print("Final Payable Amount: {:.2f}".format(final_amount))
