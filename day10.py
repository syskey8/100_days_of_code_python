# fucntions with outputs

def format_name(f_name, l_name):
    formated_f_name = f_name.title() # makes the first letter of every word captitaland rest small
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

formated_string = format_name("AnGela", "YU")
print(format_name("AnGeLA", "YU")) # output: Angela Yu

# docstring

''' this
is 
a multi
line comment

'''