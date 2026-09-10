import boto3
from datetime import datetime, timedelta

def find_large_instances():
    ec2 = boto3.client('ec2', region_name='us-east-1')
    resp = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    large = []
    for r in resp['Reservations']:
        for i in r['Instances']:
            if i['InstanceType'] in ['t3.large', 't3.xlarge', 'm5.large', 'm5.xlarge']:
                large.append({'id': i['InstanceId'], 'type': i['InstanceType'], 'state': i['State']['Name']})
    return large