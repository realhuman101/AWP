# Contributing to this project

Thank you for taking the time to contribute to this project!
We appreciate your help and welcome any contributions you make.

When contributing, please follow the [Code of Conduct](CODE_OF_CONDUCT.md), and to contribute, you can do the following:

1. Fork the repository
2. Create a new branch for your changes
3. Make your changes and commit them
4. Push the new branch to your fork
5. Submit a pull request

## Installing the program

First, clone the repository:

```shell
git clone https://github.com/realhuman101/AFFP.git
```

Then, install the dependencies:

```shell
pip install -r requirements.txt
```

Or, depending on your installation:

```shell
pip3 install -r requirements.txt
```

To install the program itself in development mode, run the following command:

```shell
python setup.py develop
```

Or, depending on your installation:

```shell
python3 setup.py develop
```

To run the program, run the following command:

```shell
AWP
```

## Formatting

Please make sure you follow all the Flake8 formatting rules (besides `W191` and `E501`, `E128`, and `F401` only if there is a viable reason). You can check this by running the following command:

```shell
flake8 --ignore=W191,E501,F401,E128
```
