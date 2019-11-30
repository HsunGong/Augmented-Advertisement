#!/bin/bash
set -e
. env.sh
seg=false
dep=false
plane1=false
plane2=false
seg=true
dep=true
plane2=true

for i in {11..17}; do
    img_dir=$(pwd)/demo/split/$i
    if [ $seg = true ]; then
        cd semseg # has subfolder as sem_seg
        bash ./run.sh --stage 2 --end_stage 2 --result_dir $img_dir --img $img_dir/img.png
        cd ..
    fi
    if [ $dep = true ]; then
        cd depth
        python demo.py --demo $img_dir/img.png
        cd ..
    fi
    if [ $plane1 = true ]; then
        cd plane/PlanarReconstruction
        python predict.py with resume_dir=checkpoint/pretrained.pt image_path=$img_dir/img.png
        cd ../..
    fi
    if [ $plane2 = true ]; then
        rm -rf $img_dir/rcnn # has sub folder as sem_seg
        cd plane/planercnn
        rm -rf tmp && mkdir tmp
        cp $img_dir/img.png $(pwd)/tmp/img.png
        python prepare.py tmp/img.png tmp/img.txt
        python evaluate.py --methods=f --suffix=warping_refine --dataset=inference \
            --customDataFolder=tmp --test_dir=tmp
        mv tmp $img_dir/rcnn
        cd ../..
    fi
done
