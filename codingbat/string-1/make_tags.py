def make_tags(tag, word):
    """
    The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. In this example,
    the "i" tag makes <i> and </i> which surround the word "Yay". Given tag and word strings, create the
    HTML string with tags around the word, e.g. "<i>Yay</i>".
    """
    return "<" + tag + ">" + word + "</" + tag + ">"

print(make_tags('i', 'Yay'))
print(make_tags('i', 'Hello'))
print(make_tags('cite', 'Yay'))