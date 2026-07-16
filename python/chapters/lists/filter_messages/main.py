def filter_messages(messages):
    filtered_messages = []
    dang_count = []

    for message in messages:
        words = message.split()
        filtered_words = []
        count = 0

        for i in range(0, len(words)):
            word = words[i]

            if word == 'dang':
                count += 1
                continue
            
            filtered_words.append(words[i])

        dang_count.append(count)
        filtered_messages.append(" ".join(filtered_words))
    
    return filtered_messages, dang_count
    
