def login_required(obj):
    if not obj.is_authenticated:
        raise Exception('User is not authorized.')


