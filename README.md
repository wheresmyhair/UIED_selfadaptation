# UIED - UI element detection, detecting UI elements from UI screenshots or drawnings

An adaptation version of UIED.

## Related Publications: 
[1. UIED: a hybrid tool for GUI element detection](https://dl.acm.org/doi/10.1145/3368089.3417940)

[2. Object Detection for Graphical User Interface: Old Fashioned or Deep Learning or a Combination?](https://arxiv.org/abs/2008.05132)

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



# automatedTest
## Introduction
对各测试记录截图进行文字与ui元素识别，配合测试中自动生成的记录信息，建立对应的操作行为知识图谱；
基于操作行为知识图谱，实现智能化测试用例构建：
- 一方面，将各应用总体结构图谱与操作行为图谱相结合，可对测试的应用覆盖度做出判断与推荐（推荐系统）；
- 长远来看，将测试用例需求文档与操作行为图谱相结合，可实现基于测试用例需求文档的自动化测试脚本生成（多模态任务）。
- 基于视觉的用户行为预测（测试人员是否做错了，是否是不合常理的行为）

## Timeline
## 2023
现存（以及可能新加入的）手机端app截图组（不论是哪个app）全部识别、入图，评估流程泛化性，并向电脑端迁移
### 23Q1
#### 1月
##### 1月计划
软件测试相关概念、问题澄清，共享空间建立，设备申请等
模型、流程解耦（主要是视觉方面）
分工：
- 探索与收集外部数据集、现有解决方案，形成简报
- 调用ocr，分析文字识别结果，先实现规则过滤出可点击文字
- 图谱建立的伪代码、逻辑（部分代码）
- 0203进行月度总结

##### 1月回顾
- uied pipeline
  - ocr
  - cv
    - 传统cv
    - yolo模型训练（rico数据集）、预测结果
- 图谱代码完成、使用模拟json文件完成测试

##### 待解决问题
- 大框架已有，需要确定优化细节
  - uied代码逻辑拆解->他是怎么融合框体的，我们需要做什么改进（可能涉及很多小算法、规则，b-v取舍（算法+应用特制参数？））
  - ui元素：yolo->素材库问题，能否拿到自己的ui元素、美术资源（等汇报后领导反馈）
  - 文字：如何确定文字是否可点击，是否需要联动附近图标判断，或者引入模型？（确定模型输入要包含什么（相对位置信息+周围图标信息+文本？））

- 确定兜底产出
  - 已跟领导提出是否存在撞车问题，等反馈（推荐覆盖度）
  - 能走到汇报文档中的哪一步
    - 推荐系统概念、设计，需要做哪些准备
    - 依据什么、推荐什么

- 环境
  - 可能DMZ
  - 配置难度如何

- 项目组织方面
  - 汇报当周周二下班前总结一下进度，汇总
  - 碰头频率？

- 2月进度安排和分工
- 其他？

开发应该是有每个页面应包括什么的规范吧？

组成结构图
结构之间的关联

专利
yolo在所有图片中识别一次
优化rico

源码读取ui元素位置：相当于前端代码+前端页面进行分析，直接形成图（或进行页面打标，用作yolo训练数据集）
redraw 11w 21个类别有图标没位置->切片？


同样的元素在不同图片中 识别率不同
哪里可以点击 开发有记录（代码分析）




P1：
我行各平台百余个应用的测试建模均由人工完成。需求编写人员需要投入大量精力和时间以理解应用中各个可视元素的功能；同时，人的视角通常聚集在某一功能的测试，缺少全局视野，对应用的测试覆盖率产生潜在影响。放眼软件测试业界，目前尚未有基于黑盒视角进行测试模型自动构建的框架。现存的基于白盒视角（代码分析）的测试模型自动构建工具，与中心测试任务契合度不高，且测试人员学习成本极高。

基于图模型的测试模型构建技术从黑盒视角出发，运用计算机视觉技术识别我行测试截图记录中的按钮、文本提示等UI元素，依此形成测试轨迹图谱，并根据图谱中的各条路径实现自动化构建测试模型，以提高测试效率和测试实际覆盖度。


P2：流程与架构模块

P3：现阶段实验结果



P4：用途展望
- 构建智能测试
  - 对于可执行自动化测试的应用，依据推荐系统生成的测试模型构建自动化测试脚本，再通过自动化测试工具进行测试，并将测试结果继续反馈至推荐系统，形成闭环；
  - 对于暂无法执行自动化测试的应用，测试人员可依照推荐系统生成的测试模型进行测试，提高测试效率。
  
- 生成指定测试
  - 根据测试需求文档，直接构建测试模型。对于可执行自动化测试的应用，继续生成自动化测试脚本并执行。

- 提示测试步骤
  - 根据测试人员当前操作步骤，结合测试手册或需求文档，提示后续步骤、检验操作是否偏离原定测试目标。











#### 2
- 初步建模
  - 视觉方面：按钮识别与定位
  - 图谱方面：完成代码，用模拟的json完成测试
- 0303月度总结

#### 3
- 完成建模，根据真实json评估各模型效果
  - 文字：规则是否够用、是否需要NLP
  - 视觉：连续截图记录的过滤、弹窗处理
- 0331月度总结

## 23Q2
- 根据Q1进度动态调整
- 泛化性测试（在多组图片下是否表现良好）、迭代更新

## 23Q3
- 新人培训、现有成果（加贝7月交流结束/新人加入）
- 模型和流程泛化性达到要求，能把现存全部手机app截图组识别、入图

## 23Q4
- 电脑端迁移（可能24Q1+24Q2）

## related works
