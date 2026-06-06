authors_books = {
    'William Shakespeare': ['Hamlet', 'Macbeth', 'Romeo and Juliet', 'Othello'],
    'J.K. Rowling': ['Harry Potter and the Sorcerer\'s Stone', 'Harry Potter and the Chamber of Secrets', 'Harry Potter and the Prisoner of Azkaban', 'Harry Potter and the Goblet of Fire'],
    'George Orwell': ['1984', 'Animal Farm', 'Coming Up for Air'],
    'Stephen King': ['It', 'The Shining', 'Carrie', 'Misery'],
    'Agatha Christie': ['Murder on the Orient Express', 'The Murder of Roger Ackroyd', 'And Then There Were None', 'Death on the Nile']
}

keys = authors_books.keys()

#all_books = authors_books['William Shakespeare'] +authors_books['J.K. Rowling']+authors_books['George Orwell']+authors_books['Stephen King']+authors_books['Agatha Christie']
all_books =[]
for k in authors_books:
    for book in authors_books[k]:
        all_books.append(book)
print(keys)
# Testing
print("The list of all books in the library:", all_books)