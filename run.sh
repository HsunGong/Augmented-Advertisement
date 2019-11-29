#!/bin/bash
set -e
. env.sh

for i in `ls $(pwd)/demo/split`; do
    img_dir=$(pwd)/demo/split/$i

    cd semseg
    . run.sh --stage 2 --end_stage 2 --result_dir $img_dir --img $img_dir/img.png
    cd ..

    cd depth
    python demo.py --demo $img_dir/img.png
    cd ..

    cd plane
    cd PlanarReconstruction
    python predict.py with resume_dir=checkpoint/pretrained.pt image_path=$img_dir/img.png
    cd ..

    cd planercnn
    rm -rf tmp && mkdir tmp
    cp $img_dir/img.png $(pwd)/tmp/4.png
    python prepare.py tmp/4.png tmp/4.txt
    python evaluate.py --methods=f --suffix=warping_refine --dataset=inference \
        --customDataFolder=tmp --test_dir=tmp
    mv tmp $img_dir/rcnn
    cd ..
    cd ..
done
