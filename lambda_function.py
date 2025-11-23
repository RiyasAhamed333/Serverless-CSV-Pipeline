import boto3
import csv
import os
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

s3 = boto3.client("s3")
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ["DDB_TABLE"])

def lambda_handler(event, context):
    try:
        # Get S3 Bucket + File Name
        records = event["Records"][0]["s3"]
        bucket = records["bucket"]["name"]
        key = records["object"]["key"]

        logger.info(f"File received: s3://{bucket}/{key}")

        # Read CSV file
        csv_file = s3.get_object(Bucket=bucket, Key=key)
        rows = csv_file["Body"].read().decode("utf-8").splitlines()

        csv_reader = csv.DictReader(rows)

        with table.batch_writer() as batch:
            for row in csv_reader:
                action = row.get("action", "").upper()
                product_id = row.get("product_id")

                if not product_id:
                    logger.error("Missing product_id, skipping row")
                    continue

                # INSERT
                if action == "INSERT":
                    batch.put_item(Item=row)
                    logger.info(f"Inserted: {product_id}")

                # UPDATE
                elif action == "UPDATE":
                    batch.put_item(Item=row)
                    logger.info(f"Updated: {product_id}")

                # DELETE
                elif action == "DELETE":
                    batch.delete_item(Key={"product_id": product_id})
                    logger.info(f"Deleted: {product_id}")

                else:
                    logger.error(f"Invalid action: {action}")

        return {
            "status": "success",
            "message": "CSV processed successfully"
        }

    except Exception as e:
        logger.exception("Error processing CSV")
        return {
            "status": "error",
            "message": str(e)
        }
