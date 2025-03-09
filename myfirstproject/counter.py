import operator

def count(article):
    words= article.split()
    word_count= len(words)
    dic_word= {}
    for word in words:
        if word in dic_word:
            dic_word[word]+= 1
        else:
            dic_word[word]= 1

    sorted_dic= sorted(dic_word.items(), key= operator.itemgetter(1), reverse=True)
    return word_count, sorted_dic