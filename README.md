# Building a Low Cost Data Warehouse

The objective of this project is to extract data from three different sources (API, 2 Postgres Databases, and CSV files) and load this data into Parquet format on AWS s3 after validating data contracts using Pydantic.

To achieve this, three Collectors were created, along with a Data App using Streamlit for uploading and verifying CSV files.

Additionally, some Ad-Hoc queries were performed using DuckDB, demonstrating the ease of accessing data directly from S3 and transforming it using SQL. DuckDB’s in-memory nature contributes to its exceptional speed.

![Arch](https://github.com/guimarczewski/lowcost_datawarehouse/blob/main/img/architecture.png?raw=true)

## Project Structure

- Analytics: Creation of tables from Parquet files in S3 using DuckDB.
- Backend: Script for fetching data from the API and the database, along with Collectors and Contracts.
- Frontend: Data App using Streamlit to upload CSV files to S3.

## Cloud Cost

To deploy this project using AWS - working with Parquet files of up to 200 columns and 66 million rows, totaling approximately 7.5GB each time - we would need an EC2 instance with 8GB of memory and optimized for memory usage, along with S3 for storing the Parquet files.

This setup would have an estimated cost of approximately $30 per month.
![Pricing](https://github.com/guimarczewski/lowcost_datawarehouse/blob/main/img/pricing.png?raw=true)
https://calculator.aws/#/estimate?id=41c95c0df4643b357a19dafb8d7b492aa04fe004