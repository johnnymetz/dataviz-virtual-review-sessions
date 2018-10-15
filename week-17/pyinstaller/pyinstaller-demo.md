# PyInstaller Demo

Distribute your app as a single file executable.

Docs: https://pyinstaller.readthedocs.io/en/stable/
Icon generator: https://iconverticons.com/online/

```bash
# develop app (code, virtual env)
conda create -n pyinstaller python=3.6
pip install flask flask_sqlalchemy

# install pyinstaller
pip install pyinstaller

# create executable
pyinstaller app.py --name 'Todo List' --onefile --clean --add-data './templates:templates' --add-data './static:static' --add-data './db.sqlite3:.' --icon pencil-icon.svg.icns
```
