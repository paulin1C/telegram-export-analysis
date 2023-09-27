import operator, json
telegram_json_export = "result.json"


def get_chat_list():
    "lists all the chats (with persons) from a telegram json data export"
    with open(telegram_json_export) as json_data:
        data = json.load(json_data)
    chats = []
    for chat in data['chats']['list']:
        if chat["type"] == "personal_chat":
            chats.append(chat)
    return chats

def find_chat_by_name(name):
    for chat in get_chat_list():
        if chat["name"] == name:
            return chat
    print("chat not found")
    return False

def default_filter(message):
    return True

def count_words(list):
    "returns a dict with words as keys and the number of apperances as values"
    count = {}
    for word in list:
        if not word in count:
            count[word] = 1
        else:
            count[word] += 1
    return count

class Conversation:
    "Describes a conversation with one person"
    def __init__(self, chat):
        self.messages = chat['messages']
        self.name = chat['name']

    def word_list(self, filter = default_filter):
        "returns a list of all words from all messages (not a set)"
        list = []
        for message in self.messages:
            if filter(message):
                if type(message['text']) == str:
                    text = message['text'].lower()
                    for char in """,!.…/"'()*?=-–;:^""":
                        text = text.replace(char, " ")
                    blocks = text.split(' ') # blocks might contain multiple words, sperated by \n
                    for block in blocks:
                        for word in block.split('\n'):
                            if not word in ["", " "]:
                                list.append(word)
        return list

    def string_of_all_messages(self):
        "returns a long string of all messages with spaces"
        return " ".join(self.word_list())

    def count_words(self):
        "returns a dict with words as keys and the number of apperances as values"
        return count_words(self.word_list())
