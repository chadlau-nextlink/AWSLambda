import boto3
region = 'us-east-1'
instances = ['i-0ef96d05207ab375c']
databases = ['test-chad']

def lambda_handler(event, context):
	ec2 = boto3.client('ec2', region_name=region)
	rds = boto3.client('rds')
	ec2.stop_instances(InstanceIds=instances)
	rds.stop_db_instance(DBInstanceIdentifier='test-chad')
	print 'stopped your instances: ' + str(instances)
	print 'stopped your instances: ' + str(databases)