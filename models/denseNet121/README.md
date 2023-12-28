# Infant Cry Classification DenseNet121 Model

# Overview
This repository contains a DenseNet121 model for classifying infant cry sounds. The model achieved an accuracy of 84.351% on the test dataset, showcasing its ability to capture intricate features of infant cry patterns.

# Model Architecture
DenseNet121 is a dense convolutional network that connects each layer to every other layer in a feed-forward fashion. It features densely connected blocks and alleviates the vanishing-gradient problem.


Model: "densenet121"
__________________________________________________________________________________________
Layer (type)                    Output Shape         Param #     Connected to
==========================================================================================
input_1 (InputLayer)            [(None, 224, 224, 3) 0
__________________________________________________________________________________________
zero_padding2d (ZeroPadding2D)  (None, 230, 230, 3)  0           input_1[0][0]
__________________________________________________________________________________________
conv1/conv (Conv2D)             (None, 112, 112, 64 9472        zero_padding2d[0][0]
...
__________________________________________________________________________________________
dense_3 (Dense)                 (None, 1)            1025        dense_2[0][0]
==========================================================================================
Total params: 8,062,849
Trainable params: 7,979,201
Non-trainable params: 83,648

# Dataset
The model was trained on a diverse dataset containing recordings of infant cry sounds. The dataset includes various cry patterns and non-cry sounds to ensure robust classification.

# Training
The DenseNet121 model was trained using TensorFlow and Keras with an Adam optimizer. The training process involved data augmentation techniques to enhance model generalization. The training accuracy reached 89%, while the validation accuracy reached 87%.

# Evaluation
The model achieved an accuracy of 84.351% on the test dataset, highlighting its ability to accurately classify infant cry sounds. The model's precision, recall, and F1-score metrics are notable.

# Usage
To use the trained DenseNet121 model for inference, you can load the model weights using the provided script:


python load_densenet121_model.py --weights path/to/densenet121_weights.h5 --audio path/to/test_audio.wav
Replace path/to/densenet121_weights.h5 with the path to the saved model weights and path/to/test_audio.wav with the path to the audio file you want to classify.

# Acknowledgments
I would like to express my gratitude to the contributors and data providers who made this project possible.

