# try-improve-code
Library for improving Python code


## Run all checks
```shell
PIPENV_IGNORE_VIRTUALENVS=1 pipenv run python -c'import src.ti_code as tic;tic.run_all("./src")'
```

## Step by step

1. Clean before analysis:
    ```shell
    PIPENV_IGNORE_VIRTUALENVS=1 pipenv run python -c'import src.ti_code as tic;tic.clean_before_test()'
    ```
1. Run black:
    ```shell
    PIPENV_IGNORE_VIRTUALENVS=1 pipenv run python -c'import src.ti_code as tic;tic.run_black("./src")'
    ```
1. Run isort:
    ```shell
    PIPENV_IGNORE_VIRTUALENVS=1 pipenv run python -c'import src.ti_code as tic;tic.run_isort("./src")'
    ```
1. Run flake8:
    ```shell
    PIPENV_IGNORE_VIRTUALENVS=1 pipenv run python -c'import src.ti_code as tic;tic.run_flake8("./src")'
    ```
1. Run radon:
    ```shell
    PIPENV_IGNORE_VIRTUALENVS=1 pipenv run python -c'import src.ti_code as tic;tic.run_radon("./src")'
    ```
1. Run final checks:
    ```shell
    PIPENV_IGNORE_VIRTUALENVS=1 pipenv run python -c'import src.ti_code as tic;tic.check_quality()'
    ```
