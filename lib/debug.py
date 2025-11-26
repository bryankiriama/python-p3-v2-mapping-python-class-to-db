#!/usr/bin/env python3
#lib/testing/debug.py

from __init__ import CONN, CURSOR
from department import Department

import ipdb
Department.create_table()

# Creating department instances

it = Department ("IT", "Mombasa")
it.save()

payroll = Department("payroll", "Nairobi")
ipdb.set_trace()
