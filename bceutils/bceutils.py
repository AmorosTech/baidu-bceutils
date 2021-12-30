import click
import logging as log


log.basicConfig(
    level   = log.INFO, 
    format  = "[%(asctime)s] %(levelname)s [%(threadName)s@%(pathname)s:%(lineno)s] - %(message)s", 
    datefmt = "%Y%m%d %H:%M:%S"
  )

import bceutils.base as base


def main():
  base.bce_cli(obj={})

if __name__ == '__main__':
  main()
