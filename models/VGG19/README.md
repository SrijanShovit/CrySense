# Infant Cry Classification VGG19 Model

# Overview
This repository contains a VGG19 model for classifying infant cry sounds. The model achieved an accuracy of 87.431% on the test dataset, showcasing its effectiveness in capturing intricate features of infant cry patterns.

# Model Architecture
VGG19 is an extension of the VGG16 architecture, with additional convolutional and fully connected layers. It maintains a simple and uniform architecture throughout, making it a powerful tool for image classification tasks.

Model: "vgg19"
__________________________________________________________________________________________
Layer (type)                    Output Shape         Param #     Connected to
==========================================================================================
input_1 (InputLayer)            [(None, 224, 224, 3) 0
__________________________________________________________________________________________
block1_conv1 (Conv2D)           (None, 224, 224, 64) 1792        input_1[0][0]
...
__________________________________________________________________________________________
dense_3 (Dense)                 (None, 1)            513         dense_2[0][0]
==========================================================================================
Total params: 143,667,849
Trainable params: 143,667,849
Non-trainable params: 0

# Dataset
The model was trained on a diverse dataset containing recordings of infant cry sounds. The dataset includes various cry patterns and non-cry sounds to ensure robust classification.

# Training
The VGG19 model was trained using TensorFlow and Keras with an Adam optimizer. The training process involved data augmentation techniques to enhance model generalization. The training accuracy reached 92%, while the validation accuracy reached 90%.

# Evaluation
The model achieved an accuracy of 87.431% on the test dataset, highlighting its ability to accurately classify infant cry sounds. The model's precision, recall, and F1-score metrics are commendable.

# Usage
To use the trained VGG19 model for inference, you can load the model weights using the provided script:

python load_vgg19_model.py --weights path/to/vgg19_weights.h5 --audio path/to/test_audio.wav
Replace path/to/vgg19_weights.h5 with the path to the saved model weights and path/to/test_audio.wav with the path to the audio file you want to classify.

# Acknowledgments
I would like to express my gratitude to the contributors and data providers who made this project possible.
