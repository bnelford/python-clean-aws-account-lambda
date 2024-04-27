import boto3

ec2 = boto3.resource('ec2')

def lambda_handler(event, context):
    #filters = [{'Name': 'tag:Class', 'Values':['ClassB']},{'Name': 'instance-state-name', 'Values': ['running']}]
    filters = []
    snapshots=ec2.snapshots.filter(OwnerIds=["583027634990"])
    for snapshot in snapshots:
        snapshot.delete()
        print 'deleting snapshot: ' + str(snapshot)
