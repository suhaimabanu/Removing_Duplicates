import re

def remove_duplicate_words(paragraph):
    cleaned_paragraph = re.sub(r'\b(\w+)( \1)+\b', r'\1', paragraph, flags=re.IGNORECASE)
    return cleaned_paragraph

# Input
paragraph = ("in the bustling bustling city city of New york, New york, the bright bright lights lights and and the the constant constant hum hum "
             "of of activity activity create create an an atmosphere atmosphere that that is is both both exhilarating exhilarating and and exhausting exhausting. "
             "The bustling city lights and the constant hum of activity create an atmosphere that is both exhilarating and exhausting.")


cleaned_paragraph = remove_duplicate_words(paragraph)


final_cleaned_paragraph = re.sub(r'\b(new york)(\s*,?\s*\1)+\b', r'\1', cleaned_paragraph, flags=re.IGNORECASE)
print("Cleaned Paragraph:")
print(final_cleaned_paragraph)
