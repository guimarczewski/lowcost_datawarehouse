SELECT * FROM sales_per_category;
COPY sales_per_category TO 'analytics/result_query/sales_per_category.csv' WITH CSV HEADER DELIMITER ',';

SELECT * FROM top_products;
COPY top_products TO 'analytics/result_query/top_products.csv' WITH CSV HEADER DELIMITER ',';


SELECT * FROM store;

.mode markdown
.output analytics/result_query/store.md