import boto3

def find_unused_eips():
    eips = []
    for region in ['ap-south-1', 'us-east-1']:
        ec2 = boto3.client('ec2', region_name=region)
        addresses = ec2.describe_addresses()['Addresses']
        for eip in addresses:
            if 'InstanceId' not in eip:  # Not attached to EC2
                eip['Region'] = region
                eips.append(eip)
    return eips