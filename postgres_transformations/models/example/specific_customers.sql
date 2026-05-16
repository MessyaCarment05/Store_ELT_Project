SELECT 
    *
FROM
    {{ref('customers')}} c
WHERE
    c.name LIKE 'Rina'
