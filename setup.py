from setuptools import setup, find_packages

setup(
    name         = 'Kheiron_Calculator',
    version      = '0.1',
    packages     = find_packages(),
    entry_points = {'console_scripts': ['kheiron_calc = calculators.calculators:calc', 'kheiron_calc_app = calculator_app.app:launch']},
)