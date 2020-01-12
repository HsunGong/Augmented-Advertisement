# End-to-End Texture-Aware and Depth-Aware Embedded Advertising for Videos

## Content

   * [End-to-End Texture-Aware and Depth-Aware Embedded Advertising for Videos](#end-to-end-texture-aware-and-depth-aware-embedded-advertising-for-videos)
      * [Abstract](#abstract)
      * [Author](#author)
      * [Introduction](#introduction)
      * [License](#license)

## Abstract

The number of online videos is increasing rapidly with the prosperity of advertising market. To dig out the immense potential of videos, there are mainly two advertising types for commercial usage, mid-roll and embedded.  Embedded advertisements, compared with mid-roll ones, is an imperceptible and brilliant strategy. However once the video is produced, the advertisement embedded in it is nonchangeable, which causes out-of-date advertisements or personalized advertising difficulty. Meanwhile, the trade-off among video webs' income, video shooters' production difficulty and video watchers' aesthetic taste remains as a challenge with previous advertising strategies. To solve the problems above, we propose a pipeline that automatically embeds advertisements in real-time into a monocular RGB video or a single RGB image. The pipeline detects a non-intrusive region with awareness of texture and depth, and overlays it with an advertisement. A corner-based tracker is built to preserve 3D shape information of the candidate region, which makes the embedded advertisement natural. The pipeline runs a shoot change detector in parallel to keep advertisement visible on the main scene.

![pipeline1](pipeline1.png)


## Author

<center class="half">
<img src='gongxun.jfif' width="200" alt="Xun Gong" /> <img src='lijiasen.jfif' width="200" alt="Xun Gong" />  <img src='liboning.jfif' width="200" alt="Xun Gong" />
</center>


## Introduction

Use this pipeline, one can embed a rectangle-like advertisement in a video without any difficulty.

- Code is available on `Github`: [https://github.com/HsunGong/Augmented-Advertisement](https://github.com/HsunGong/Augmented-Advertisement)

- Paper is available on `Readme.md`: [https://github.com/HsunGong/Augmented-Advertisement/blob/master/README.md](https://github.com/HsunGong/Augmented-Advertisement/blob/master/README.md)

- Demo Video:
    - A `demo` can be seen [here](https://www.youtube.com/watch?v=6h5ptSp3lbY) at youtube.com.

<a href="https://youtu.be/6h5ptSp3lbY"><img src='maxresdefault.jpg' alt="Xun Gong" /></a>

## License

Our Paper is licensed under the MIT license [https://opensource.org/licenses/MIT](https://opensource.org/licenses/MIT).

