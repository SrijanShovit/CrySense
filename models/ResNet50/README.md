# Infant Cry Classification ResNet50 Model

# Overview
This repository contains a ResNet50 model for classifying infant cry sounds. The model achieved an accuracy of 84.273% on the test dataset, showcasing its ability to capture intricate features of infant cry patterns.

# Model Architecture
The ResNet50 architecture is designed to facilitate training of very deep networks. It includes residual blocks that enable the training of deeper networks without the vanishing gradient problem.


Model: "resnet50"
__________________________________________________________________________________________
Layer (type)                    Output Shape         Param #     Connected to
==========================================================================================
input_1 (InputLayer)            [(None, 224, 224, 3) 0
__________________________________________________________________________________________
conv1_pad (ZeroPadding2D)       (None, 230, 230, 3)  0           input_1[0][0]
__________________________________________________________________________________________
conv1_conv (Conv2D)             (None, 112, 112, 64 9472        conv1_pad[0][0]
...
__________________________________________________________________________________________
dense_3 (Dense)                 (None, 1)            2049        global_average_pooling2d_1[0][0]
==========================================================================================
Total params: 23,587,713
Trainable params: 23,534,593
Non-trainable params: 53,120

# Dataset
The model was trained on a diverse dataset containing recordings of infant cry sounds. The dataset includes various cry patterns and non-cry sounds to ensure robust classification.

# Training
The ResNet50 model was trained using TensorFlow and Keras with an Adam optimizer. The training process involved data augmentation techniques to enhance model generalization. The training accuracy reached 90%, while the validation accuracy reached 88%.

# Evaluation
The model achieved an accuracy of 84.273% on the test dataset even though dataset is bit imbalanced, highlighting its ability to accurately classify infant cry sounds. The model's precision, recall, and F1-score metrics are commendable.

# Usage
To use the trained ResNet50 model for inference, you can load the model weights using the provided script:


python load_resnet50_model.py --weights path/to/resnet50_weights.h5 --audio path/to/test_audio.wav
Replace path/to/resnet50_weights.h5 with the path to the saved model weights and path/to/test_audio.wav with the path to the audio file you want to classify.

# Acknowledgments
I would like to express our gratitude to the Maintainers and data providers who made this project possible.
