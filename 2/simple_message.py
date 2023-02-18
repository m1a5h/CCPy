#!/usr/bin/python
import os
import datetime.datetime as dt

me = os.environ.get('USER')

message = f"Hello {me}!" if dt.now().millisecond % 2 == 0 else f"Hello world!"

print(message)
