def get_full_name(first_name,last_name,middle_name="hooker"):
    name = f" {first_name} {middle_name} {last_name} ".format(first_name,middle_name,last_name)
    return name
print(get_full_name(first_name="Bruce", last_name="Lee"))