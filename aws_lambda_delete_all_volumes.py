import boto3

ec2 = boto3.resource('ec2')

def lambda_handler(event, context):
    #filters = [{'Name': 'tag:Class', 'Values':['ClassB']},{'Name': 'instance-state-name', 'Values': ['running']}]
    filters = []
    volumes=ec2.volumes.all()
    for volume in volumes:
        volume.delete()
        print 'deleting volume: ' + str(volume)
