import getpass
import os
import requests

import cv2 as cv
import praw

from proprossesing import prepocesses_image


def download_images_from_subreddit(subreddit, number_images, save_path):
    """
    Takes a subreddit name, for example "earthporn", downloads images from that subreddit,
    and saves them in <save_path>.

    Note: save_path must exist.

    :param subreddit: string. Subreddit instance to download from.
    :param save_path: string. Path to save downloaded images.
    :return: None
    """
    if(not os.path.exists(save_path)):
        raise OSError("Save path does not exist!")

    # TODO figure out where we want to save images and the metadata
    count = 0
    for submission in subreddit.top(limit=number_images):
        # The top post in r/earthporn is an ad for fighting net neutrality.
        if(count == 0):
            count += 1
            continue

        image_path = "{}{}image_{}_score_{}.png".format(save_path,
                                                        os.path.sep,
                                                        submission.id,
                                                        submission.score)

        url = (submission.url)

        r = requests.get(url)
        with open(image_path, "wb") as f:
            f.write(r.content)


def get_subreddit_instance(subreddit, secret_file_path):
    """

    :param secret_file_path:
    :param subreddit: string. Name of a subreddit.
    :return: The subreddit instance.
    """
    clinet_id = "yVOpTZ6pI7aHnw"

    with open(secret_file_path, "r") as f:
        secret = f.readline()

    # TODO replace the inputs with valid values
    reddit = praw.Reddit(client_id=clinet_id,
                         client_secret=secret,
                         user_agent="learning_earthporn")

    return reddit.subreddit(subreddit)


def main():
    number_images = 5

    user             = getpass.getuser()
    secret_file_path = os.path.join("C:\\", "users", user, "Documents", "reddit_app_pass.txt")
    image_save_path  = os.path.join("C:\\", "users", user, "Documents", "learning_earthporn", "images")

    os.makedirs(image_save_path, exist_ok=True)

    subreddit = get_subreddit_instance("earthporn", secret_file_path)
    download_images_from_subreddit(subreddit, number_images, image_save_path)

    files           = os.listdir(image_save_path)
    test_image_path = os.path.join(image_save_path, files[0])

    image      = cv.imread(test_image_path)
    post_image = prepocesses_image(image)

    cv.imshow("pre test", image)
    cv.imshow("post test", post_image)
    cv.waitKey(0)
    cv.destroyAllWindows()


if( __name__ == "__main__"):
    main()
