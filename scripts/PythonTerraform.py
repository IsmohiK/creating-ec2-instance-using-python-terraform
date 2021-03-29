''''
python-terraform is a python module provide a wrapper of terraform command line tool.
'''

from python_terraform import *
import yaml
import json
import sys

def PythonTerraform():
	#### Reading teh manifest file for E2 config ####
	with open("scripts\\EC2_manifest.yaml", "r") as f:
		config = yaml.safe_load(f)
		f.close()
	vars_dict = {
		'desiredCapacity':config['params']['default']['desiredCapacity'],
		'region':config['params']['default']['region'],
		'role_arn':config['params']['default']['RoleArn'],
		'ami-name':config['params']['default']['ami-name'],
		'instance_type':config['params']['default']['instance_type'],
		'resourceName':config['params']['default']['resourceName']
	}
	tf = Terraform(working_dir='C:\\Automation\\terraform',variables=vars_dict)
	tf.init()
	'''
	Run terraform plan to check whether the execution plan for a configuration matches your 
	expectations before provisioning or changing infrastructure.
	'''
	approve = {"auto-approve": True, "capture_output":True}
	print("Terraform plan Started")
	tuple_output = tf.plan(capture_output=True)
	print(tuple_output[-2])
	'''
	Apply changes to hundreds of cloud providers with terraform apply 
	to reach the desired state of the configuration.
	'''
	print("Terraform apply Started")
	print("Type yes to perform terraform apply")
	tuple_output = tf.apply(**approve)
	print(tuple_output[-2])


