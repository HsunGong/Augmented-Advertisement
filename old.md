## Brief Info

Virtual advertisement insertion / Overlay advertising / Augmented reality

->>>> live broadcast

constrain the advertisement to be placed in a way that is aesthetic and natural.

After successful placement in a
single frame, we use homography-based, shape-preserving tracking such
that the advertisement appears perspective correct for the duration of a video clip.

augmentation has a minimal impact on the viewing experience

Or anti-"adblocker"

In this work, we identify
“virtual real estate” as the crowded sections of a sporting arena and use those
regions for asset insertion.

We argue that the latter are good candidates for asset
placement because they are of less relevance to the focus of the broadcast

1. Automatically identifies viable “crowd” regions through spatio-temporal analysis
in a video clip
2. Places the asset in a “natural” fashion, respecting the physical constraints of
the real world scene
3. Is fully automatic
   

Various systems and pipelines have been proposed for the insertion of assets
in video
The asset should be apparent but not disruptive
ImageSence solves this problem by choosing insertion content according
to visual consistency.

define intrusiveness as follows: (a) if the inserted asset covers the Region of
Interest (ROI), it is truly very intrusive, and (b) if the asset distracts audience
attention from the original attending point, it is also very intrusive.


constraining the
overlaid asset to the physical boundaries of the real world scene

Our biggest challenge was to achieve the goal of virtual asset placement in
compliance with the conditions of (a) non-intrusiveness, and (b) conformity to
real world scene constraints, while requiring minimal manual intervention

advertisers hire professional editors to manually implement virtual ads


## EXPR SETUP

### Setup

– the input video is captured from a single viewpoint with a monocular RGB
camera
– intrinsic parameters about the camera may not be known
– the texture we aim to overlay on will be a crowd of people in a sports stadium
– the asset to be overlayed in the video will be a 2D image/video and not a 3D
object
– the shot need not be static, i.e., the camera may change location or angle
– the video may contain multiple camera shots

### Segmentation and Seed Frame Selection

#### the most ideal frame

Once this frame is determined, we track
our asset through subsequent frames.

contains the texture of interest(e.g. crowds in sport stadium imagery)
the textured area is large enough

sample the video at
one frame per second and only segment those frames.

discontinue segmentation until tracking fails

####  Semantic segmentation
Pyramid Scene Parsing network on ADE20K ->>>> our textures of choice: “person” and “grandstand”. this combination of classes as “crowd”.

alleviate computation time?

#### Measuring Segmentation Quality

the segmentation mask can be far
from ideal, containing holes, fragmentation etc.

(a) the
asset only covers the crowd region of the image and (b) the crowd region of the
image is large enough

an ideally segmented region to
be one
Is connected
Contains no holes
Is compact
Is readable?

SQS = Scp Scl Ssp, Scp is the component score, Ssp is the completeness score and Ssp is the shape score. minimum possible SQS score is 1.

For some frames with small SQS, the detected crowd area is significantly
small.

finds the maximum detected
crowd area, then disregards all frames with detected crowd area less than the
half of the maximum area.

The frame with the lowest SQS (Eq. 1) is then chosen