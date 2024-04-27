import boto3

ec2 = boto3.resource('ec2')

def lambda_handler(event, context):
    #filters = [{'Name': 'tag:Class', 'Values':['ClassB']},{'Name': 'instance-state-name', 'Values': ['running']}]
    filters = []
    instances=ec2.instances.filter(Filters=filters)
    for instance in instances:
        instance.terminate()
        print 'terminating instance: ' + str(instance)
