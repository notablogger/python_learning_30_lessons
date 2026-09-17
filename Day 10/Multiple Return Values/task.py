def format_name(f_name, l_name):
    """format the name if
     both are not empty.
     :param f_name:
     :param l_name:
     :return: """
    if f_name == "" or l_name == "":
        print("condition not met")
        return
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


print(format_name("AnGEla", "YU"))
print(format_name("", ""))

format_name("AnGEla", "YU")
