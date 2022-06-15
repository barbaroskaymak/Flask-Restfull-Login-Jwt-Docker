#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# standard python imports

postgresql = {'host': 'database',
         'user': 'user',
         'passwd': 'password',
         'db': 'db'}

postgresqlConfig = "postgresql+psycopg2://{}:{}@{}/{}".format(postgresql['user'], postgresql['passwd'], postgresql['host'], postgresql['db'])

