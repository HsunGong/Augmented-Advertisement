#!/bin/bash

set -e
. ../../env.sh

python evaluate.py --methods=f --suffix=warping_refine --dataset=inference --customDataFolder=example_images --test_dir=example_images/output


