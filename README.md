# Based
---

This is based, a python package that makes using json databases easy.

How to use:
---
Writing Keys:
```py
from Based import Based

Database = Based("Lipsum")
Lipsum = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
Database.write("Lipsum",Lipsum)
```
Reading Keys:
```py
from Based import Based

Database = Based("Lipsum")
Lipsum = Database.get("Lipsum")
```
Deleting Keys:
```py
from Based import Based

Database = Based("Lipsum")
Lipsum = Database.delete("Lipsum")
```
Wiping the Database:
```py
from Based import Based

Database = Based("Lipsum")
Lipsum = Database.nuke()
```
