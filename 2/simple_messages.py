#!/usr/bin/python3

import os
import datetime as dt

me = os.environ.get("LOGNAME")

message = f"Hello {me}!" if dt.datetime.now().microsecond % 2 == 0 else f"Hello world!"

print(message)
