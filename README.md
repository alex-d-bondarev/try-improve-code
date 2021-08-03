# try_improve_code POC
Package for improving Python code

## Example usage
```shell
python -c'import try_improve.code as tic;tic.run_all("<path_to_project>")'
```


## Build and install the project
```shell
PIPENV_IGNORE_VIRTUALENVS=1 pipenv run python setup.py bdist_wheel
PIPENV_IGNORE_VIRTUALENVS=1 pipenv run pip install -e .
pipenv shell
python
```
```python
import try_improve.code as tic
tic.run_all("./try_improve")
exit()
```
```shell
exit
```


## Run all checks
```shell
PIPENV_IGNORE_VIRTUALENVS=1 pipenv run python -c'import try_improve.code as tic;tic.run_all("./try_improve")'
```

## Step by step

1. Clean before analysis:
    ```shell
    PIPENV_IGNORE_VIRTUALENVS=1 pipenv run python -c'import try_improve.code as tic;tic.clean_before_test()'
    ```
1. Run black:
    ```shell
    PIPENV_IGNORE_VIRTUALENVS=1 pipenv run python -c'import try_improve.code as tic;tic.run_black("./try_improve")'
    ```
1. Run isort:
    ```shell
    PIPENV_IGNORE_VIRTUALENVS=1 pipenv run python -c'import try_improve.code as tic;tic.run_isort("./try_improve")'
    ```
1. Run flake8:
    ```shell
    PIPENV_IGNORE_VIRTUALENVS=1 pipenv run python -c'import try_improve.code as tic;tic.run_flake8("./try_improve")'
    ```
1. Run radon:
    ```shell
    PIPENV_IGNORE_VIRTUALENVS=1 pipenv run python -c'import try_improve.code as tic;tic.run_radon("./try_improve")'
    ```
1. Run final checks:
    ```shell
    PIPENV_IGNORE_VIRTUALENVS=1 pipenv run python -c'import try_improve.code as tic;tic.check_quality()'
    ```
