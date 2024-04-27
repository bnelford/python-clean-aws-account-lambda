import boto3

ec2 = boto3.resource('ec2')

def lambda_handler(event, context):
    #filters = [{'Name': 'tag:Class', 'Values':['ClassB']},{'Name': 'instance-state-name', 'Values': ['running']}]
    filters = [{'Name': 'instance-state-name', 'Values': ['in-use']}]
    volumes=ec2.volumes.all()
    for volume in volumes:
        volume.detach_from_instance(Force=True)
        print 'detaching volume: ' + str(volume)
