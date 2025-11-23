🚀 Serverless CSV Pipeline – S3 → Lambda → DynamoDB
Flipkart Price Update Use Case | Automated Serverless Data Processing

📌 Project Overview

This project demonstrates a fully serverless, event-driven data pipeline built on AWS.
Whenever a CSV file is uploaded to Amazon S3, it automatically triggers a Lambda function that reads the file and performs:

INSERT

UPDATE

DELETE

operations on a DynamoDB table based on the action column in the CSV.

🔥 Real-World Use Cases

✔ Flipkart product price updates
✔ Inventory synchronization
✔ Bulk catalog import
✔ Automated price corrections
✔ E-commerce product ingestion

🏗️ Architecture Clean Visual Flow

| Flow | AWS Service          | Action                                                     |
| ---- | -------------------- | ---------------------------------------------------------- |
| 📄   | **CSV File**         | Data source uploaded by user                               |
| ⬇️   | **Amazon S3**        | CSV file is uploaded to S3 bucket                          |
| ⚡    | **S3 Event Trigger** | Automatically triggers Lambda on file upload               |
| 🧠   | **AWS Lambda**       | Parses CSV & performs Insert / Update / Delete in DynamoDB |
| 🗄️  | **Amazon DynamoDB**  | Stores updated product records                             |
| 📊   | **CloudWatch Logs**  | Logs processing details, successes, and errors             |

📂 Folder Structure

serverless-csv-pipeline/
│
├── lambda_function.py      # Main Lambda code
├── requirements.txt        # Python dependencies
├── sample.csv              # Example CSV file
└── README.md               # Documentation


🧠 How It Works

1️⃣ Upload CSV to S3

Example CSV:
product_id,name,price,action
101,Redmi Note 12,15999,INSERT
102,Boat Headset,799,INSERT
101,Redmi Note 12,14999,UPDATE
102,Boat Headset,,DELETE

2️⃣ S3 Triggers the Lambda Function

S3 Event Type:

s3:ObjectCreated:*


Lambda receives:

Bucket name
Object key

3️⃣ Lambda Parses the CSV

Lambda checks the action column:

Action	Operation
INSERT	Add a new item
UPDATE	Update existing item
DELETE	Delete item from table

4️⃣ DynamoDB is Updated

Data is written to a table containing fields like:

product_id (Partition Key)

name

price

And others based on CSV columns

5️⃣ CloudWatch Logs

Every row action is logged:

“Inserted: <product_id>”

“Updated: <product_id>”

“Deleted: <product_id>”

Error logs (if any)

💻 Lambda Function Code

(Upload the lambda_function.py provided earlier.)

🔧 Deployment Steps
1️⃣ Create DynamoDB Table

Table Name: FlipkartProducts

Primary Key: product_id (String)

2️⃣ Create an S3 Bucket

Example:

flipkart-product-csv-bucket

3️⃣ Create Lambda Function

Runtime: Python 3.9+

Add environment variable:

DDB_TABLE = FlipkartProducts

4️⃣ Add S3 Trigger

Navigate to:
S3 → Bucket → Properties → Event Notifications

Configure:

Event type: PUT

Prefix: (optional)

Destination: Lambda Function

5️⃣ IAM Permissions

Attach these managed policies to the Lambda execution role:

AmazonS3ReadOnlyAccess
AmazonDynamoDBFullAccess
CloudWatchLogsFullAccess

📊 Sample CloudWatch Output

File received: s3://flipkart-bucket/sample.csv

Inserted: 101

Inserted: 102

Updated: 101

Deleted: 102

CSV processed successfully

🏅 Skills Demonstrated

AWS Lambda

Amazon S3

DynamoDB

IAM

CloudWatch Logs

Python CSV Processing

Serverless Architecture

Event-Driven Workflows
