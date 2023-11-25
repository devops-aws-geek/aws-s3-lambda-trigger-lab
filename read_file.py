import json
import os
import boto3
import csv

def lambda_handler(event,  context):
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        file_key = record['s3']['object']['key']
        print(bucket, file_key)
        s3 = boto3.client('s3')
        csvfile = s3.get_object(Bucket=bucket, Key=file_key)
        csvcontent = csvfile['Body'].read().split(b'\n')
