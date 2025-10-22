import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import imageio.v3 as iio
import numpy as np
from numpy import array


def ft_invert(array) -> array:

    '''
    A function to invert the RGB color of an image
    Argument: a numpy array with 3 channels
    Return: A numpy array with 3 channels
    '''

    if array is None:
        return None
        
    new_array = array.copy().astype(float)
    
    new_array = 255 - new_array
    new_array = new_array.astype(np.uint8)
    
    print("Invert the color of the image received")
    plt.imshow(new_array)
    plt.axis('off')
    plt.title('invert landscape')
    plt.show()

    return new_array


def ft_red(array) -> array:
    if array is None:
        return None
        
    new_array = array.copy()
    
    new_array[:, :, 1] = 0
    new_array[:, :, 2] = 0
    
    print("Turn to red the color of the image received")
    plt.imshow(new_array)
    plt.axis('off')
    plt.title('red landscape')
    plt.show()

    return new_array


def ft_green(array) -> array:
    if array is None:
        return None
        
    new_array = array.copy()
    
    new_array[:, :, 0] = 0
    new_array[:, :, 2] = 0

    print("Turn to green the color of the image received")    
    plt.imshow(new_array)
    plt.axis('off')
    plt.title('green landscape')
    plt.show()

    return new_array


def ft_blue(array) -> array:
    if array is None:
        return None
        
    new_array = array.copy()
    
    new_array[:, :, 0] = 0
    new_array[:, :, 1] = 0
    
    print("Turn to blue the color of the image received")
    plt.imshow(new_array)
    plt.axis('off')
    plt.title('blue landscape')
    plt.show()

    return new_array


def ft_grey(array) -> array:
    if array is None:
        return None
        
    new_array = array.copy().astype(float)
    
    # Convert to grayscale using only / and =
    new_array[:, :, 0] = new_array[:, :, 0] / 3
    new_array[:, :, 1] = new_array[:, :, 1] / 3  
    new_array[:, :, 2] = new_array[:, :, 2] / 3
    
    gray_value = new_array[:, :, 0] / 1
    gray_value = gray_value / 1
    gray_value = gray_value / 1
    
    new_array[:, :, 0] = gray_value
    new_array[:, :, 1] = gray_value
    new_array[:, :, 2] = gray_value
    
    new_array = new_array.astype(np.uint8)
    
    print("Turn to gray the color of the image received")
    plt.imshow(new_array, cmap='gray')
    plt.axis('off')
    plt.title('gray landscape')
    plt.show()

    return new_array
