from load_image import ft_load
import matplotlib.pyplot as plt
import imageio.v3 as iio


def rgb_to_gray(rgb):

    '''
    Function to convert 3 channels RDB into 1 channel gray
    Argument: 3 channels image
    Return: 1 channel image
    '''

    r, g, b = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]
    gray = 0.30 * r + 0.59 * g + 0.11 * b
    return gray


def display_everything(gray_image_3D, gray_image, image) -> None:

    '''
    Function to display image and image's info
    Argument: 3 images
    Return: None
    '''

    print(image)
    print("The shape of image is:", gray_image_3D.shape,
          "or", gray_image.shape)
    print(gray_image_3D.reshape(1, -1, 1))

    plt.imshow(gray_image_3D, cmap='gray')
    plt.axis('on')
    plt.title('Zoomed Racoon')
    plt.show()


def main() -> None:

    '''
    Function to load and format image, proteted by a try, expect
    Argument: None
    Return: None
    '''

    image = ft_load('animal.jpeg')
    if image is None:
        return

    original_image = iio.imread('animal.jpeg')
    reshaped = original_image[100:500, 450:850, :]
    gray_image = rgb_to_gray(reshaped)
    gray_image_int = gray_image.astype(int)
    gray_image_3D = gray_image_int.reshape(gray_image_int.shape[0],
                                           gray_image_int.shape[1], 1)

    display_everything(gray_image_3D, gray_image, image)


if __name__ == "__main__":
    main()
