import json

from image import image_urls

class UserService:
    def __init__(self):
        try:
            with open('data.json', 'r') as file:
                self.data = json.load(file)
                self.member_index = {}
                for member in self.data['members']:
                    if 'id' in member:
                        self.member_index[member['id']] = member
                self.member_length = len(self.member_index)
        except FileNotFoundError:
            raise

    def get_member(self, user_id):
        if int(user_id) > self.member_length:
            return
        return self.member_index.get(user_id)

    def image_helper(self, user_id: str, slices: int = 9):
        zero_based_number = int(user_id) - 1
        start_index = zero_based_number * slices
        end_index = start_index + slices
        if start_index > len(image_urls):
            return []
        elif end_index > len(image_urls):
            return image_urls[start_index:len(image_urls)]
        return image_urls[start_index:end_index]

    def text_helper(self, member):
        text_carousel = []

        for i in range(1, 6):
            trait_key = f'trait_{i}'
            trait = member.get(trait_key)
            if trait:
                trait_data = {
                    'answer': trait.get('answer'),
                    'is_scale': trait.get('is_scale'),
                    'max_val': trait.get('max_val'),
                    'percentage': trait.get('percentage'),
                    'question': trait.get('question')
                }
                text_carousel.append(trait_data)
        return text_carousel