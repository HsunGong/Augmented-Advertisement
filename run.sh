#! /bin/bash
# SBATCH

stage=0
end_stage=0

if [ $(hostname) = date ]; then
    source activate base
else
    source activate torch10
fi

if [ $stage -ge 0 ] && [ $end_stage -le 0 ]; then
    # sh semseg/train.sh voc2012 pspnet50
    sh semseg/train.sh ade20k pspnet50
    # sh tool/test.sh ade20k pspnet50
    # PYTHONPATH=./ python tool/demo.py --config=config/ade20k/ade20k_pspnet50.yaml --image=figure/demo/ADE_val_00001515.jpg TEST.scales '[1.0]'
    # tensorboard --logdir=run1:$EXP1,run2:$EXP2 --port=6789
fi
