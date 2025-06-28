from tiktoken import encoding_for_model

def count_tokens(messages, model="gpt-4"):
   enc = encoding_for_model(model)
   return sum(len(enc.encode(m)) + 4 for m in messages)

def trim_messages(messages, max_tokens=4000):
   if count_tokens(messages) <= max_tokens:
       return messages
   # remove oldest user/assistant messages
   while count_tokens(messages) > max_tokens and len(messages) > 1:
       messages.pop(0)
   return messages
