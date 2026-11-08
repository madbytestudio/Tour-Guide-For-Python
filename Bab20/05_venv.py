import sys

print("Executable:", sys.executable)
print("Prefix:", sys.prefix)
print("Base prefix:", sys.base_prefix)
print("Dalam venv:", sys.prefix != sys.base_prefix)
