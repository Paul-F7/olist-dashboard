SELECT 
    customer_state,
    customer_city,
    COUNT(DISTINCT c.customer_id) as customers,
    COUNT(o.order_id) as orders
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY customer_state, customer_city
ORDER BY customers DESC;