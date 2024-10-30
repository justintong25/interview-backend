from services.user_service import UserService


class UserResource:
    def __init__(self, user_service: UserService):
        self._user_service = user_service

    def on_get(self, req, resp):
        user_id = req.get_param('id', default='')
        member = self._user_service.get_member(user_id)
        if member:
            images = self._user_service.image_helper(user_id)
            text = self._user_service.text_helper(member)
            resp.media = {
                'user_data': member,
                'images': images,
                'text': text
            }
        else:
            resp.media = {
                'user_data': '',
                'images': [],
                'text': ''
            }

