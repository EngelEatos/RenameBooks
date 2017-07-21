import nltk, re

def truecase(text):
    truecased_sents = [] # list of truecased sentences
    # apply POS-tagging
    tagged_sent = nltk.pos_tag([word.lower() for word in nltk.word_tokenize(text)])
    # infer capitalization from POS-tags
    normalized_sent = [w.capitalize() if t in ["NN","NNS"] else w for (w,t) in tagged_sent]
    # capitalize first word in sentence
    normalized_sent[0] = normalized_sent[0].capitalize()
    # use regular expression to get punctuation right
    pretty_string = re.sub(" (?=[\.,'!?:;])", "", ' '.join(normalized_sent))
    return pretty_string

text = "Clonazepam Has Been Approved As An Anticonvulsant To Be Manufactured In 0.5mg, 1mg And 2mg Tablets. It Is The Generic Equivalent Of Roche Laboratories' Klonopin."
print(truecase(text))
