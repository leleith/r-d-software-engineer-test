# Section 1: Python and Data Structures

### Question 1
Run the code using this command:  
- Windows `py section-1/question-1/binary_search.py -l <list> -v <value_to_search>`.  
Example 1: `py section-1/question-1/binary_search.py -l 2,3,5,8,13,21 -v 8`  
Example 2: `py section-1/question-1/binary_search.py -l 3,4,1,5 -v 8,4,3`

- Unix (Mac/Linux) `python3 section-1/question-1/binary_search.py -l <list> -v <value_to_search>`.  
Example 1: `python3 section-1/question-1/binary_search.py -l 2,3,5,8,13,21 -v 8`  
Example 2: `python3 section-1/question-1/binary_search.py -l 3,4,1,5 -v 8,4,3`

### Question 2
Run the code using this command:
- Windows `py section-1/question-2/matrices_multiplication.py`  

- Unix (Mac/Linux) `python3 section-1/question-2/matrices_multiplication.py`  

---

# Section 2: SQL and BigQuery

### Question 1
You can verify the query in this file: `section-2/question-1/top_five_clients.sql`

### Question 2
*Partitioning* divides the table into smaller tables, based on a column, usually a date, timestamp or id column. *Clustering* organizes, sort the data into pieces.

```
-- Example of a partitioned and clustered table for sales data

-- Create a partitioned table by date
CREATE TABLE sales_data_partitioned
PARTITION BY DATE(sale_date)
CLUSTER BY product_category, region
AS (
  SELECT 
    sale_date,
    product_category,
    region,
    total_sales,
    num_transactions
  FROM sales_raw_data
);

-- Query example showing benefits of partitioning and clustering
SELECT 
  product_category, 
  SUM(total_sales) as total_revenue
FROM sales_data_partitioned
WHERE sale_date BETWEEN '2023-01-01' AND '2023-01-31'
  AND region = 'Northeast'
  AND product_category = 'Electronics'
GROUP BY product_category;
```

---

# Section 3: AWS and Containerization

### Question 1
I would develop the Python code and then put inside a Lambda, the main lambda function is usually called lambda_handler (in this case, the function must return a JSON-like text). For the dependencies, I can create a `requirements.txt` inside the project folder. Then I build a zip file, based on a virtual enviroment folder (where I installed the dependencies and contains the lambda function file). After that, I push the package to AWS and set the json file for the API Gateway. All the process can be made inside the AWS console or using AWS CLI.

### Question 2
To run the python app (with numpy and pandas - numpy already comes with pandas):

- build the image using `docker build -t my-python-app -f section-3/question-2/Dockerfile.yml .`

- take the `image_id` using `docker images`

- creating the container `docker run <image_id>`

---

# Section 4: ETL and Multithreading

### Question 1
1 - Some years ago I was working with Pentaho Data Integration. Most clients we (the team) had to connect directly with their databases. So the extraction part was pulling data from the databases, then we transform them (using Pentaho) and then using an API Post method we sent to the company database, in AWS.

2 - Another ETL process I can tell you is one entirely based on AWS: extracting data using DMS, using Lambda or Glue (it depended of the amount) to transform the data and loading into S3

### Question 2
Run the code using this command:  
- Windows `py section-4/question-2/multithreading.py`  

- Unix (Mac/Linux) `python3 section-4/question-2/multithreading.py`  

---

# Section 5: CI/CD and DevOps

### Question 1
A CI/CD pipeline automates tests and builds - when a developer push some code to a repository, this triggers the tests and merge the code if the code is ok. As I said, I do not have experience with Jenkins but it may let the process of configuration easier and help with monitoring, sending Slack messages (for example).

### Question 2
Git mantains a history of changes, prevent more than one person edit the same code track, facilitates the team work by enabling multiple team people work on the same codebase, helps revert errors that were commited, keeps a central codebase.
