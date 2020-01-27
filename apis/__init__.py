from flask_restplus import Api

from .cats import api as cats
from .dogs import api as dogs

api = Api(
  title= 'My API',
  version= '0,1',
  description= 'Minha api',
)

# api.add_namespace(cats, path='/cats')
api.add_namespace(dogs, path='/dogs')