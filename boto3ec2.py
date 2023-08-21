#!/usr/bin/python3

print("content-type: text/html")
print()


import cgi


import boto3

#AWS credentials and region
aws_access_key = ''
aws_secret_key = ''
region = 'ap-south-1'  # Change this to your desired region

# EC2 instance settings
instance_type = 't2.micro'  # Change this to your desired instance type
ami_id = ''  # Change this to your desired AMI ID


# Create a Boto3 EC2 client
ec2_client = boto3.client('ec2', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key, region_name=region)

# Launch EC2 instance
response = ec2_client.run_instances(
    ImageId=ami_id,
    InstanceType=instance_type,
    
    MinCount=1,
    MaxCount=1
)

print("Instance  has been launched.")
