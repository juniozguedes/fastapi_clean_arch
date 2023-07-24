# Pytest

Pytest with logs:

```
 pytest -s -v
```

# Linter checking

To check pre-commit status:

```
 pre-commit run --all-files
```

# Freezing requirements with venv

Might change depending on the OS, but find the pip inside venv folder:

```
 .\venv\Scripts\pip3 freeze > requirements.txt
```

# First time you create a project from scratch considerations

Generate pylintrc:

```
pylint --generate-rcfile | out-file -encoding utf8 .pylintrc
```

after configurating the .pre-commit-config.yaml

```
pre-commit install
```
