

doc = [{'DBInstanceMemory': 1024, 'ResourceGroupId': 'rg-acfmwfskyjkwkgi', 'Port': '3306', 'LatestKernelVersion': 'rds_20200430', 'DBInstanceType': 'Primary', 'ConsoleVersion': '', 'InstanceNetworkType': 'VPC', 'DBInstanceClassType': 'x', 'DBInstanceId': 'rm-bp1i91og36706i98q', 'AutoUpgradeMinorVersion': 'Auto', 'DBInstanceStorage': 20, 'AvailabilityValue': '100.0%', 'Engine': 'MySQL', 'IPType': 'IPv4', 'DBInstanceDiskUsed': 1297088512, 'EngineVersion': '5.7', 'DBInstanceStatus': 'Running', 'MaxConnections': 2000, 'DBInstanceClass': 'mysql.n1.micro.1', 'AccountMaxQuantity': 99999, 'VSwitchId': 'vsw-bp15h7w5xmbrh6oakn9j0', 'PayType': 'Postpaid', 'LockMode': 'Unlock', 'SupportCreateSuperAccount': 'Yes', 'InsId': 1, 'VpcId': 'vpc-bp1vwt43jqxj6zilb29c5', 'CurrentKernelVersion': 'rds_20200430', 'CreationTime': '2020-11-02T11:34:53Z', 'ConnectionMode': 'Standard', 'VpcCloudInstanceId': 'rm-bp1i91og36706i98q', 'ProxyType': 0, 'ConnectionString': 'rm-bp1i91og36706i98q.mysql.rds.aliyuncs.com', 'ExpireTime': '', 'DBMaxQuantity': 99999, 'Category': 'Basic', 'DBInstanceNetType': 'Intranet', 'SuperPermissionMode': '', 'DedicatedHostGroupId': '', 'DBInstanceCPU': '1', 'SecurityIPList': '', 'OriginConfiguration': '', 'ReadOnlyDBInstanceIds': {'ReadOnlyDBInstanceId': []}, 'SecurityIPMode': 'normal', 'MaintainTime': '18:00Z-22:00Z', 'DispenseMode': 'ClassicDispenseMode', 'ZoneId': 'cn-hangzhou-h', 'DBInstanceStorageType': 'cloud_ssd', 'AccountType': 'Mix', 'MaxIOPS': 1500, 'SupportUpgradeAccountType': 'Yes', 'SlaveZones': {'SlaveZone': []}, 'Extra': {'DBInstanceIds': {'DBInstanceId': []}}, 'CanTempUpgrade': False, 'RegionId': 'cn-hangzhou'}]

doc = doc[0]
print(doc)
dicss = {}
for i in doc :
    print(type(i))

    dicss[i] = doc[i]

print(dicss)

a=0
for i in dicss:
    a += 1
    print(dicss[i],a)