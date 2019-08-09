# dump_dsn

Linux and Mac machines store their ODBC DSN definitions in a plain text file. Windows, on the other hand, stores its DSN definitions in the Registry and presents them with a GUI from ODBC Administrator (odbcad32.exe). That makes it a bit awkward to determine precisely what the DSN settings are when providing remote assistance.

This module simply extracts the DSN settings from the Registry. The `to_dict` method puts the information into a `dict`, while the `to_text` method constructs a string that mimics the corresponding section of an odbc.ini file.

Sample usage:

```python
import dump_dsn

print(dump_dsn.to_text('my_dsn'))

""" console output:
[my_dsn]
Driver=C:\PROGRA~1\COMMON~1\MICROS~1\OFFICE14\ACEODBC.DLL
DBQ=C:\Users\Public\Database1.accdb
...
"""
```

**NOTE:** Some ODBC drivers will store database credentials (username/password) in the DSN definition. Check your output carefully before sharing it with someone who should not have that information.