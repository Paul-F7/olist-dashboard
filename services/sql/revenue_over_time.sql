SELECT
    DATE(o.order_purchase_timestamp) as date,
    SUM(oi.price) as revenue,
    COUNT(DISTINCT o.order_id) as orders

FROM orders as o
JOIN order_items as oi ON o.order_id = oi.order_id
WHERE o.order_status = 'delivered'
GROUP BY date
ORDER BY date;