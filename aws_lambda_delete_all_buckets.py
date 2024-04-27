import boto3

s3 = boto3.resource('s3')

def lambda_handler(event, context):
    #filters = [{'Name': 'tag:Class', 'Values':['ClassB']},{'Name': 'instance-state-name', 'Values': ['running']}]
    filters = []
    for bucket in s3.buckets.all():
        for key in bucket.objects.all():
            print 'deleting key' + str(key.key) + ' in bucket: ' + str(bucket)
            key.delete()
        print 'deleting bucket: ' + str(bucket)
        bucket.delete()
