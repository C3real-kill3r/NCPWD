import os


def get_domain():
    return os.getenv("CLIENT_DOMAIN")


def get_activation_link(token, uid):
    """
    :rtype: object
    """
    return "{}/{}?token={}&uid={}".format(
        get_domain(), os.getenv("CLIENT_ACTIVATE_ACCOUNT_ROUTE"), token, uid)
