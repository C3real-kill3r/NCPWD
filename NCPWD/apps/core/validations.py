import re

email_expression = re.compile(
    r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
trial_email = re.compile(
    r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[0-9-.]+$)")
trial_email_2 = re.compile(
    r"(^[a-zA-Z0-9_.+-]+@[0-9-]+\.[a-zA-Z0-9-.]+$)")
at_least_number = re.compile(
    r"^(?=.*[0-9]).*")
at_least_uppercase = re.compile(
    r"^(?=.*[A-Z])(?=.*[a-z])(?!.*\s).*")
at_least_special_char = re.compile(
    r".*[!@#$%^&*()_\-+={};:\'\"|`~,<.>?/].*")