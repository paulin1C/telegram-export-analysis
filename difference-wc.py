# -*- coding: utf-8 -*-
import sys
from tools import *
import imageio
from wordcloud import WordCloud

name = sys.argv[1]

chats = get_chat_list()
selected_chat = find_chat_by_name(name)
if selected_chat:
    chats.remove(selected_chat)
    total_words = 0
    count = {}
    for chat in chats:
        c = Conversation(chat)
        total_words += len(c.word_list())
        for key, value in c.count_words().items(): # create one big dict with all apperances from all chats
            if key in count:
                count[key] += value
            else:
                count[key] = value

    all_probability = {}
    for key, value in count.items(): # convert total count to a relative value to make it compareable
        all_probability[key] = value/total_words

    selected_chat = Conversation(selected_chat) # thats the chat specified with str 'name' above
    selected_chat_total = len(selected_chat.word_list())
    selected_chat_probability = {}
    for key, value in selected_chat.count_words().items():
        selected_chat_probability[key] = value/selected_chat_total

    difference = {}
     # create dict 'difference' with words as key and relations of apperance probability as values
    for word, probability in selected_chat_probability.items():
        if word in all_probability:
            difference[word] = probability / all_probability[word]

    wc = WordCloud(max_font_size=250, width=1920, height=1080, max_words=1000)
    wc.generate_from_frequencies(difference)
    imageio.imwrite(name + "-diff.png", wc)
