from background_task import background
from .models import Post


DAILY = 60 * 60 * 24


@background(schedule=5)
def reset_upvotes():
    """
    function to reset upvotes daily
    """
    Post.objects.update(upvotes=0)


reset_upvotes(repeat=DAILY)
