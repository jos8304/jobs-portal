from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    exception_class = exc.__class__.__name__


    if exception_class == 'AuthenticationFailed':
        response.data = {
            "error": "Invalid Email or Password. Please try again"
        }
    
    if exception_class == 'NotAuthenticationFailed':
        response.data = {
            "error": "Login first to access this resouce"
        }

    if exception_class == 'InvalidToken':
        response.data = {
            "error": "Your authentication token is expired. Please login again."
        }

    return response