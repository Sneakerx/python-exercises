"""Prints the current Python version."""

import sys

INFOS = sys.version
print(INFOS)

# Get the version number only
version = INFOS.split(" ", maxsplit=1)[0]
print(version)

# Or for version comparisons / checks:
print(
    f"""Python-Version:
{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"""
)
