CREATE VIEW top_products AS

WITH sales_category AS (

    SELECT
        CAST(sa.ean AS VARCHAR) AS ean,
        sa.price AS price,
        st.produto AS produto
    FROM
        sales AS sa
    INNER JOIN store AS st ON CAST(st.ean AS VARCHAR) = sa.ean

)

SELECT
    produto,
    ROUND(SUM(price), 2) AS price_total,
    COUNT(*) AS sales_total
FROM
    sales_category
GROUP BY
    1
ORDER BY
    3 DESC
LIMIT 5;