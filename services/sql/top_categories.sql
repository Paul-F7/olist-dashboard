SELECT 
    COALESCE(t.product_category_name_english, 'Unknown') as category,
    COUNT(*) as sales,
    SUM(oi.price) as revenue
FROM order_items oi
JOIN products p ON oi.product_id = p.product_id
LEFT JOIN category_translation t 
    ON p.product_category_name = t.product_category_name
GROUP BY category
ORDER BY revenue DESC
LIMIT 10;