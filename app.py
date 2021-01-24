from aws_cdk import core

from ambiente_aws_data_lake.data_lake.stack import DataLakeStack

app = core.App()
data_lake = DataLakeStack(app)
app.synth()

