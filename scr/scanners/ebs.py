import boto3
def find_unused_ebs():
    ec2 = boto3.client('ec2', region_name='us-east-1')
    volumes = ec2.describe_volumes(Filters=[{'Name': 'status', 'Values': ['available']}])
    waste = []
    for v in volumes['Volumes']:
        waste.append({
            'id': v['VolumeId'],
            'size_gb': v['Size'],
            'monthly_cost': round(v['Size'] * 0.08, 2),
            'created': str(v['CreateTime'].date())
        })
    return waste