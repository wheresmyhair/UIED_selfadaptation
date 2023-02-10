# UIED - UI element detection, detecting UI elements from UI screenshots or drawnings

An adaptation version of UIED.

## Related Works
[1. UIED: a hybrid tool for GUI element detection](https://dl.acm.org/doi/10.1145/3368089.3417940)

[2. Object Detection for Graphical User Interface: Old Fashioned or Deep Learning or a Combination?](https://arxiv.org/abs/2008.05132)

## Future works may be based on...
[1. (Blog) Understanding User Interfaces with Screen Parsing](https://blog.ml.cmu.edu/2021/12/10/understanding-user-interfaces-with-screen-parsing/)
[2. Screen Parsing: Towards Reverse Engineering of UI Models from Screenshots](https://dl.acm.org/doi/10.1145/3472749.3474763)[local link](./data/__papers/Screen%20Parsing%20-%20Towards%20Reverse%20Engineering%20of%20UI%20Models%20from%20Screenshots.pdf)

## What is it?

UI Element Detection (UIED) is an old-fashioned computer vision (CV) based element detection approach for graphic user interface. 

The input of UIED could be various UI image, such as mobile app or web page screenshot, UI design drawn by Photoshop or Sketch, and even some hand-drawn UI design. Then the approach detects and classifies text and graphic UI elements, and exports the detection result as JSON file for future application. 

UIED comprises two parts to detect UI text and graphic elements, such as button, image and input bar. 
* For text, it leverages existing OCR model to perfrom detection. 

* For graphical elements, it uses old-fashioned CV approaches to locate the elements and a CNN classifier to achieve classification. 

> UIED is **highly customizable**, you can replace both parts by your choice (e.g. other text detection approaches). Unlike black-box end-to-end deep learning approach, you can revise the algorithms in the non-text detection and merging (partially or entirely) easily to fit your task.

![UIED Approach](./data/demo/approach.png)

## How to use?
### Dependencies

### Installation

### Usage
To test your own image(s):
* To test single image, change *input_path_img* in ``run_single.py`` to your input image and the results will be output to *output_root*.
* To test mutiple images, change *input_img_root* in ``run_batch.py`` to your input directory and the results will be output to *output_root*.
* To adjust the parameters lively, using ``run_testing.py`` 

> Note: The best set of parameters vary for different types of GUI image (Mobile App, Web, PC). I highly recommend to first play with the ``run_testing.py`` to pick a good set of parameters for your data.
   
## Folder structure
``cnn/``
* Used to train classifier for graphic UI elements
* Set path of the CNN classification model

``config/``
* Set data paths 
* Set parameters for graphic elements detection

``data/``
* Input UI images and output detection results

``detect_compo/``
* Non-text GUI component detection

``detect_text/``
* GUI text detection using Google OCR

``detect_merge/``
* Merge the detection results of non-text and text GUI elements

The major detection algorithms are in ``detect_compo/``, ``detect_text/`` and ``detect_merge/``

## Demo
![UIED Demo](./data/demo/demo.png)

