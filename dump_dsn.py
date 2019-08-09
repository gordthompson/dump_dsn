# Copyright 2019 Gordon D. Thompson
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import winreg

"""dump_dsn

A module to extract ODBC DSN settings from the Windows Registry.
"""


def to_dict(dsn_name):
    """Return the DSN settings as a `dict`.
    """
    try:
        reg = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
        reg_key = winreg.OpenKey(reg, 'SOFTWARE\\ODBC\\ODBC.INI\\' + dsn_name)
    except FileNotFoundError:
        try:
            reg = winreg.ConnectRegistry(None, winreg.HKEY_LOCAL_MACHINE)
            reg_key = winreg.OpenKey(reg, 'SOFTWARE\\ODBC\\ODBC.INI\\' + dsn_name)
        except FileNotFoundError:
            raise ValueError('Cannot find "{}" as a User or System DSN'.format(dsn_name))
    dsn_dict = {}
    for i in range(winreg.QueryInfoKey(reg_key)[1]):
        tup = winreg.EnumValue(reg_key, i)
        dsn_dict[tup[0]] = tup[1]
    return dsn_dict


def to_text(dsn_name):
    """Return the DSN settings as they would appear in an odbc.ini file.
    """
    dsn_dict = to_dict(dsn_name)
    return '[{}]'.format(dsn_name) \
           + ''.join('\r\n{}={}'.format(name, dsn_dict[name]) for name in dsn_dict)


if __name__ == '__main__':
    try:
        test_dsn_name = 'PostgreSQL35W'
        print(to_text(test_dsn_name))
    except ValueError as ve:
        print(ve)
