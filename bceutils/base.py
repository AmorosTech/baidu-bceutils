import click
import json
import os
import logging as log
from pathlib import Path
from baidubce.auth.bce_credentials import BceCredentials
from baidubce.bce_client_configuration import BceClientConfiguration

bce_config_file_path = Path.home() / '.config/bceutils/config.json'
bce_endpoints = {
  'eip': 'eip.{region}.baidubce.com'
}

@click.group(invoke_without_command=True)
@click.pass_context
@click.option('--region', envvar="BCE_REGION", help="所在地域")
@click.option('--config', is_flag=True, help="保存访问密钥和地域至~/.config/bceutils/config.json")
def bce_cli(ctx, region, config):
  config_json = {}

  if config or not bce_config_file_path.is_file() or bce_config_file_path.stat().st_size == 0:
    config_json['access_key'] = click.prompt('AccessKey')
    config_json['access_secret'] = click.prompt('AccessSecret')
    config_json['region'] = click.prompt('Region')
    if config:
      bce_config_file_path.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
      with bce_config_file_path.open(mode='w+') as config_file:
        config_file.write(json.dumps(config_json, indent=2))
      bce_config_file_path.chmod(0o600)
  else:
    with bce_config_file_path.open() as config_file:
      config_json = json.load(config_file)

  ctx.obj['credentials'] = BceCredentials(config_json['access_key'], config_json['access_secret'])
  ctx.obj['region'] = config_json['region']
  ctx.obj['_raw_config'] = config_json
  if region:
    ctx.obj['region'] = region


def bce_reponse_to_str(bce_response):
  return json.dumps(json.loads(bce_response.raw_data), indent=2)

def get_bce_endpoint(service, region=None):
  return bce_endpoints[service].format(**{'region': region})

def create_bce_config(service, credentials=None, region=None):
  return BceClientConfiguration(credentials=credentials,
                                endpoint=get_bce_endpoint(service, region=region))