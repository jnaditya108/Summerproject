#!/usr/bin/python3

print("content-type: text/html")
print()

import boto3

region = 'ap-south-1'

def create_s3_bucket(bucket_name, region=region):
    try:
        s3_client = boto3.client('s3', region_name=region)
        location_constraint = region if region != 'us-east-1' else ''

        s3_client.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={
                'LocationConstraint': location_constraint
            }
        )
        print(f"Bucket '{bucket_name}' created successfully.")
    except Exception as e:
        print(f"Error creating bucket '{bucket_name}': {e}")

create_s3_bucket("aditya009092hdkfvhdfkvdddd")
