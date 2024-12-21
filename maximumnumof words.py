def mostWordsInSentence(sentences):
    max_words = 0
    
    for sentence in sentences:

        word_count = len(sentence.split())
        

        max_words = max(max_words, word_count)
    

    return max_words


sentences = [
    "This is a simple sentence",
    "Another sentence with more words in it",
    "Short sentence",
]

print(mostWordsInSentence(sentences))
