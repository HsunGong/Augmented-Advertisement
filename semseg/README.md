## [Semantic Segmentation on MIT ADE20K dataset in PyTorch](https://github.com/CSAILVision/semantic-segmentation-pytorch)

### Supported models

Split our models into encoder and decoder, where encoders are usually modified directly from classification networks, 
and decoders consist of final convolutions and upsampling. We have provided some pre-configured models in the ```config``` folder.

<details>
<summary>Encoder-Decoder Models</summary>
<p class="has-line-data" data-line-start="0" data-line-end="1">Encoder:</p>
<ul>
<li class="has-line-data" data-line-start="1" data-line-end="2">MobileNetV2dilated</li>
<li class="has-line-data" data-line-start="2" data-line-end="3">ResNet18/ResNet18dilated</li>
<li class="has-line-data" data-line-start="3" data-line-end="4">ResNet50/ResNet50dilated</li>
<li class="has-line-data" data-line-start="4" data-line-end="5">ResNet101/ResNet101dilated</li>
<li class="has-line-data" data-line-start="5" data-line-end="6">HRNetV2 (W48)</li>
</ul>

<p class="has-line-data" data-line-start="0" data-line-end="1">Decoder:</p>
<ul>
<li class="has-line-data" data-line-start="1" data-line-end="2">C1 (one convolution module)</li>
<li class="has-line-data" data-line-start="2" data-line-end="3">C1_deepsup (C1 + deep supervision trick)</li>
<li class="has-line-data" data-line-start="3" data-line-end="4">PPM (Pyramid Pooling Module, see <a href="https://hszhao.github.io/projects/pspnet">PSPNet</a> paper for details.)</li>
<li class="has-line-data" data-line-start="4" data-line-end="5">PPM_deepsup (PPM + deep supervision trick)</li>
<li class="has-line-data" data-line-start="5" data-line-end="6">UPerNet (Pyramid Pooling + FPN head, see <a href="https://arxiv.org/abs/1807.10221">UperNet</a> for details.)</li>
</ul>
</details>

### FineTune

modified Dataset

retraining

##  