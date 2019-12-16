#!/bin/bash
set -e
. env.sh
seg=false
dep=false
plane1=false
plane2=false
intersect=false
track=false
insert=false
placement=false

seg=true
dep=true
plane2=true
intersect=true
# placement=true
# insert=true

img_dir=$(pwd)/demo/img
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
    echo "Start Plane RCNN"
    python evaluate.py --methods=f --suffix=warping_refine --dataset=inference \
        --customDataFolder=tmp --test_dir=tmp
    mv tmp $img_dir/rcnn
    cd ../..
fi

if [ $intersect = true ]; then
    rm -rf $img_dir/intersect
    mkdir -p $img_dir/intersect
    python utils/intersection.py --pic1 $img_dir/sem_seg --pic2 $img_dir/rcnn/seg --dir $img_dir/intersect
fi

if [ $placement = true ]; then
    python utils/read_graph.py $img_dir
    ./utils/plane $img_dir
fi

if [ $insert = true ]; then
    python utils/utils.py $img_dir
fi
