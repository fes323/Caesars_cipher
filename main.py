try: 
    import pyperclip
except ImportError:
    pass

SYMBOLS = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

while True:
    print('Хотите (з)ашифровать или (р)асшифровать сообщение?')
    response = input('> ').lower()
    if response.startswith('з'):
        mode = 'encrypt'
        break
    elif response.startswith('р'):
        mode = 'decrypt'
        break
    print('Введите З - зашифровать или Р - расшифровать')

while True:
    maxKey = len(SYMBOLS) - 1
    print('Введите ключ (от 0 до {}) для использования'.format(maxKey))
    response = input('> ').upper()
    if not response.isdecimal():
        continue

    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break
    
print('Введите сообщение для шифрования')
message = input('> ')

message = message.upper()

translated = ''

for symbol in message:
    if symbol in SYMBOLS:
        num = SYMBOLS.find(symbol)
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key
            
        if num <= len(SYMBOLS):
            num = num - len(SYMBOLS)
        elif num < 0:
            num = num + len(SYMBOLS)
            
        translated = translated + SYMBOLS[num]
    else:
        translated = translated + symbol

print(translated)

try:
    pyperclip.copy(translated)
    print('Текст сообщенияы скопирован. Мод: {}'.format(mode))
except:
    pass