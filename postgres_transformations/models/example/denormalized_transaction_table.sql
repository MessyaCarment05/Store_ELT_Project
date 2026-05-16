SELECT
    ti.item_id AS item_id,
    ti.transaction_date  AS transaction_date,
    c.customer_id AS customer_id,
    c.name AS customer_name,
    c.email AS customer_email,
    c.city AS customer_city,
    p.product_id AS product_id,
    p.product_name AS product_name,
    p.price AS product_price,
    p.stock AS product_stock,
    ti.quantity AS quantity,
    (ti.quantity * p.price) AS total_price
FROM
    {{ref('transaction_items')}} ti JOIN {{ref('customers')}} c 
    ON ti.customer_id=c.customer_id JOIN
    {{ref('products')}} p 
    ON ti.product_id = p.product_id
ORDER BY
    ti.transaction_date, ti.item_id