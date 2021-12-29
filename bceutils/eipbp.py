import click
from bceutils.base import bce_cli
from bceutils.base import bce_reponse_to_str
import logging as log
import json

from baidubce.bce_client_configuration import BceClientConfiguration
from baidubce.services.eip.eip_bp_client import EipBpClient

@bce_cli.group()
@click.pass_context
def eipbp(ctx):
  """带宽包命令"""
  config = BceClientConfiguration(credentials=ctx.obj['credentials'],
                                endpoint='eip.{}.baidubce.com'.format(ctx.obj['region']))
  ctx.obj['client'] = EipBpClient(config)


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
  local_vars = dict(locals())
  del local_vars['ctx']
  log.info("eipbp create: {}".format(local_vars))
  result = ctx.obj['client'].create_eip_bp(eip, eip_group_id, bandwidth_in_mbps, name, auto_release_time, client_token)
  log.info(bce_reponse_to_str(result))


@eipbp.command()
@click.pass_context
@click.option('--id', help='带宽包ID')
@click.option('--name', help='带宽包名称')
@click.option('--bind-type', type=click.Choice(['eip', 'eipgroup'], case_sensitive=False), help='带宽包绑定类型')
def list(ctx, id, name, bind_type):
  result = ctx.obj['client'].list_eip_bps(id=id, name=name, bind_type=bind_type)
  log.info(bce_reponse_to_str(result))

