import boto3

def lambda_handler(event, context):
    rds = boto3.client('rds')
    snapshot_id = event.get('snapshot_id', 'your-snapshot-id')
    new_instance_id = event.get('new_instance_id', 'restored-db-instance')

    rds.restore_db_instance_from_db_snapshot(
        DBInstanceIdentifier=new_instance_id,
        DBSnapshotIdentifier=snapshot_id,
        DBInstanceClass='db.t2.micro',
        PubliclyAccessible=True
    )

    return {
        "statusCode": 200,
        "body": f"Restoration started for {new_instance_id} from snapshot {snapshot_id}"
    }
