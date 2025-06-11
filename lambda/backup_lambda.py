import boto3
from datetime import datetime

def lambda_handler(event, context):
    rds = boto3.client('rds')
    db_instance = event.get('db_instance', 'your-db-instance')
    snapshot_id = f"{db_instance}-{datetime.now().strftime('%Y%m%d%H%M%S')}"

    rds.create_db_snapshot(
        DBInstanceIdentifier=db_instance,
        DBSnapshotIdentifier=snapshot_id
    )

    return {
        "statusCode": 200,
        "body": f"Snapshot {snapshot_id} created successfully."
    }
