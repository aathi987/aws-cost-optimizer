import boto3
from datetime import datetime, timezone

def find_old_snapshots(days=90):
    ec2 = boto3.client('ec2', region_name='ap-south-1')
    snaps = ec2.describe_snapshots(OwnerIds=['self'])['Snapshots']
    old = []
    for s in snaps:
        age = (datetime.now(timezone.utc) - s['StartTime']).days
        if age > days:
            s['AgeDays'] = age
            old.append(s)
    return old