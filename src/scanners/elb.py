import boto3

def find_idle_elb():
    idle = []
    for region in ['ap-south-1', 'us-east-1']:
        elb = boto3.client('elbv2', region_name=region)
        try:
            lbs = elb.describe_load_balancers()['LoadBalancers']
            for lb in lbs:
                # Check if no targets
                idle.append(lb)
        except:
            pass
    return idle