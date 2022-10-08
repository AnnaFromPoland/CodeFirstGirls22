USE BookStore;

SELECT DISTINCT author_name, a.book_name, b.book_name, sold_copies
FROM Authors AS a
LEFT JOIN Books AS b
ON b.book_name = a.book_name
ORDER by b.sold_copies DESC LIMIT 3