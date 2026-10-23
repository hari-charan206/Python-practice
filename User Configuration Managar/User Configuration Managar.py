def add_setting(settings,tuplee):
    key=tuplee[0].lower()
    value=tuplee[1].lower()
    exists=False
    for keys in settings.keys():
        if key==keys.lower():
            exists=True
            break
        else:
            pass
    if exists==True:
        return(f"Setting '{key}' already exists! Cannot add a new setting with this name.")
    else:
        settings[key]=value
        return(f"Setting '{key}' added with value '{value}' successfully!")
def update_setting(settings,tuplee):
    key=tuplee[0].lower()
    value=tuplee[1].lower()
    exists=False
    for keys in settings.keys():
        if key==keys:
            exists=True
            break
        else:
            pass
    if exists==True:
        settings[key]=value
        return(f"Setting '{key}' updated to '{value}' successfully!")
    else:
        return(f"Setting '{key}' does not exist! Cannot update a non-existing setting.")
def delete_setting(settings,key):
    key=key.lower()
    exists=False
    for keys in settings.keys():
        if key==keys:
            exists=True
            break
        else:
            pass
    if exists==True:
        settings.pop(key)
        return(f"Setting '{key}' deleted successfully!")
    else:
        return("Setting not found!")
def view_settings(settings):
    if settings == {}:
        return "No settings available."
    string = "Current User Settings:\n"
    for key, value in settings.items():
        string += f"{key.capitalize()}: {value}\n"
    return string
test_settings={'theme': 'light', 'language': 'English'}   
add_setting({'theme': 'light', 'language': 'English'}, ('THEME', 'dark'))
add_setting({'theme': 'light'}, ('volume', 'high'))
update_setting({'theme': 'light', 'language': 'English'}, ('theme', 'dark'))
update_setting({'theme': 'light'}, ('volume', 'high'))
delete_setting({'theme': 'light', 'language': 'English'}, 'theme')
delete_setting
view_settings
