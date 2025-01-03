# FIFA players prices documentation!

## Description

And end-to-end ML project to predict the prices of football players using data from FIFA (FC Sports) videogames. The goal is to showcase the MLOps lifecycle using Microsoft Azure.

## Commands

The Makefile contains the central entry points for common tasks related to this project.

### Syncing data to cloud storage

* `make sync_data_up` will use `az storage blob upload-batch -d` to recursively sync files in `data/` up to `azureml/data/`.
* `make sync_data_down` will use `az storage blob upload-batch -d` to recursively sync files from `azureml/data/` to `data/`.


