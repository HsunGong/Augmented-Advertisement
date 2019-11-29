#!/bin/bash

stage=0 end_stage=-1
dataset=ade20k

encoder=resnet50dilated
decoder=ppm_deepsup
# http://sceneparsing.csail.mit.edu/model/pytorch/

model=$dataset-$encoder-$decoder
config=config/${model}.yaml

exp_dir=exp/${model}

test=false

img=../demo/4.png
# no change
result_dir=../demo
model_dir=$exp_dir/models

set -e
. env.sh && . utils/parse_options.sh
echo -e "${GREEN}Expr at $exp_dir${BLANK}"

# model configs(can not mix with --args)
args=(
    DIR $model_dir
    # under it is ADEChallengeData2016 folder
    DATASET.root_dataset data
    DATASET.list_train data/ADEChallengeData2016/training.odgt
    DATASET.list_val data/ADEChallengeData2016/validation.odgt
    MODEL.arch_decoder $decoder
    MODEL.arch_encoder $encoder
)

if [ $stage -le -1 ] && [ $end_stage -ge -1 ]; then
    echo -e "${GREEN}Load data of ADE20K${BLANK}"
    if ! [ -f data/ADEChallengeData2016.zip ]; then
        wget -O ./data/ADEChallengeData2016.zip http://data.csail.mit.edu/places/ADEchallenge/ADEChallengeData2016.zip
    fi
    unzip ./data/ADEChallengeData2016.zip -d ./data
    # rm ./data/ADEChallengeData2016.zip
    echo "Dataset downloaded."
fi

if [ $stage -le 0 ] && [ $end_stage -ge 0 ]; then
    echo -e "${GREEN}Training NN${BLANK}"
    python scripts/train.py --cfg $config \
        ${args[*]}
fi

if [ $stage -le 1 ] && [ $end_stage -ge 1 ]; then
    echo -e "${GREEN}Eval model${BLANK}"
    python3 scripts/eval_multipro.py --cfg $config \
        ${args[*]}
fi
# munster_000005_000019_leftImg8bit
if [[ $stage -le 2 && $end_stage -ge 2 ]] || [ $test = true ]; then
    echo -e "${GREEN}Test File${BLANK}"
    python3 -u scripts/test.py --cfg $config \
        --imgs $img \
        TEST.checkpoint epoch_20.pth \
        TEST.result $result_dir \
        ${args[@]}
fi

if [ $stage -le 0 ] && [ $end_stage -ge 0 ]; then
    echo -e "${GREEN}FineTune Model${BLANK}"
fi
