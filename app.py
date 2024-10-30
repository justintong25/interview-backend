import json

import falcon
from falcon_cors import CORS
from wsgiref.simple_server import make_server

from resources.user_resource import UserResource
from services.user_service import UserService

cors = CORS(
    allow_all_origins=True,
    allow_all_headers=True,
    allow_all_methods=True
)


user_service = UserService()
app = falcon.App(middleware=[cors.middleware])
app.add_route('/', UserResource(user_service))

if __name__ == '__main__':
    with make_server('', 8000, app) as httpd:
        print('Serving on port 8000...')
        httpd.serve_forever()
