# gendiff
[![Actions Status](https://github.com/illata1998/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/illata1998/python-project-50/actions) [![Python CI](https://github.com/illata1998/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/illata1998/python-project-50/actions/workflows/pyci.yml) <a href="https://codeclimate.com/github/illata1998/python-project-50/maintainability"><img src="https://api.codeclimate.com/v1/badges/841642d2ab5606d50523/maintainability" /></a> <a href="https://codeclimate.com/github/illata1998/python-project-50/test_coverage"><img src="https://api.codeclimate.com/v1/badges/841642d2ab5606d50523/test_coverage" /></a>

## Description
Console application that compares two configuration files (JSON or YAML) and shows a difference.
## Installation
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install gendiff.
```bash
pip install --user git+https://github.com/illata1998/python-project-50.git
```
## Usage
```bash
#display the help message
gendiff -h

#compare two files using the default formatter
gendiff file1.json file2.json
gendiff -f stylish file1.json file2.yml

#compare two files using other available formatters
gendiff -f plain file1.json file2.yaml
gendiff -f json file1.yaml file2.json
```
### Example 1: Display the help message
<a href="https://asciinema.org/a/d9gkDX2qskXiJpvFXSbVwkrpd" target="_blank"><img src="https://asciinema.org/a/d9gkDX2qskXiJpvFXSbVwkrpd.svg" /></a>
### Example 2: Compare two flat JSONs
<a href="https://asciinema.org/a/W11egoRzgNMiuJ84C3kipuQ74" target="_blank"><img src="https://asciinema.org/a/W11egoRzgNMiuJ84C3kipuQ74.svg" /></a>
### Example 3: Compare two flat YAMLs
<a href="https://asciinema.org/a/05qLbfR8ded6cXbEaQ8NMJMkp" target="_blank"><img src="https://asciinema.org/a/05qLbfR8ded6cXbEaQ8NMJMkp.svg" /></a>
### Example 4: Compare two files with nested structures using the default 'stylish' formatter
<a href="https://asciinema.org/a/P2VzGqPQ59R17LmFN1gN9Lx9F" target="_blank"><img src="https://asciinema.org/a/P2VzGqPQ59R17LmFN1gN9Lx9F.svg" /></a>
### Example 5: Compare two files with nested structures using the 'plain' formatter
<a href="https://asciinema.org/a/h1L6DzGFGHTqRsmdrfKsEK4QC" target="_blank"><img src="https://asciinema.org/a/h1L6DzGFGHTqRsmdrfKsEK4QC.svg" /></a>
### Example 6: Compare two files with nested structures using the 'json' formatter
<a href="https://asciinema.org/a/NMTKc9Hj254YEnTlErCtipRpx" target="_blank"><img src="https://asciinema.org/a/NMTKc9Hj254YEnTlErCtipRpx.svg" /></a>
