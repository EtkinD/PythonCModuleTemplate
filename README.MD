# Python C Module Template

This is a template for a Python C module. It is a simple example that shows how to create a Python module in C and C++.

## How to use

1. Clone the repository
2. `init.sh` to initialize the project
3. `source venv/bin/activate` to activate the virtual environment
4. `pip install .` for installing the module or `pip install -e .` for installing the module in editable mode
5. `python -m tests` to run the tests
6. `python -m pycmtemplate` or directly run `pycmtemplate` to run the module from the command line

## How to build with `setup.py`

Required configurations are in the `setup.py` file. The `init.sh` script initializes the project by creating virtual environment and installing the required packages.

To build the module, run the following command:

```bash
python setup.py build
```

The build command will create a `build` directory with the compiled module.

### Install after build

To install the module after building via `setup.py`, run the following command:

```bash
python setup.py install
```

## How to build and install with `pip`

To build and install the module with `pip`, run the following command:

```bash
pip install .
```

To install the module in editable mode, run the following command:

```bash
pip install -e .
```

Note: editable mode is useful for development purposes. It allows you to modify the source code and see the changes without reinstalling the module. However, it does not work with C/C++ modules.

## How to run the module

After installing the module, you can run it from the command line:

```bash
python -m pycmtemplate
```

or directly:

```bash
pycmtemplate
```

## How to run the tests

To run the tests:

```bash
python -m tests
```

## How to clean up

To clean up the project, run the following command:

```bash
./clean.sh
```

The `clean.sh` script removes the `build`, `dist`, `pycmtemplate.egg-info` and `venv` directories, as well as the `__pycache__` directories.
