#!/usr/bin/env python
# -*- coding: utf-8 -*-
###############################################################################
#
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from __future__ import print_function

import argparse
import getpass

from odoo_api import *


def get_arguments():

    global server
    global username
    global password
    global dbname

    parser = argparse.ArgumentParser()
    parser.add_argument('--server', action="store", dest="server")
    parser.add_argument('--user', action="store", dest="username")
    parser.add_argument('--pw', action="store", dest="password")
    parser.add_argument('--db', action="store", dest="dbname")

    args = parser.parse_args()
    print('%s%s' % ('--> ', args))

    if args.server is not None:
        server = args.server
    elif server == '*':
        server = raw_input('server: ')

    if args.dbname is not None:
        dbname = args.dbname
    elif dbname == '*':
        dbname = raw_input('dbname: ')

    if args.username is not None:
        username = args.username
    elif username == '*':
        username = raw_input('username: ')

    if args.password is not None:
        password = args.password
    elif password == '*':
        password = getpass.getpass('password: ')


def secondsToStr(t):

    return "%d:%02d:%02d.%03d" % reduce(lambda ll, b: divmod(ll[0], b) + ll[1:], [(t * 1000,), 1000, 60, 60])


if __name__ == '__main__':

    server = 'http://localhost:8069'
    # server = '*'

    username = 'username'
    # username = '*'
    password = 'password'
    # password = '*'

    dbname = 'odoo'
    # dbname = '*'

    print()
    print('--> fmng.py...')
    print('--> server:', server)

    get_arguments()

    from time import time
    start = time()

    client = erppeek.Client(server, dbname, username, password)

    # file_args = []
    # db_path = 'data/fmng.sqlite'
    # print('-->', client, file_args, db_path)
    # print('--> Executing fmng_entity_export_sqlite()...')
    # print()
    # fmng_entity_export_sqlite(client, file_args, db_path)

    # file_args = []
    # db_path = 'data/fmng.sqlite'
    # print('-->', client, file_args, db_path)
    # print('--> Executing fmng_entity_import_sqlite()...')
    # print()
    # fmng_entity_import_sqlite(client, file_args, db_path)

    # tag_args = []
    # db_path = 'data/fmng.sqlite'
    # print('-->', client, tag_args, db_path)
    # print('--> Executing clv_tag_export_sqlite()...')
    # print()
    # clv_tag_export_sqlite(client, tag_args, db_path)

    # file_category_args = []
    # db_path = 'data/fmng.sqlite'
    # print('-->', client, file_category_args, db_path)
    # print('--> Executing clv_file_category_export_sqlite()...')
    # print()
    # clv_file_category_export_sqlite(client, file_category_args, db_path)

    # file_args = []
    # db_path = 'data/fmng.sqlite'
    # print('-->', client, file_args, db_path)
    # print('--> Executing clv_file_export_sqlite()...')
    # print()
    # clv_file_export_sqlite(client, file_args, db_path)

    # tag_args = []
    # db_path = 'data/fmng.sqlite'
    # print('-->', client, tag_args, db_path)
    # print('--> Executing clv_tag_import_sqlite()...')
    # print()
    # clv_tag_import_sqlite(client, tag_args, db_path)

    # file_category_args = []
    # db_path = 'data/fmng.sqlite'
    # print('-->', client, file_category_args, db_path)
    # print('--> Executing clv_file_category_import_sqlite()...')
    # print()
    # clv_file_category_import_sqlite(client, file_category_args, db_path)

    # file_args = []
    # db_path = 'data/fmng.sqlite'
    # print('-->', client, file_args, db_path)
    # print('--> Executing clv_file_import_sqlite()...')
    # print()
    # clv_file_import_sqlite(client, file_args, db_path)

    # file_args = []
    # db_path = 'data/fmng.sqlite'
    # print('-->', client, file_args, db_path)
    # print('--> Executing clv_file_import_parent_id_sqlite()...')
    # print()
    # clv_file_import_parent_id_sqlite(client, file_args, db_path)

    print()
    print('--> fmng.py', '- Execution time:', secondsToStr(time() - start))
    print()
