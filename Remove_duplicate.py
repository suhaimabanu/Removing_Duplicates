import re

def remove_duplicate_words(text):
    # Use regex to find duplicate consecutive words and replace them
    result = re.sub(r'\b(\w+)\b(?:\s+\1)+', r'\1', text)
    return result

# Input text
input_text = """In the bustling bustling city city of New York, New York, the the bright bright lights lights and and the the constant constant hum hum of of activity activity create create an an atmosphere atmosphere that that is is both both exhilarating exhilarating and and exhausting exhausting. The bustling city lights and the constant hum of activity create an atmosphere that is both exhilarating and exhausting."""

# Process the input text
output_text = remove_duplicate_words(input_text)

# Print the output
print("Output:")
print(output_text)
