#!/bin/bash

# Image and model names
TEST_IMG=ADE_val_00001519.jpg
MODEL_PATH=ade20k-resnet50dilated-ppm_deepsup
RESULT_PATH=./

ENCODER=$MODEL_PATH/encoder_epoch_20.pth
DECODER=$MODEL_PATH/decoder_epoch_20.pth



# Inference
python3 -u scripts/test.py \
  --imgs exp/ade20k-resnet50dilated-ppm_deepsup/results/ADE_val_00001519.jpg \
  --cfg config/ade20k-resnet50dilated-ppm_deepsup.yaml \
  DIR exp/ade20k-resnet50dilated-ppm_deepsup/models \
  TEST.result ./exp/ade20k-resnet50dilated-ppm_deepsup/results \
  TEST.checkpoint epoch_20.pth
