file = 'my name is jones'



def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

    # LEARNER CODE START HERE
    remove_punctuation = ""
    for char in file_contents:
        if char not in punctuations:
            remove_punctuation = remove_punctuation + char

    interesting_words = {}
    words = remove_punctuation.split()
    words = [print(word.lower()) for word in words]

    for word in words:
        if word in uninteresting_words:
            pass
        elif word in interesting_words:
            interesting_words[word] += 1
        else:
            interesting_words[word] = 1

    print(interesting_words)
    #wordcloud
calculate_frequencies(file)
