# AWS Lazy BOT Tutorial

basic implementation of lambda function with python for manipulate AWS instance with Slack BOT

## Prerequsite

- create new AWS user & private key for SSH to EC2 instance
    - Add IAM role 
        - `AmazonEC2FullAccess`
- `aws configure`
    - setup credential when using aws
    - in this tutorial use `slack-bot` profile
- enable python virutal environment name `slack-env`
    - install all dependencies

## References
- [BOTO Shared Credential](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html#shared-credentials-file)
- [BOTO EC2 References](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html)
    - [BOTO instance](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#instance) with Id
    - [BOTO describe_instance](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client.describe_instances)