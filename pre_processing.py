# Import packages
import pandas as pd
from pathlib import Path
import shutil
import os
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from random import sample
import cv2
import numpy as np
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split
from skimage.feature import hog, local_binary_pattern
from sklearn.preprocessing import StandardScaler
from config import *


def data_preprocessing(data_directory, filename_column, target_column, training_percentage_size=0.85, batches_size=16,
                       validation_split=0.15, img_size=(96, 96), color_mode='rgb', horizontal_flip=True):
    """
        Whether a test dataset folder does not already exist, it divides the dataset in training and test sets .
        In the second part it prepares the training, validation and test batches.

        :param data_directory: name (not path) of the images folder.
        :param filename_column: name of the column in the csv file where all the related filenames are declared.
        :param target_column: name of the column in the csv file where the labels are declared.
        :param training_percentage_size: percentage size of the entire dataset dedicated to the training dataset.
            default_value=0.85.
        :param batches_size: dimension of every batch. default_value=16.
        :param validation_split: percentage size of the entire dataset dedicated to the validation set.
            default_value=0.15.
        :param img_size: size of images after the reshaping. default_value=(96,96).
        :param color_mode: state 'grayscale' if the images have only one channel. default_value='rgb'.
        :param horizontal_flip: state False if it is not desired images are randomly flipped. default_value=True.
        :return: the training, validation and test batches.
    """
    # Loading the csv file
    # The sep parameter chosen according to the delimiter adopted in labels.csv
    path = os.path.join(base_dir, data_directory)
    dataset_labels = pd.read_csv(os.path.join(path, labels_filename), sep='\t', dtype='str')
    # Divide data in two sets: one for training and one for testing
    training_dir = os.path.join(path, 'img')
    test_dir = os.path.join(path + '_testing', 'img')
    # Division will be made only if the testing directory does not already exist
    if not os.path.isdir(test_dir):
        # Create the Test dataset folder
        # If parents is True, any missing parents of the folder will be created
        # If exist_ok is True, an Error is not raised if the directory already exists
        Path(test_dir).mkdir(parents=True, exist_ok=True)
        # Sorted list of all the images available
        files = sorted(os.listdir(training_dir), key=lambda x: int(x.split(".")[0]))
        # Simple random sampling to select examples for the test dataset
        images_testing = sorted(sample(files, round(len(files) * (1 - training_percentage_size))))
        # Move all the test images into the related folder
        for file in images_testing:
            shutil.move(os.path.join(training_dir, file), test_dir)
    # List of all the images within the training and testing folders
    random_test_list = sorted([dataset_labels[dataset_labels[filename_column] == i].index[0]
                               for i in os.listdir(test_dir)])
    random_training_list = sorted([dataset_labels[dataset_labels[filename_column] == i].index[0]
                                   for i in os.listdir(training_dir)])

    # Prepare the training, test and validation batches
    # Select labels associated to the images inside the training and test folders
    training_labels = dataset_labels.iloc[[i for i in random_training_list]]
    test_labels = dataset_labels.iloc[[i for i in random_test_list]]
    # With the following line the validation_split passed as argument becomes equal to the percentage of the total
    # dataset (and not anymore to the percentage of the training dataset dedicated to the validation dataset)
    validation_split = validation_split / training_percentage_size
    # ImageDataGenerator generates batches of images with real-time data augmentation
    image_generator = ImageDataGenerator(rescale=1. / 255., validation_split=validation_split,
                                         horizontal_flip=horizontal_flip)
    # It produces batches of images everytime it is called
    training_batches = image_generator.flow_from_dataframe(dataframe=training_labels, directory=training_dir,
                                                           x_col=filename_column, y_col=target_column,
                                                           subset="training", batch_size=batches_size, seed=42,
                                                           color_mode=color_mode, shuffle=True, target_size=img_size)
    # No data augmentation applied for validation and test data
    image_generator = ImageDataGenerator(rescale=1. / 255., validation_split=validation_split)
    valid_batches = image_generator.flow_from_dataframe(dataframe=training_labels, directory=training_dir,
                                                        x_col=filename_column, y_col=target_column, subset="validation",
                                                        batch_size=batches_size, seed=42, shuffle=True,
                                                        color_mode=color_mode, target_size=img_size)
    test_batches = image_generator.flow_from_dataframe(dataframe=test_labels, directory=test_dir,
                                                       x_col=filename_column, y_col=target_column,
                                                       color_mode=color_mode, batch_size=batches_size,
                                                       shuffle=False, target_size=img_size)
    return training_batches, valid_batches, test_batches


