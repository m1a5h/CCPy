#!/usr/bin/python
import os

me = os.environ.get('LOGNAME')

message = f"Hello {me}!"

print(message)
