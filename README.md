# Kheiron Test: Prefix & Infix Calculator

This package provides calucation functions in prefix and infix format.

## Prerequisites

* Python >= 3.7.9
* flask >= 1.1.2


## Getting Started

### Installation
`
pip install git+https://github.com/yuan1202/kheiron_calculator.git
`

### Usage

After installation, the package can be used as follows:

- Run prefix calculation\
`
kheiron_calc '- / 10 + 1 1 * 1 2'
`  
or  
`
kheiron_calc -m prefix '- / 10 + 1 1 * 1 2'
`  

- Run infix calculation  
`
kheiron_calc -m infix "( 3 + 3 ) * 10"
`  

- Run unit tests  
Firstly run  
`
git clone https://github.com/yuan1202/kheiron_calculator.git
`  
to copy the repository to local directory.  
Then navigate into the repository folder and run  
`
python -m unittest
`  
to run unit test cases.

- Launch calucaltion app
`
kheiron_calc_app
`  
The *restAPI.ipynb* provides demonstrations/tests of kheiron_calc_app rest api call.