import os


def get_domain():
    return os.getenv("CLIENT_DOMAIN")


def get_activation_link(token, uid):
    return "{}/{}?token={}&uid={}".format(
        get_domain(), os.getenv("CLIENT_ACTIVATE_ACCOUNT_ROUTE"), token, uid)


def get_login_link():
    return "/login".format(get_domain(), os.getenv(
            "LOGIN_ROUTE"))


def get_password_reset_link(token):
    return "{}/{}?token={}".format(get_domain(), os.getenv(
            "CLIENT_RESET_PASSWORD_ROUTE"), token)
