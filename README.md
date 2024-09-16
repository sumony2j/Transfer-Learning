# Yoga Pose Classification Using Transfer Learning

## Overview
Yoga is a practice that originated in ancient India, aimed at balancing the mind and body through meditation, exercise, and regulated breathing. Hatha Yoga, a type of physical yoga, consists of postures (asanas) performed in a continuous sequence. Correct identification of yoga poses is essential to ensure proper practice and alignment with individual needs.

This repository provides an implementation of yoga pose classification from images using a transfer learning approach. The model classifies yoga poses from images of five different asanas, leveraging pre-trained deep learning models to achieve high accuracy.

## Summary
In this project, a total of 1551 images representing 5 distinct yoga postures were used. The images were resized to optimize computation. Transfer learning was employed, utilizing 10 different pre-trained models for classification.

## Dataset
- **Total Images**: 1551
- **Yoga Poses**: 5 distinct yoga asanas
- **Image Preprocessing**: All images were resized for consistency and computational efficiency.

## Models
The following pre-trained models from popular deep learning architectures were used for classification:
1. **VGG16**
2. **VGG19**
3. **InceptionV3**
4. **DenseNet201**
5. **ResNet50V2**
6. **ResNet101V2**
7. **ResNet152V2**
8. **MobileNet**
9. **MobileNetV2**
10. **InceptionResNetV2**

### Best Model
- **VGG16** performed the best with a validation accuracy of **94.47%**.

## Requirements

To replicate the results, you will need the following libraries:
- TensorFlow
- Keras
- NumPy
- seaborn
- Matplotlib (for visualizations)
- Scikit-learn (for model evaluation metrics)

You can install the dependencies by running:

```bash
pip install -r requirements.txt
```
## Implementation
follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/sumony2j/Transfer-Learning.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Transfer-Learning
    ```
3. The Dataset is in /Data directory in zip format (Yoga_New_Dataset_Resized.zip)
4. Navigate to the Code implementation directory:
    ```bash
    cd Implementation
    ```
## Results
- **VGG16** achieved the highest accuracy of **94.47%** on the validation set.
- Model performance metrics (accuracy, precision, recall, F1-score) will be printed for each model.

## Research Paper
This repository contains the implementation of my published research paper on **Yoga Pose Classification Using Transfer Learning**. The paper presents a comparative analysis of 10 different deep learning models for classifying yoga poses from images.

For more details, you can refer to the published paper:

- **Title**: Yoga Pose Classification Using Transfer Learning
- **Author**: Sumon Singh,Deepali Handgar
- **Published In**: International Journal of Innovative Research in Technology (https://ijirt.org/Article?manuscript=167821)
- **DOI/Link**: https://ijirt.org/publishedpaper/IJIRT167821_PAPER.pdf


## Future Work
- **Fine-tuning**: Fine-tune pre-trained models on the yoga dataset for improved performance.
- **Additional Poses**: Expand the dataset to include more yoga poses.

## Acknowledgments
We would like to thank the open-source community for providing pre-trained models and tools that made this project possible.



