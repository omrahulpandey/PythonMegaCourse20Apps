def prepare(text):
    text = text.title()
    print(text)
    text = text.strip()
    print(text)
    return text
    
print(prepare("hello    "))