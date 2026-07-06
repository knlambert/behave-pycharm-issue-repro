from behave import given, then, when

from src.some_code import S3StorageConnectionInfo


@given('I create a key')
def step_given_name(context):
    S3StorageConnectionInfo(
        access_id="access_id",
        access_key="access_key",
        bucket_name="my_bucket"
    )
