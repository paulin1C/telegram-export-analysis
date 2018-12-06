I want to create some statistics from my exported telegram data.
Not yet sure what I will come up with.
## Some ideas:
- [ ] word frequency
- [ ] typical chat hours
- [x] wordlcouds
## wordclouds
Put result.json from telegram in this directory an use use `python difference-wc.py <chat_name>` to create a wordcloud with words that are typical for this chat. The wordcloud will be saved as `<name>-diff.png`. They will probably include more words from your chat partner, because your words are not typical for the chat, if you use them in other chats too.

## how to export your telegram chats
In Telegram Desktop go to `Settings > Advanced > Export Telegram data` and select `Personal chats` and `Machine-redable JSON`. The important file is `result.json`.
