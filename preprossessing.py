import cv2 as cv


def preprossess_image(image):
    """
    # Note: the input image but be in BGR format (follows opencv conventions).

    :param image: 
    :return: 
    """
    # First, get the grayscale image.
    gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    # Second, blur the image.
    # TODO what's the best kernal size, sigmaX, and padding?
    blurred_image = cv.GaussianBlur(gray_image, (5, 5), 0.5, borderType=cv.BORDER_REFLECT_101)

    # Then Downscale the image by a factor of 1/4.
    scale_percent = 25  # percent of original size
    width         = int(blurred_image.shape[1] * scale_percent / 100)
    height        = int(blurred_image.shape[0] * scale_percent / 100)
    dim           = (width, height)
    downscaled    = cv.resize(blurred_image, dim, interpolation=cv.INTER_AREA)

    # Finally, Upscale the image back to the original size.
    scale_percent = 400  # percent of original size
    width         = int(downscaled.shape[1] * scale_percent / 100)
    height        = int(downscaled.shape[0] * scale_percent / 100)
    dim           = (width, height)
    upscaled      = cv.resize(downscaled, dim, interpolation=cv.INTER_AREA)

    # Check to see if the output image has the same dimensions as the input image.
    if(image.shape[0:2] != upscaled.shape[0:2]):
        # TODO do we care if the dimensions are off by a little?
        #raise ArithmeticError("Prepossessed and post possessed image do not have the same dimensions!")
        pass

    return upscaled


def main():
    test_image_path = "C:\\users\\natej\\Documents\\test_dog.png"

    image = cv.imread(test_image_path)
    post_image = prepocesses_image(image)

    cv.imshow("pre test", image)
    cv.imshow("post test", post_image)
    cv.waitKey(0)
    cv.destroyAllWindows()


if( __name__ == "__main__"):
    main()