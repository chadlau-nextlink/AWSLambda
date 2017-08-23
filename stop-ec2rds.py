import boto3
region = 'us-east-1'
instances = ['instanceid']
databases = ['dbidentifier']

def lambda_handler(event, context):
	ec2 = boto3.client('ec2', region_name=region)
	rds = boto3.client('rds')
	ec2.stop_instances(InstanceIds=instances)
	rds.stop_db_instance(DBInstanceIdentifier='dbidentifier')
	print 'stopped your instances: ' + str(instances)
	print 'stopped your instances: ' + str(databases)
