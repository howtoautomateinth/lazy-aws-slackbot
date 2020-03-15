import boto3

session = boto3.Session(profile_name='slack-bot')
ec2 = session.client('ec2')

def get_instance_name(fid):
    ec2 = boto3.resource('ec2')
    instance = ec2.Instance(fid)
    instancename = ''
    for tags in instance.tags:
        if tags["Key"] == 'Name':
            instancename = tags["Value"]
    return instancename

def list_instances_by_tag_value(key, value):
    ec2 = session.client('ec2')
    response = ec2.describe_instances(
        Filters=[
            {
                'Name': 'tag:'+key,
                'Values': [value]
            }
        ]
    )
    instancelist = []
    for reservation in (response["Reservations"]):
        for instance in reservation["Instances"]:
            instancelist.append(instance["InstanceId"])
    return instancelist

def buildResponse(listId):
    response_list = []
    for id in listId:
        dictResponse = {}
        name = get_instance_name(id)
        dictResponse['name'] = name
        dictResponse['id'] = id
        response_list.append(dictResponse)
    return response_list

ids = list_instances_by_tag_value('Purpose','slack')
data_response = buildResponse(ids)
print(data_response)

