# <div align="center">AFFP - Automated Forest Fire Prediction</div>

<div align="center"><i>AI for a safer, and greener future</i></div>

***

> **NOTE:** This project is currently in development and is not ready for use.

## Table of Contents

- [AFFP - Automated Forest Fire Prediction](#affp---automated-forest-fire-prediction)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Datasets](#datasets)
  - [Model](#model)
  - [Contributing](#contributing)
  - [License](#license)
  - [Credits](#credits)
  - [Contact](#contact)
  - [Acknowledgments](#acknowledgments)

## Introduction

AFFP (Automated Forest Fire Prediction) is a Python-based project that uses machine learning and Tensorflow to predict and prevent forest fires. By analyzing a dataset of historical forest fire data, AFFP is able to identify patterns and trends that can help forecast the likelihood of future fires in a given area. This information can be used to take proactive measures to prevent fires from starting or spreading, and to help emergency responders better allocate their resources.

This project is part of the [AIoT Engineering & Entrepreneurial Skills Education for Gifted Students programme](https://cityueegef.github.io/about/).

## Requirements

- Python 3.10 to Python 3.10.9
- Tensorflow 2.10.1 or higher
- Numpy 1.24.1 or higher
- Pandas 1.5.2 or higher
- Requests 2.28.1 or higher
- Setuptools 63.2.0 or higher
- Scikit-learn 1.2.1 or higher
- Scipy 1.10.0 or higher
- Keras 2.11.0 or higher
- Matplotlib 3.5.1 or higher
  
For a complete list of requirements, please check our [requirements.txt](requirements.txt).

## Installation

To install the required packages, run the following command:

```py
pip install -r requirements.txt
```

Or, depending on your installation:

```py
pip3 install -r requirements.txt
```

## Usage

> **NOTE:** Project is still **in development** and is therefore unavailable for use. The following instructions are for development purposes only.

First we must install the program, which can be done by running the following command:

```shell
python setup.py install
```

Or, depending on your installation:

```shell
python3 setup.py install
```

Then, we can run the program by running the following command:

```shell
affp
```

A GUI will then appear.

> These instructions are not yet completed, and will be completed upon completion of the project.

## Datasets

> *See official citation [here](src/model/datasets/README.md)*

- Our [dataset](src/model/datasets/dataset.csv). ***Citation:***
  - Available at: [UCI Machine Learning Repository - Algerian Forest Fires Dataset](https://archive.ics.uci.edu/ml/datasets/Algerian+Forest+Fires+Dataset++#)
  - Source:
    - Faroudja ABID, fabid@cdta.dz, abidfaroudja@gmail.com, Microelectronic & Nanotechnology Division, Center for Development of Advanced Technologies (CDTA).
  - Relevant Papers:
    - Faroudja ABID et al., Predicting Forest Fire in Algeria using Data Mining Techniques: Case Study of the Decision Tree Algorithm, International Conference on Advanced Intelligent Systems for Sustainable Development (AI2SD 2019) , 08 - 11 July, 2019, Marrakech, Morocco.

## Model

Please visit the [model notebook](src/model/model.ipynb) for more information.  

The model is to predict the likelihood of forest fires using Tensorflow and Keras in Python. The model takes in temperature in Celsius, relative humidity as a percentage, wind speed in Kilometers per hour, and rain size in millimeters as input, and outputs a probability score between 0 and 1 indicating the likelihood of a forest fire. The model is trained on historical forest fire data, optimized using the Adam optimizer, and has an early stopping criterion to prevent overfitting. The model is then saved as a .h5 file for use in the main program.

## Contributing

If you want to contribute to this project, please follow the guidelines below:

1. Fork the repository
2. Create a new branch for your changes
3. Make your changes and commit them
4. Push the new branch to your fork
5. Submit a pull request

## License

This project is licensed under the GPL v3 license. See our [LICENSE](LICENSE) for more information.

## Credits

- [Valentina Banner](https://github.com/realhuman101) - *Co-creator*
- [Alicia Yuen](https://github.com/Alicia1234567891) - *Co-creator*
- [Maya Yan](https://github.com/mayahkg) - *Co-creator*

## Contact

- GitHub: [@realhuman101](https://github.com/realhuman101)
- Email: valentinavbanner@gmail.com

## Acknowledgments

We would like to thank the following people and organizations for their support and contributions to this project:

- [Valentina Banner](https://realhuman101.github.io/) for contributing code and ideas.
- [Alicia Yuen](https://github.com/Alicia1234567891) for contributing code and ideas.
- [Maya Yan](https://github.com/mayahkg) for contributing code and ideas.
- [CityU EE GEF](https://cityueegef.github.io/) for providing funding, opportunities and resources.

We are grateful for the support of CityU and for the contributions of everyone who has helped make this project what it is.
