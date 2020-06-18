# Using Python code to scrape data from [Books to Scrape] and then save it to a SQL database.

import sqlite3, bs4, requests

def scrapeBooks(productUrl):
	res = requests.get(productUrl) # Request to download the page
	res.raise_for_status() # Raise an Exception if there is an issue.
	soup = bs4.BeautifulSoup(res.text, 'html.parser') # Passed html.parser to dismiss the warning.
	books = soup.find_all('article') # This will return all of the articles.
	allBooks = [] # Create a list.
	for book in books: # For each article that comes back, we're calling a book.
		bookData = (getTitle(book), getPrice(book), getRating(book)) # Compile 3 pieces of data as a tuple.
		allBooks.append(bookData) # Append the data into our list, allBooks.
	saveBooks(allBooks) # Pass the list into saveBooks.

# Save data to SQL database.
def saveBooks(allBooks):
	connection = sqlite3.connect('books.db') # Connect to the database.
	c = connection.cursor() # Create a new cursor.
	c.execute('''CREATE TABLE books -- Comment this line out after creating the table.
		(title TEXT, price REAL, rating INTEGER)''') # Comment this line out after creating the table.
	c.executemany('INSERT INTO books VALUES (?, ?, ?)', allBooks) # Insert into books.
	connection.commit()
	connection.close()

def getTitle(book):
	return book.find('h3').find('a')['title'] # In the markup, there is an <h3> with an anchor tag inside.

def getPrice(book):
	price = book.select('.price_color')[0].get_text() # Class price_color contains the inner-text, price.
	return float(price.replace('£', '').replace('Â', '')) # Store in SQL db as a number, without currency.

def getRating(book):
	ratings = {'Zero': 0, 'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5} # Dict to get int.
	paragraph = book.select('.star-rating')[0] # Selecting class with star rating.
	word = paragraph.get_attribute_list('class')[1] # We want the second item.
	return ratings[word]

scrapeBooks('http://books.toscrape.com/catalogue/category/books/history_32/index.html')
