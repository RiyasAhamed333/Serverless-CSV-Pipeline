🚀 Serverless CSV Pipeline – S3 → Lambda → DynamoDB
Flipkart Price Update Use Case | Automated Serverless Data Processing

📌 Project Overview

This project demonstrates a fully serverless, event-driven data pipeline built on AWS.
When a CSV file is uploaded to Amazon S3, it automatically triggers a Lambda function, which reads the data and performs Insert, Update, or Delete operations on a DynamoDB table — based on the action column in the CSV.

This pipeline mirrors real-world use-cases like:

✔ Flipkart product price updates
✔ Inventory synchronization
✔ Bulk catalog imports
✔ Automated price corrections
✔ E-commerce product ingestion

🏗️ Architecture Diagram
      +--------------+
      |   CSV File   |
      | (Flipkart)   |
      +--------------+
             |
             v
     +---------------+
     | Amazon S3     |
     |  (Upload)     |
     +---------------+
             |
       S3 Event Trigger
             |
             v
   +-----------------------+
   | AWS Lambda Function   |
   | - Parse CSV           |
   | - Insert / Update     |
   | - Delete              |
   +-----------------------+
             |
             v
   +-----------------------+
   | Amazon DynamoDB       |
   |   Product Table       |
   +-----------------------+
             |
             v
   +-----------------------+
   | CloudWatch Logs       |
   +-----------------------+

📂 Folder Structure
serverless-csv-pipeline/
│
├── lambda_function.py       # Main Lambda code
├── requirements.txt         # Python dependencies
├── sample.csv               # Example CSV file
└── README.md                # Documentation

🧠 How It Works
1️⃣ Upload CSV to S3

You upload a file like:

product_id,name,price,action
101,Redmi Note 12,15999,INSERT
102,Boat Headset,799,INSERT
101,Redmi Note 12,14999,UPDATE
102,Boat Headset,,DELETE

2️⃣ S3 Triggers Lambda

S3 Event = s3:ObjectCreated:*

Lambda receives:

bucket name

file key

3️⃣ Lambda Parses CSV

Lambda reads each row and checks:

action = INSERT / UPDATE / DELETE


Then performs:

Action	Operation
INSERT	Add new item
UPDATE	Update existing item
DELETE	Remove item
4️⃣ DynamoDB is Updated

Data is stored or modified in the table:

product_id (Partition key)
name
price
...

5️⃣ Logs in CloudWatch

Every action is logged:

Inserted product

Updated product

Deleted product

Errors (if any)

💻 Lambda Function Code (Production Ready)

Already given to you earlier — include the same lambda_function.py file in your repo.

🔧 Deployment Steps
1️⃣ Create DynamoDB Table

Name: FlipkartProducts

Primary Key: product_id (String)

2️⃣ Create an S3 Bucket

Example:

flipkart-product-csv-bucket

3️⃣ Create Lambda Function

Runtime: Python 3.9+

Add environment variable:

DDB_TABLE = FlipkartProducts

4️⃣ Add S3 Trigger

Go to → S3 Bucket → Properties → Event Notifications
Create:

Event: PUT

Prefix: (optional)

Send to: Lambda function

5️⃣ IAM Permissions

Attach to Lambda Role:

AmazonS3ReadOnlyAccess
AmazonDynamoDBFullAccess
CloudWatchLogsFullAccess

📊 Sample Output Logs (CloudWatch)
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

Event-driven architecture

Python CSV processing

Serverless design patterns
