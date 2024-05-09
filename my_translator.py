from googletrans import Translator
translator = Translator(service_urls=[
      'translate.google.com',
      'translate.google.co.kr',
    ])
term = input("Enter text to be converted: ")
x = translator.translate(term)
print(x.text)
