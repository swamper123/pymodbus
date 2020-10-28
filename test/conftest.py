from pymodbus.compat import PYTHON_VERSION
if PYTHON_VERSION.minor < 7:
    collect_ignore = ["test_server_asyncio.py"]
