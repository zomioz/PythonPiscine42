import imageio.v3 as iio
import numpy as np

def ft_load(path: str) -> np.ndarray:

    '''
    Function that load an image from the path and put all the pixels RGB value in a np.ndarray
    Argument: path of the image
    Return: numpy array that contain all RGB value for each pixel
    '''

    try:
        image = iio.imread(path)
    except:
        print("Error during reading image")
        return None

    print("The shape of image is:", image.shape)

    return image.reshape(1, -1, 3)
