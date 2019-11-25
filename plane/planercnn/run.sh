#!/bin/bash

set -e
. ../../env.sh

rm -rf tmp
mkdir tmp

cp ../../demo/4.png `pwd`/tmp

python prepare.py tmp/4.png tmp/4.txt

python evaluate.py --methods=f --suffix=warping_refine --dataset=inference \
        --customDataFolder=tmp --test_dir=tmp

mv tmp ../../demo/rcnn