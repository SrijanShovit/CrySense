# Infant Cry Classification VGG16 Model

# Overview
This repository contains a VGG16 model for classifying infant cry sounds. The model achieved an accuracy of 84.593% on the test dataset, demonstrating its effectiveness in capturing intricate features of infant cry patterns.

# Model Architecture
VGG16 is a convolutional neural network architecture that gained popularity for its simplicity and effectiveness. It comprises multiple convolutional and max-pooling layers, followed by fully connected layers.

Model: "vgg16"
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
Total params: 138,357,513
Trainable params: 138,357,513
Non-trainable params: 0

# Dataset
The model was trained on a diverse dataset containing recordings of infant cry sounds. The dataset includes various cry patterns and non-cry sounds to ensure robust classification.

# Training
The VGG16 model was trained using TensorFlow and Keras with an Adam optimizer. The training process involved data augmentation techniques to enhance model generalization. The training accuracy reached 91%, while the validation accuracy reached 89%.

# Evaluation
The model achieved an accuracy of 84.593% on the test dataset, showcasing its ability to accurately classify infant cry sounds. The model's precision, recall, and F1-score metrics are impressive.

# Usage
To use the trained VGG16 model for inference, you can load the model weights using the provided script:

python load_vgg16_model.py --weights path/to/vgg16_weights.h5 --audio path/to/test_audio.wav
Replace path/to/vgg16_weights.h5 with the path to the saved model weights and path/to/test_audio.wav with the path to the audio file you want to classify.

# Acknowledgments
I would like to express my gratitude to the contributors and data providers who made this project possible.
