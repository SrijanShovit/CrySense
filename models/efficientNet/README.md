# Infant Cry Classification EfficientNet Model

# Overview
This repository contains an EfficientNet model for classifying infant cry sounds. The model achieved an accuracy of 84.236% on the test dataset, demonstrating its efficiency in capturing intricate features of infant cry patterns.

# Model Architecture
The EfficientNet architecture is designed to provide a powerful yet lightweight model. It consists of multiple blocks with depthwise separable convolutions, allowing the model to learn complex patterns efficiently.

Model: "efficientnet_b0"
__________________________________________________________________________________________
Layer (type)                    Output Shape         Param #     Connected to
==========================================================================================
input_1 (InputLayer)            [(None, 224, 224, 3) 0
__________________________________________________________________________________________
rescaling (Rescaling)            (None, 224, 224, 3)  0           input_1[0][0]
__________________________________________________________________________________________
normalization (Normalization)    (None, 224, 224, 3)  7           rescaling[0][0]
__________________________________________________________________________________________
stem_conv_pad (ZeroPadding2D)   (None, 225, 225, 3)  0           normalization[0][0]
__________________________________________________________________________________________
stem_conv (Conv2D)              (None, 112, 112, 32 864         stem_conv_pad[0][0]
...
__________________________________________________________________________________________
dense (Dense)                   (None, 1)            257         top_dropout[0][0]
==========================================================================================
Total params: 4,049,825
Trainable params: 4,007,802
Non-trainable params: 42,023

# Dataset
The model was trained on a diverse dataset containing recordings of infant cry sounds. The dataset includes various cry patterns and non-cry sounds to ensure robust classification.

# Training
The EfficientNet model was trained using TensorFlow and Keras with an Adam optimizer. The training process involved data augmentation techniques to enhance model generalization. The training accuracy reached 88%, while the validation accuracy reached 86%.

# Evaluation
The model achieved an accuracy of 84.236% on the test dataset, showcasing its ability to efficiently classify infant cry sounds. The model's precision, recall, and F1-score metrics are also noteworthy.

# Usage
To use the trained EfficientNet model for inference, you can load the model weights using the provided script:

python load_efficientnet_model.py --weights path/to/efficientnet_weights.h5 --audio path/to/test_audio.wav
Replace path/to/efficientnet_weights.h5 with the path to the saved model weights and path/to/test_audio.wav with the path to the audio file you want to classify.

# Acknowledgments
I would like to express my gratitude to the maintainers  and data providers who made this project possible.
