import boto3
from datetime import datetime

rds = boto3.client('rds')
s3 = boto3.client('s3')

DB_INSTANCE_IDENTIFIER = 'your-db-instance'
S3_BUCKET = 'your-s3-bucket-name'

def create_snapshot():
    snapshot_id = f"{DB_INSTANCE_IDENTIFIER}-{datetime.now().strftime('%Y%m%d%H%M%S')}"
    response = rds.create_db_snapshot(
        DBInstanceIdentifier=DB_INSTANCE_IDENTIFIER,
        DBSnapshotIdentifier=snapshot_id
    )
    print(f"Snapshot started: {snapshot_id}")
    return snapshot_id

if __name__ == "__main__":
    create_snapshot()
