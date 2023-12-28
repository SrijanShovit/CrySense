# Infant Cry Classification CNN Model

# Overview
This notebook contains a Convolutional Neural Network (CNN) model for classifying infant cry sounds. The model achieved an impressive accuracy of 85.712% on the test dataset, demonstrating its effectiveness in distinguishing different cry patterns.

# Model Architecture
The CNN architecture is designed to capture intricate features in infant cry sounds. The model comprises convolutional layers, max-pooling layers, dropout layers, and fully connected layers. The architecture is optimized for learning complex patterns in the audio data.


Layer (type)                Output Shape         Param #
=======================================================
conv2d (Conv2D)             (None, 64, 64, 64)   1792
_______________________________________________________
max_pooling2d (MaxPooling2D)(None, 32, 32, 64)   0
_______________________________________________________
conv2d_1 (Conv2D)           (None, 30, 30, 128)  73856
_______________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 15, 15, 128)  0
_______________________________________________________
flatten (Flatten)           (None, 28800)        0
_______________________________________________________
dense (Dense)               (None, 256)          7373056
_______________________________________________________
dropout (Dropout)           (None, 256)          0
_______________________________________________________
dense_1 (Dense)             (None, 1)            257
=======================================================
Total params: 7,447,961
Trainable params: 7,447,961
Non-trainable params: 0

# Dataset
The model was trained on a diverse dataset containing recordings of infant cry sounds. The dataset includes various cry patterns and non-cry sounds to ensure robust classification.

# Training
The model was trained using TensorFlow and Keras with an Adam optimizer. The training process involved data augmentation techniques to enhance model generalization. The training accuracy reached 90%, while the validation accuracy reached 88%.

# Evaluation
The model achieved an accuracy of 85.712% on the test dataset, showcasing its ability to accurately classify infant cry sounds. The model's precision, recall, and F1-score metrics are also impressive.

#Usage
To use the trained model for inference, you can load the model weights using the provided script:

python load_model.py --weights path/to/weights.h5 --audio path/to/test_audio.wav
Replace path/to/weights.h5 with the path to the saved model weights and path/to/test_audio.wav with the path to the audio file you want to classify.

# Acknowledgments
I would like to express my gratitude to the maintainer and data providers who made this  possible.
