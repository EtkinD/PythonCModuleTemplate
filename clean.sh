#!/bin/bash

rm -rf build
rm -rf dist
rm -rf *.egg-info
rm -rf venv
# __pycache__ directories:
find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf
