def format_name(f_name, l_name):
    """this method is responsible for returning a formatted name
    :rtype: str
    """
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formatted_name = format_name("AnGeLa", "YU")
