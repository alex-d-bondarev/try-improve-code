from setuptools import setup, find_packages

setup(
    name='try_improve_code',
    version='0.0.1',
    python_requires=">=3.9",
    description='Package for improving Python code',
    url='https://github.com/alex-d-bondarev/try-improve-code',
    author='Sasha Bondarev (Oleksandr)',
    author_email='alex.d.bondarev@gmail.com',
    license='MIT',
    # py_modules=['ti_code'],
    # package_dir={'', 'src'},
    packages=find_packages(),
    install_requires=[
        'black==21.7b0',
        'flake8==3.9.2',
        'isort==5.9.2',
        'radon==4.1.0',
    ]
)
