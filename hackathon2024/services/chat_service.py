from ..models import Chat

class ChatService:
    def get_all_chats(self):
        return Chat.objects.all()

    def create_chat(self, data):
        chat = Chat.objects.create(**data)
        return chat