def greet(name):
    """
    Generates a greeting message for the given name.

    :param name: (str) The name of the person to greet.
    :return: (str) The greeting message.
    """
    return f"Hello, {name}!"


if __name__ == "__main__":
    user_name = "Alice"
    print(greet(user_name))