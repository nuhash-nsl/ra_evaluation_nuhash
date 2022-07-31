### Environment File
    environment.yml is the environment file.
### Required Packages For the Project
    keras==2.9.0
    keras_nightly==2.10.0.dev2022071707
    matplotlib==3.1.3
    numpy==1.21.6
    opencv_python==4.5.5.64
    packaging==20.1
    pandas==1.0.1
    Pillow==9.2.0
    scikit_image==0.16.2
    scikit_learn==1.1.1
    skimage==0.0
    tensorflow==2.9.1
    tf_nightly==2.10.0.dev20220717
### Synthetic Image Generation
    Here we have mnist data. I have concatenated the train and test set of mnist data and generated corresponding synthetic image data with Pillow. The dataset has mnist data as input and synthetic image as target.
    
### Dataset Split
    The data is splitted into train, validation and test set in 60-20-20 ratio.
### Model Description
    Here we have used convolutional autoencoder for the image generation from the dataset.
###  Training
    Run the train.py for training. The best model is saved in Model file and logs are also saved in logs file. 
### Evaluation
    Since we are applying image to image generation, for evaluation we have taken 2 methods
    1. Calculate MSE for the actual,predicted images.
    2. Calculate similarity for the actual, predicted images.
    MSE values are:
    MEAN SQUARED ERROR OF TRAIN SET: 0.00014171425
    MEAN SQUARED ERROR OF TEST SET: 0.0015053536
    MEAN SQUARED ERROR OF VALIDATION SET 0.0014947985
    
    For similarity check, if the actual and predicted images similarity is more than 80%, we have considered those images similar. Using similarity:
    Accuracy with similarity miss match TRAIN: 0.9986904761904762
    Accuracy with similarity miss match VALIDATION: 0.9879285714285714
    Accuracy with similarity miss match TEST: 0.9867142857142858
### Inference 
    In the inference script, if we input a path of image, it will generate the corresponding synthetic image from the best model.