from pypro.modulos import facade


def list_modules(request):
    return {'MODULES': facade.list_modules_ordered()}
