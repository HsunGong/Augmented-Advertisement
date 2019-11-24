#!/bin/bash

set -e
. ../../env.sh

python predict.py with resume_dir=checkpoint/pretrained.pt image_path=../../demo/4.png
