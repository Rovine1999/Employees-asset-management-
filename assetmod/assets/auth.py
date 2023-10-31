from rest_framework.authentication import TokenAuthentication

# This class is used to override the default keyword used for token authentication
class BearerTokenAuthentication(TokenAuthentication):
    keyword = 'Bearer'


AUTH_CLASS = BearerTokenAuthentication
