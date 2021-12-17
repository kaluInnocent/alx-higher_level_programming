def say_my_name(first_name, last_name=""):
    """Function prints First Name and Last name
    Args:
        first_name (str): First name supplied by user
        last_name (str): last name supplied by user
    Returns: Nothing
    """
    if isinstance(first_name, str):
        if isinstance(last_name, str):
            if last_name == "":
                print(f"My name is {first_name}")
            else:
                print(f"My name is {first_name} {last_name}")
        else:
            raise TypeError("last_name must be a string")
    else:
        raise TypeError("first_name must be a string")
