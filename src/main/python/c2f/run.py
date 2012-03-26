#!/usr/bin/env python
## -*- coding: utf-8 -*-

import os
import sys
import logging

# log
logger = logging.getLogger(__name__)

stderr = sys.stderr.write

# python path
app_path = os.path.realpath(__file__)
package_path = os.path.dirname(app_path)
base_path = os.path.split(package_path)[0]
sys.path.append(base_path)  # append source dir to python path


if __name__ == '__main__':
    from c2f.site import config
    # verifica se eh passado o path do arquivo de configuracao no "start" do server
    if len(sys.argv) < 2:
        config_file = os.path.join(package_path, 'site', 'config', 'system.conf')
    else:
        config_file = sys.argv[1]

    # load config
    config.load(config_file)

    stderr('Iniciando Site... \n')

    from bottle import run as bottle_run
    from bottle import debug as bottle_debug
    from bottle import TEMPLATE_PATH as bottle_template_path
    from c2f.site import app
    from c2f.site.controller import *  # @UnusedWildImport

    # verifica se eh passado o path do arquivo de pid no "start" do server
    if len(sys.argv) < 3:  # FIXME verificar como guinicorn trata daemonization e implementar!
        pid_file_name = '/tmp/site.pid'  # FIXME barras padrão sistema operacional
    else:
        pid_file_name = sys.argv[2]

    config.base_path = base_path

    # write pid
    pid_file = open(pid_file_name, 'w')
    pid_file.write(str(os.getpid()))  # FIXME verificar como guinicorn trata daemonization e implementar!
    pid_file.close()

    bottle_template_path.append(package_path + '/site/view/')
    #stderr("%s" % bottle_template_path)
    bottle_debug(True)
    bottle_run(app, host='0.0.0.0', port=config.parameters.getint('system', 'http_port'), reloader=True)
