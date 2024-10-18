-- Query 1: Retrieve Top 5 Customers by Quantity of Books Purchased
SELECT c.customer_id, c.name, SUM(od.quantity) AS total_books
FROM Customers c
JOIN Orders o ON c.customer_id = o.customer_id
JOIN OrderDetails od ON o.order_id = od.order_id
WHERE o.order_date >= DATE_SUB(CURDATE(), INTERVAL 1 YEAR)
GROUP BY c.customer_id
ORDER BY total_books DESC
LIMIT 5;

-- Query 2: Calculate Total Revenue from Book Sales by Author
SELECT b.author, SUM(od.quantity * b.price) AS total_revenue
FROM Books b
JOIN OrderDetails od ON b.book_id = od.book_id
GROUP BY b.author;

-- Query 3: Retrieve Books Ordered More Than 10 Times
SELECT b.title, SUM(od.quantity) AS total_ordered
FROM Books b
JOIN OrderDetails od ON b.book_id = od.book_id
GROUP BY b.book_id
HAVING total_ordered > 10;
