def new_password(oldpassword, newpassword):
    if oldpassword != newpassword and len(newpassword) >= 6 and any(char.isdigit() for char in newpassword):
        return True
    else:
        return False
