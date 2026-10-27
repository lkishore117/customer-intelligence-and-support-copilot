-- Q1 — WHERE then HAVING
SELECT customer_id, SUM(order_amount) AS total_spend
FROM orders
WHERE status = 'completed' AND order_amount > 500
GROUP BY customer_id
HAVING SUM(order_amount) > 8000;

-- Q2 — Three-Table Join
SELECT c.city, p.category, SUM(o.order_amount) AS revenue, o.order_amount
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
JOIN products p ON o.product_id = p.product_id
WHERE o.status = 'completed'
GROUP BY c.city, p.category;

-- Q3 — Scalar Subquery
SELECT *
FROM products
WHERE price_inr > (SELECT AVG(price_inr) FROM products);

-- Q4 — LEFT JOIN
SELECT c.customer_id
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id AND o.status = 'completed'
WHERE o.order_id IS NULL;

-- Q5 — Common Table Expressions (CTEs)
WITH customer_spend AS (
    SELECT customer_id, SUM(order_amount) AS total_spend
    FROM orders
    WHERE status = 'completed'
    GROUP BY customer_id
),
avg_spend AS (
    SELECT AVG(total_spend) AS avg_total FROM customer_spend
)
SELECT cs.customer_id, cs.total_spend
FROM customer_spend cs, avg_spend
WHERE cs.total_spend > avg_spend.avg_total;

-- Q6 — Ranking Window Functions
WITH customer_totals AS (
    SELECT o.customer_id, c.city, SUM(o.order_amount) AS total_spend
    FROM orders o
    JOIN customers c ON o.customer_id = c.customer_id
    WHERE o.status = 'completed'
    GROUP BY o.customer_id, c.city
)
SELECT customer_id, city, total_spend,
       RANK() OVER (PARTITION BY city ORDER BY total_spend DESC) AS rnk,
       DENSE_RANK() OVER (PARTITION BY city ORDER BY total_spend DESC) AS dense_rnk,
       ROW_NUMBER() OVER (PARTITION BY city ORDER BY total_spend DESC) AS row_num
FROM customer_totals;

-- Q7 — Running Total
WITH daily_revenue AS (
    SELECT SUBSTR(order_ts, 1, 10) AS day, SUM(order_amount) AS revenue
    FROM orders
    WHERE status = 'completed'
    GROUP BY day
)
SELECT day, revenue,
       SUM(revenue) OVER (ORDER BY day ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS cumulative_revenue
FROM daily_revenue;
