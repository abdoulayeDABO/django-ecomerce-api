from ..utils import HTTPResponse, checkToken


def login_required(func):
    """
    Decorator for views that checks that the user is logged in
    """
    def function(request, *args, **kwargs):
        # print(request.headers['Authorization'])
        if not request.headers['Authorization']:
            return HTTPResponse({'status': 'error', 'message': 'Unauthorized'}, 401)
        token = request.headers['Authorization'].split(' ')[1]
        try:
            decoded = checkToken(token)
            # print(decoded)
            if not decoded:
                return HTTPResponse({'status': 'error', 'message': 'Unauthorized'}, 401)
        except:
            return HTTPResponse({'status': 'error', 'message': 'Unauthorized'}, 401)
        return func(request, *args, **kwargs)
    return function