def hog_pca_preprocessing(dataset_name, img_size=(96, 48), validation_split=0.15, variance=0.95, training_size=0.85,
                          target_column='smiling'):
    """
    Given a dataset it extracts HOG features from each image. Data dimensionality is then further reduced applying
    PCA algorithm.

    :param dataset_name: name (not path) of the folder that contains the images.
    :param img_size: image dimension after reshaping. default_value=(96,48).
    :param target_column: name of the column in the csv file where the labels are declared. default_value='smiling'.
    :param training_size: percentage size of the entire dataset dedicated to the training dataset. default_value=0.85.
    :param validation_split: percentage size of the entire dataset dedicated to the validation set. default_value=0.15.
    :param variance: the amount of variance to capture. default_value=0.95.
    :return: dataset and labels divided in training, validation and test parts. To each image is associated
        a reduced vector of features thanks to HOG and PCA algorithms. It returns also the pca and sc fitted on the
        training dataset so that it can applied on separate test datasets.
    """
    # Create path to access to all the images
    path = os.path.join(base_dir, dataset_name)
    images_dir = os.path.join(path, 'img')
    # List all the images within the folder
    files = sorted(os.listdir(images_dir), key=lambda x: int(x.split(".")[0]))
    dataset_labels = pd.read_csv(os.path.join(path, labels_filename), sep='\t', dtype='str')[target_column]
    feature_matrix = []
    # Counter inserted to display the execution status
    counter = 0
    print('\nExtracting features...')
    for file in files:
        counter += 1
        img = cv2.imread(os.path.join(images_dir, file), cv2.IMREAD_GRAYSCALE)
        # Resize the image in case it has a different size than the expected
        img = cv2.resize(img, img_size)
        hog_feature = hog(img, orientations=8, pixels_per_cell=(8, 8), cells_per_block=(2, 2),
                          multichannel=False, feature_vector=True)
        # Append the HOG features vector to the feature map
        feature_matrix.append(hog_feature)
        if counter % 1000 == 0:
            print('Images processed: {}'.format(counter))
    print('Computing PCA...')
    print('Data dimensionality before PCA: {}'.format(len(feature_matrix[0])))
    pca = PCA(n_components=variance)
    # Retrieve labels of all the image processed
    # Note: some images faces, i.e. smiles, are not detected
    files = [file.split('.')[0] for file in files]
    dataset_labels = dataset_labels.iloc[files]
    # Labels have to be transformed in int from the string format
    y = [int(label) for label in dataset_labels]
    X = np.array(feature_matrix)
    test_size = 1 - training_size
    # Split dataset in training and test dataset
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=test_size)
    # Find the percentage of the training dataset that has to be dedicated to validation
    validation_split = validation_split / training_size
    # Divide training dataset between training and validation dataset
    x_train, x_valid, y_train, y_valid = train_test_split(x_train, y_train, test_size=validation_split)
    # Normalize values before using PCA
    sc = StandardScaler()
    # Fit the StandardScaler with training data
    x_train = sc.fit_transform(x_train)
    x_test = sc.transform(x_test)
    x_valid = sc.transform(x_valid)
    # Fit the pca with training data and apply the dimensionality reduction on them
    x_train = pca.fit_transform(x_train)
    # Data is now projected on the first principal components previously extracted from the training set
    x_valid = pca.transform(x_valid)
    x_test = pca.transform(x_test)
    print('Data dimensionality after PCA: {}'.format(pca.n_components_))
    return x_test, x_train, x_valid, y_test, y_train, y_valid, pca, sc


