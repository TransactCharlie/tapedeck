import sys


class StdOutByteWriter:

    def __init__(self):
        self.stdout = sys.stdout

    def write(self, b):
        self.stdout.buffer.write(b)