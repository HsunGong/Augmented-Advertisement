## sem-seg pspnet
https://github.com/CSAILVision/semantic-segmentation-pytorch

 bash run.sh --stage 2 --end_stage 2

## depth megadepth
https://github.com/zhengqili/MegaDepth

 py demo.py --demo ../demo/4.png

## plane

https://github.com/NVlabs/planercnn

module load gcc/5.4.0 cuda/9.0
nvcc -c -o nms_kernel.cu.o nms_kernel.cu -x cu -Xcompiler -fPIC

python evaluate.py --methods=f --suffix=warping_refine --dataset=inference --customDataFolder=example_images

https://github.com/svip-lab/PlanarReconstruction

cd ...
python predict.py with resume_dir=checkpoint/pretrained.pt image_path=../../demo/4.png