import os
import praw


def download_images_from_subreddit(subreddit, number_images, save_path):
    """
    Takes a subreddit name, for example "earthporn", downloads images from that subreddit,
    and saves them in <save_path>.

    Note: The meta data for the images has to be saved and be able to relate back to the image.
    Metadata we'll need includes number of upvotes, date posted, and post title.

    :param subreddit: string. Subreddit instance to download from.
    :param save_path: string. Path to save downloaded images.
    :return: None
    """
    # TODO configure where we want images from. ie: hot, top, new, etc
    # TODO figure out where we want to save images and the metadata
    for submission in subreddit.hot(limit=number_images):
        print(submission.title)  # Output: the submission's title
        print(submission.score)  # Output: the submission's score
        print(submission.id)  # Output: the submission's ID
        print(submission.url)  # Output: the URL the submission points to
        # or the submission's URL if it's a self post


def get_subreddit_instance(subreddit, secret_file_path):
    """

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


def save_images_to_dropbox():
    # TODO are we using dropbox? googledrive? something else?
    raise NotImplementedError


def main():
    # NOTE replace this with the file that has the reddit client secret.
    user = "natej"
    secret_file_path = os.path.join("C:\\", "users", user, "Documents", "reddit_app_pass.txt")

    subreddit = get_subreddit_instance("earthporn", secret_file_path)
    download_images_from_subreddit(subreddit, 10, "")


if( __name__ == "__main__"):
    main()
