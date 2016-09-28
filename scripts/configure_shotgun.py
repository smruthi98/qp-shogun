#!/usr/bin/env python

# -----------------------------------------------------------------------------
# Copyright (c) 2014--, The Qiita Development Team.
#
# Distributed under the terms of the BSD 3-clause License.
#
# The full license is in the file LICENSE, distributed with this software.
# -----------------------------------------------------------------------------

import click

from qp_shotgun import plugin


@click.command()
def config():
    """Generates the Qiita configuration files"""
    env_script = click.prompt('Environment script',
                              default='source activate qp-target-gene')
    server_cert = click.prompt('Server certificate', default='None')
    if server_cert == 'None':
        server_cert = None
    plugin.generate_config(env_script, 'start_shotgun',
                           server_cert=server_cert)

if __name__ == '__main__':
    config()
