def new_password(oldpassword, newpassword):
    return oldpassword != newpassword and len(newpassword) >= 6 and any(char.isdigit() for char in newpassword)
