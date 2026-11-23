def censor(text, word):
    word_length = len(word)
    text_length = len(text)
    stars = "*" * word_length
    result = ""
    index = 0

    while index < text_length:
        if index + word_length <= text_length and text[index:index+word_length] == word:
            result += stars
            index += word_length
        else:
            result += text[index]
            index += 1

    return result
