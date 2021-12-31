import click
from bceutils.base import bce_cli
import bceutils.base as bcebase
import json

from baidubce.bce_client_configuration import BceClientConfiguration
from baidubce.services.eip.eip_group_client import EipGroupClient

@bce_cli.group()
@click.pass_context
def eipgroup(ctx):
  """共享带宽命令"""
  ctx.obj['client'] = EipGroupClient(bcebase.create_bce_config('eip', credentials=ctx.obj['credentials'], region=ctx.obj['region']))


@eipgroup.command()
@click.pass_context
@click.option('--id', help='共享带宽ID')
@click.option('--name', help='共享带宽名称')
@click.option('--status', type=click.Choice(['creating', 'available', 'binded', 'binding', 'unbinding', 'updating', 'paused', 'unavailable'], case_sensitive=False), 
                          help='共享带宽状态')
@click.option('--marker', help='批量获取列表的查询的起始位置，是一个由系统生成的字符串')
@click.option('--max-keys', help='每页包含的最大数量，最大数量不超过1000。缺省值为1000', default=1000)
def list(ctx, id, name, status, marker, max_keys):
  """查询用户带宽包列表信息"""
  result = ctx.obj['client'].list_eip_groups()
  print(bcebase.bce_reponse_to_str(result))

