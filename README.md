### Hexlet tests and linter status:
[![Actions Status](https://github.com/amahmetov1998/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/amahmetov1998/python-project-50/actions)
[![run test and linter](https://github.com/amahmetov1998/python-project-50/actions/workflows/main.yml/badge.svg)](https://github.com/amahmetov1998/python-project-50/actions/workflows/main.yml)
[![Maintainability](https://api.codeclimate.com/v1/badges/1e04e557ed003ce6ff2c/maintainability)](https://codeclimate.com/github/amahmetov1998/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/1e04e557ed003ce6ff2c/test_coverage)](https://codeclimate.com/github/amahmetov1998/python-project-50/test_coverage)

<h2 align="center">Hexlet Project #2 – GenDiff</h2>

### Description

The program generates differences between JSON and YAML files.

### Installation

```
git clone https://github.com/amahmetov1998/python-project-50.git
make package-install
```
### Launching
#### help
```
gendiff -h
```
#### generate differences between plain JSON files
```
gendiff <file_path1> <file_path2>
```
<a href="https://asciinema.org/a/V5denz3SnfHF3pENj6dUx2sAN" target="_blank"><img src="https://asciinema.org/a/V5denz3SnfHF3pENj6dUx2sAN.svg" /></a>
#### generate differences between plain YAML files
```
gendiff <file_path1> <file_path2>
```
<a href="https://asciinema.org/a/AWADDMSTgQyL0IZyuwAYzBp5j" target="_blank"><img src="https://asciinema.org/a/AWADDMSTgQyL0IZyuwAYzBp5j.svg" /></a>
#### generate differences between nested JSON/YAML files
```
gendiff <file_path1> <file_path2>
```
<a href="https://asciinema.org/a/5hRFB1OZgv2xiZB1KjevERfpf" target="_blank"><img src="https://asciinema.org/a/5hRFB1OZgv2xiZB1KjevERfpf.svg" /></a>
#### Plain format of output
```
gendiff --format plain <file_path1> <file_path2>
```
<a href="https://asciinema.org/a/0TfjzQYBlK5gTGAdTv5ndn8Si" target="_blank"><img src="https://asciinema.org/a/0TfjzQYBlK5gTGAdTv5ndn8Si.svg" /></a>
#### JSON format of output
```
gendiff --format json <file_path1> <file_path2>
```
<a href="https://asciinema.org/a/ip3zFjOZVN9N1Ck0n1eiULY6o" target="_blank"><img src="https://asciinema.org/a/ip3zFjOZVN9N1Ck0n1eiULY6o.svg" /></a>