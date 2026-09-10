import boto3

def find_unused_ebs():
    volumes = []
    savings = 0
    for region in ['ap-south-1', 'us-east-1']:
        ec2 = boto3.client('ec2', region_name=region)
        vols = ec2.describe_volumes(Filters=[{'Name': 'status', 'Values': ['available']}])['Volumes']
        for v in vols:
            v['Region'] = region
            size = v['Size']
            # gp3 ~ $0.08/GB-month
            cost = size * 0.08
            v['MonthlyCost'] = cost
            savings += cost
            volumes.append(v)
    return volumes, savings