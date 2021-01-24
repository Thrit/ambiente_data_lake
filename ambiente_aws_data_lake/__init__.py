import os

from ambiente_data_lake.ambiente_aws_data_lake.environment import Environment

active_environment = Environment[os.environ['ENVIRONMENT']]