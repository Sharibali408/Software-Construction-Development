# --- BEFORE  
def check_access(user, resource):
    if user:
        if user.active:
            if resource:
                if user.role == "admin":
                    return True
                else:
                    if resource.owner_id == user.id:
                        return True
                    else:
                        if resource.public:
                            return True
    return False