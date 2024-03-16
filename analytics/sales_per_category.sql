CREATE VIEW sales_per_category AS 

WITH sales_category AS (

    SELECT
        CAST(sa.ean AS VARCHAR) AS ean,
        sa.price AS price,
        st.categoria AS categoria
    FROM
        sales AS sa
    INNER JOIN store AS st ON CAST(st.ean AS VARCHAR) = sa.ean

)

SELECT
    categoria,
    ROUND(SUM(price), 2) AS total
FROM
    sales_category
GROUP BY
    1
ORDER BY
    2 DESC;