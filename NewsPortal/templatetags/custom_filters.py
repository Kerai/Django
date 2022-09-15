from django import template

register = template.Library()

#@register.filter()
#def scensor(text):
#    bad_words = ('редиска', 'bla')

#    if not isinstance(text, str):
#        raise TypeError(f"unresolved type '{type(text)}' expected  type 'str'")

#    for word in text.split():
#        if word.lower() in bad_words:
#            text = text.replace(word, f"{word[0]}{'*' * (len(word) - 0)}")
#    return text

@register.filter()
def scensor(text):
    ban_words = ('редиска', 'bla')

    if not isinstance(text, str):
        raise TypeError(f"unresolved type '{type(text)}' expected  type 'str'")

    for word in text.split():
        if word.lower() in ban_words:
            text = text.replace(word, f"{'Hail Caisar! '}")
    return text
