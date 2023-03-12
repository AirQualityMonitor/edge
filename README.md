
![](icon.png)

This repository contains code and instructions for setting up an air quality monitor on a Raspberry Pi using FastAPI, Poetry, and Clean Architecture. The monitor can measure various pollutants and environmental factors and features real-time monitoring.

- [Requirements](#requirements)
- [Installation](#installation)

## Requirements
- [__Python__](https://www.python.org/)
- [__Poetry__](https://python-poetry.org/)

## Installation
```shell
$ poetry install
```

## Execution
Running the server on local machine
```shell
$ uvicorn main:app --reload --port 3740
```
Running tests
```shell
$ pytest
```
