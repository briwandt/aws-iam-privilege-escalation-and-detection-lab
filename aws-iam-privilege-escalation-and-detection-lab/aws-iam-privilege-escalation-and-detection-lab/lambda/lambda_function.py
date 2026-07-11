import boto3

s3 = boto3.client("s3")

BUCKET_NAME = "brianna-iam-escalation-lab-48291"
OBJECT_KEY = "protected-lab-data.txt"


def lambda_handler(event, context):
    response = s3.get_object(
        Bucket=BUCKET_NAME,
        Key=OBJECT_KEY
    )

    contents = response["Body"].read().decode("utf-8")

    return {
        "statusCode": 200,
        "bucket": BUCKET_NAME,
        "object": OBJECT_KEY,
        "contents": contents
    }