# This function was created to increase the number of examples of the training data applying data augmentation.
# Unfortunately, the results reported show that it does not increase the generalization ability of the model.
def hog_pca_augmentation_preprocessing(dataset_name, img_size=(96, 48), validation_split=0.15, variance=0.95,
                                       training_size=0.85, target_column='smiling'):
    """
    Given a dataset it extracts HOG features from each image. Data dimensionality is then further reduced applying
    PCA algorithm. It also augments data on the training set.

    :param dataset_name: name (not path) of the folder that contains the images.
    :param img_size: image dimension after reshaping. default_value=(96,48).
    :param target_column: name of the column in the csv file where the labels are declared. default_value='smiling'.
    :param training_size: percentage size of the entire dataset dedicated to the training dataset. default_value=0.85.
    :param validation_split: percentage size of the entire dataset dedicated to the validation set. default_value=0.15
    :param variance: the amount of variance to capture. default_value=0.95.
    :return: dataset and labels divided in training, validation and test parts. To each image is associated
        a reduced vector of features thanks to HOG and PCA algorithms. It returns also the pca and sc fitted on the
        training dataset so that it can applied on separate test datasets.
    """
    # Create path to access to all the images
    path = os.path.join(base_dir, dataset_name)
    images_dir = os.path.join(path, 'img')
    # List all the images within the folder
    files = sorted(os.listdir(images_dir), key=lambda x: int(x.split(".")[0]))
    dataset_labels = pd.read_csv(os.path.join(path, labels_filename), sep='\t', dtype='str')[target_column]
    # Divide dataset in three parts
    # Simple random sampling to select examples for the test dataset
    # Augmentation not applied on test and validation sets
    valid_test_split = validation_split + 1 - training_size
    valid_test_images = sorted(sample(files, round(len(files) * valid_test_split)))
    feature_matrix = []
    print('Extracting features from validation and test sets...')
    for file in valid_test_images:
        img = cv2.imread(os.path.join(images_dir, file), cv2.IMREAD_GRAYSCALE)
        # Resize the image in case it has a different size than the expected
        img = cv2.resize(img, img_size)
        hog_feature = hog(img, orientations=8, pixels_per_cell=(8, 8), cells_per_block=(2, 2),
                          multichannel=False, feature_vector=True)
        # Append the HOG features vector to the feature map
        feature_matrix.append(hog_feature)
    # Retrieve labels
    labels = dataset_labels.iloc[[file.split('.')[0] for file in valid_test_images]]
    # Test size with respect to the sum of test and validation sets
    test_size = (1 - training_size) / valid_test_split
    x_valid, x_test, y_valid, y_test = train_test_split(np.array(feature_matrix), labels, test_size=test_size)

    # Create image data augmentation generator
    data_generator = ImageDataGenerator(height_shift_range=0.2, rotation_range=40, width_shift_range=0.2,
                                        brightness_range=[0.4, 1.5], shear_range=0.2, zoom_range=0.3)
    training_images = sorted(i for i in files if i not in valid_test_images)
    feature_matrix = []
    # Data augmentation applied only to the training dataset
    # Created a list to keep track of the files from which images are generated.
    # It is crucial to retrieve the correct labels after having applied data augmentation.
    names = []
    print('Extracting features from training set...\nApplying data augmentation...')
    for file in training_images:
        img = cv2.imread(os.path.join(images_dir, file), cv2.IMREAD_GRAYSCALE)
        # Resize the image in case it has a different size than the expected
        img = cv2.resize(img, img_size)
        hog_feature = hog(img, orientations=8, pixels_per_cell=(8, 8), cells_per_block=(2, 2),
                          multichannel=False, feature_vector=True)
        # Append the HOG features vector to the feature map
        feature_matrix.append(hog_feature)
        names.append(file)

        # Images on which data_generator works must have dimension (number, width, height, channels)
        img = np.expand_dims(img, (0, 3))
        # Apply data augmentation
        it = data_generator.flow(img, batch_size=1)
        # Convert the image format to the original (width, height)
        img = it.next()[0, :, :, 0]
        hog_feature = hog(img, orientations=8, pixels_per_cell=(8, 8), cells_per_block=(2, 2),
                          multichannel=False, feature_vector=True)
        # Append the HOG features vector to the feature map
        feature_matrix.append(hog_feature)
        names.append(file)
    # Retrieve labels
    y_train = dataset_labels.iloc[[file.split('.')[0] for file in names]]
    x_train = np.array(feature_matrix)
    print('Computing PCA...')
    print('Data dimensionality before PCA: {}'.format(len(feature_matrix[0])))
    pca = PCA(n_components=variance)
    # Normalize values before using PCA
    sc = StandardScaler()
    x_train = sc.fit_transform(x_train)
    x_test = sc.transform(x_test)
    x_valid = sc.transform(x_valid)
    # Fit the model with training data and apply the dimensionality reduction on them
    x_train = pca.fit_transform(x_train)
    # Data is now projected on the first principal components previously extracted from the training set
    x_valid = pca.transform(x_valid)
    x_test = pca.transform(x_test)
    print('Data dimensionality after PCA: {}'.format(pca.n_components_))
    return x_test, x_train, x_valid, y_test, y_train, y_valid, pca, sc


