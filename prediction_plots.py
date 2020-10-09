import matplotlib.pyplot as plt
import numpy as np

def plot_single_prediction(image, predicted_breed_image):
    '''Plot input picture along with the sample picture of predicted breed'''
    plt.figure(figsize = (10, 5))
    # Plot input image
    plt.subplot(1, 2, 1)
    plt.title('Image')
    plt.imshow(image)
    plt.axis('off')
    # Along with the predicted breed image
    plt.subplot(1, 2, 2)
    plt.title('Predicted breed')
    plt.imshow(predicted_breed_image)
    plt.axis('off')
    plt.show()

def plot_multiple_predictions(image,
                              predicted_breed_image,
                              class_names,
                              probabilities):
    '''Plot input picture, predicted breed picture and a plot of probabilities
    for a list of predicted breeds'''
    plt.figure(figsize = (15, 5))
    # Plot input image
    plt.subplot(1, 3, 1)
    plt.title('Image')
    plt.imshow(image)
    plt.axis('off')
    # Along with the predicted breed image
    plt.subplot(1, 3, 2)
    plt.title('Predicted breed')
    plt.imshow(predicted_breed_image)
    plt.axis('off')
    # And breed probabilities
    ax = plt.subplot(1, 3, 3)
    y_ticks = np.arange(len(probabilities))
    ax.barh(y_ticks, probabilities)
    ax.set_aspect(0.1)
    ax.set_yticks(y_ticks)
    ax.set_yticklabels(class_names)
    ax.set_title('Breed probability')
    ax.set_xlim(0, 1)
    ax.invert_yaxis()  # labels read top-to-bottom
    plt.tight_layout()
    plt.show()

def plot_no_prediction(image):
    '''Plot just the image'''
    plt.figure(figsize = (5, 5))
    plt.imshow(image)
    plt.axis('off')
    plt.show()
