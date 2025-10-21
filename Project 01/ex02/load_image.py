import imageio.v3 as iio
import numpy as np

def ft_load(path: str) -> np.ndarray:

    try:
        image = iio.imread(path)
    except:
        print("Error during reading image")
        return

    print("The shape of image is:", image.shape)

    return image.reshape(1, -1, 3)