# This function extracts meaningful information from the images thanks to hog and lbp descriptors. The features
# considered are standardised and then reduced by PCA algorithm.
# Unfortunately, the results reported show that it does not increase the model performances.
def hog_lbp_pca_preprocessing(dataset_name, img_size=(96, 48), validation_split=0.15, variance=0.95, training_size=0.85,
                              target_column='smiling'):
    """
    Given a dataset it extracts HOG and LBP features from each image.
    Data dimensionality is then further reduced applying PCA algorithm.

    :param dataset_name: name (not path) of the folder that contains the images.
    :param img_size: image dimension after reshaping. default_value=(96,48).
    :param target_column: name of the column in the csv file where the labels are declared. default_value='smiling'.
    :param training_size: percentage size of the entire dataset dedicated to the training dataset. default_value=0.85.
    :param validation_split: percentage size of the entire dataset dedicated to the validation set. default_value=0.15.
    :param variance: the amount of variance to capture. default_value=0.95.
    :return: dataset and labels divided in training, validation and test parts. To each image is associated
        a reduced vector of features thanks to HOG and PCA algorithms. It returns also the pca and sc fitted on the
        training dataset so that it can applied on separate test datasets.
    """
    # Create path to access to all the images
    path = os.path.join(base_dir, dataset_name)
    images_dir = os.path.join(path, 'img')
    # List all the images within the folder
    files = sorted(os.listdir(images_dir), key=lambda x: int(x.split(".")[0]))
    dataset_labels = pd.read_csv(os.path.join(path, labels_filename), sep='\t', dtype='str')[target_column]
    feature_matrix = []
    # Counter inserted to display the execution status
    counter = 0
    print('\nExtracting features...')
    for file in files:
        counter += 1
        img = cv2.imread(os.path.join(images_dir, file), cv2.IMREAD_GRAYSCALE)
        # Resize the image in case it has a different size than the expected
        img = cv2.resize(img, img_size)
        hog_feature = hog(img, orientations=8, pixels_per_cell=(8, 8), cells_per_block=(2, 2),
                          multichannel=False, feature_vector=True)
        lbp_feature = local_binary_pattern(img, P=8, R=1).flatten()
        feature_vector = [*hog_feature, *lbp_feature]
        # Append the HOG features vector to the feature map
        feature_matrix.append(feature_vector)
        if counter % 1000 == 0:
            print('Images processed: {}'.format(counter))
    print('Computing PCA...')
    print('Data dimensionality before PCA: {}'.format(len(feature_matrix[0])))
    pca = PCA(n_components=variance)
    # Retrieve labels of all the image processed
    # Recall: in some images faces, i.e. smiles, are not detected
    files = [file.split('.')[0] for file in files]
    dataset_labels = dataset_labels.iloc[files]
    # Labels have to be transformed in int from the string format
    y = [int(label) for label in dataset_labels]
    X = np.array(feature_matrix)
    test_size = 1 - training_size
    # Split dataset in training and test dataset
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=test_size)
    # Find the percentage of the training dataset that has to be dedicated to validation
    validation_split = validation_split / training_size
    # Divide training dataset between training and validation dataset
    x_train, x_valid, y_train, y_valid = train_test_split(x_train, y_train, test_size=validation_split)
    # Normalize values before using PCA
    sc = StandardScaler()
    # Fit the StandardScaler with training data
    x_train = sc.fit_transform(x_train)
    x_test = sc.transform(x_test)
    x_valid = sc.transform(x_valid)
    # Fit the pca with training data and apply the dimensionality reduction on them
    x_train = pca.fit_transform(x_train)
    # Data is now projected on the first principal components previously extracted from the training set
    x_valid = pca.transform(x_valid)
    x_test = pca.transform(x_test)
    print('Data dimensionality after PCA: {}'.format(pca.n_components_))
    return x_test, x_train, x_valid, y_test, y_train, y_valid, pca, sc
