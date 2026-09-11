SELECT DISTINCT customers.customer_id, customers.customer_name FROM customers
LEFT JOIN orders
ON customers.customer_id=orders.customer_id
WHERE orders.customer_id IN (
    SELECT orders.customer_id FROM orders
    WHERE product_name='A'
)
AND orders.customer_id IN (
    SELECT orders.customer_id FROM orders 
    WHERE product_name='B'
)
AND orders.customer_id NOT IN (
    SELECT orders.customer_id FROM orders
    WHERE product_name='C'
)
ORDER BY customer_name;