def get_profile(*args, name='julian', profession='programmer',**kwargs):
    if args:
        raise(TypeError)

    if kwargs.keys():
        raise(TypeError)

    return f"{name} is a {profession}"