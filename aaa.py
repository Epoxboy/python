#!/usr/bin/python

# this is a demo

import boto3

ec2 = boto3.resource('ec2')
for instance in ec2.instances.all():
    print instance.id, instance.state

    
s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
        print(bucket.name)



