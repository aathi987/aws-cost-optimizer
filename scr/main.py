from scanners.ebs import find_unused_ebs
from scanners.ec2 import find_large_instances

if __name__ == "__main__":
    print("--- AWS COST SCAN STARTED ---")
    ebs = find_unused_ebs()
    ec2 = find_large_instances()
    
    total = sum(x['monthly_cost'] for x in ebs)
    
    print(f"\nFound {len(ebs)} Unused EBS Volumes")
    for v in ebs: print(v)
    
    print(f"\nFound {len(ec2)} Large Running EC2s")
    for i in ec2: print(i)
    
    print(f"\n💰 POTENTIAL SAVINGS: ${total} / month from EBS alone")