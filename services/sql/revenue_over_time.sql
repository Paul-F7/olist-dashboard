SELECT
    DATE(o.order_purchase_timestamp) as date,
    SUM(oi.price) as revenue,
    COUNT(DISTINCT o.order_id) as orders
    
FROM order as oi
JOIN order_items as oi ON o.order_id = oi.order_id
WHERE o.order_stats = 'delivered'
GROUP BY date
ORDER BY date;