import click
from bceutils.base import bce_cli
import bceutils.base as bcebase
import json

from baidubce.services.eip.eip_bp_client import EipBpClient

@bce_cli.group()
@click.pass_context
def eipbp(ctx):
  """带宽包命令"""
  ctx.obj['client'] = EipBpClient(bcebase.create_bce_config('eip', credentials=ctx.obj['credentials'], region=ctx.obj['region']))


@eipbp.command()
@click.pass_context
@click.option('--eip', help='带宽包绑定的EIP地址，和eip-group-id二选一')
@click.option('--eip-group-id', help='带宽包绑定的共享带宽ID，和eip二选一')
@click.option('--bandwidth-in-mbps', type=int, required=True, help='带宽包的带宽大小，单位Mbps')
@click.option('--name', help='带宽包名称')
@click.option('--auto-release-time', required=True, help='自动释放时间，UTC格式：yyyy-mm-ddThh:mm:ssZ')
@click.option('--client-token', required=True, help='客户端幂等性token')
def create(ctx, eip, eip_group_id, bandwidth_in_mbps, name, auto_release_time, client_token):
  """创建带宽包"""
  result = ctx.obj['client'].create_eip_bp(eip, eip_group_id, bandwidth_in_mbps, name, auto_release_time, client_token)
  print(bcebase.bce_reponse_to_str(result))


@eipbp.command()
@click.pass_context
@click.option('--id', help='带宽包ID')
@click.option('--name', help='带宽包名称')
@click.option('--bind-type', type=click.Choice(['eip', 'eipgroup'], case_sensitive=False), help='带宽包绑定类型')
def list(ctx, id, name, bind_type):
  """查询用户带宽包列表信息"""
  result = ctx.obj['client'].list_eip_bps(id=id, name=name, bind_type=bind_type)
  print(bcebase.bce_reponse_to_str(result))


@eipbp.command()
@click.pass_context
@click.option('--id', help='带宽包ID')
@click.option('--new-bandwidth-in-mbps', help='带宽包名称')
@click.option('--client-token', required=True, help='客户端幂等性token')
def resize(ctx, id, new_bandwidth_in_mbps, client_token):
  """调整带宽包带宽"""
  result = ctx.obj['client'].resize_eip_bp(id, new_bandwidth_in_mbps, client_token=client_token)
  print(bcebase.bce_reponse_to_str(result))
