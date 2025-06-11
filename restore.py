import boto3

rds = boto3.client('rds')

SNAPSHOT_ID = 'your-snapshot-id'
NEW_DB_INSTANCE_ID = 'restored-db-instance'

def restore_from_snapshot():
    response = rds.restore_db_instance_from_db_snapshot(
        DBInstanceIdentifier=NEW_DB_INSTANCE_ID,
        DBSnapshotIdentifier=SNAPSHOT_ID,
        DBInstanceClass='db.t3.micro',
        PubliclyAccessible=True
    )
    print(f"Restore initiated for: {NEW_DB_INSTANCE_ID}")

if __name__ == "__main__":
    restore_from_snapshot()
