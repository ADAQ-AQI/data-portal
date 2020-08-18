# dataportal
Data Portal framework

## Setup

Setup is as simple as creating the `dataportal` conda environment:
```bash
conda env create -f environment.yaml
```
This environment contains packages both for building and running the Portal,
and for interacting directly with data.

Jupyter is included, but if working with an existing Jupyter environment -
such as the [Clean Air Pangeo][ca-pangeo] - remember that the `dataportal`
environment can be made available to any instance of Jupyter by running
```bash
conda activate dataportal
python -m ipykernel install --user --name dataportal
```

Note that access to the [Clean Air Pangeo][ca-pangeo] is determined by being
a member of the [clean-air-pangeo][ca-pangeo-group] GitHub organisation.

## Usage

A Jupyter session can be started with either
```bash
jupyter notebook
# or
jupyter lab
```
depending on preference.

The portal can be built with
```bash
./build.sh path/to/htmldir
```


[ca-pangeo]: https://clean-air.informaticslab.co.uk/hub/login
[ca-pangeo-group]: https://github.com/clean-air-pangeo
