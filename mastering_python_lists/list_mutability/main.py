# Initial travel wishlist with nested lists
travel_wishlist = [
    ["Paris", "France", 2000],
    ["Tokyo", "Japan", 3000],
    ["New York", "USA", 2500]
]

# Applying a 20% discount to the estimated cost
travel_wishlist[0][2] = int(2000 * 0.8)
travel_wishlist[1][2] = int(3000 * 0.8)
travel_wishlist[2][2] = int(2500 * 0.8)

# Printing the updated travel_wishlist to verify the change
print('Updated list:', travel_wishlist)