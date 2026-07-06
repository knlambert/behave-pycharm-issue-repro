# Behave + Poetry example

```bash
poetry config virtualenvs.in-project true --local
poetry install
poetry run behave
```

# To fix the issue

```cli
patch -b "/Applications/PyCharm.app/Contents/plugins/python-ce/helpers/pycharm/behave_runner.py" fix_behave.diff
```
