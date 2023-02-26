from PIL import Image

scaling_factor = 200

# banner from https://textkool.com/en/ascii-art-generator?hl=default&vl=default&font=ANSI%20Regular&text=YOUR%201%20%26%200%20Image
def banner():
    print('\033[2J')
    print('''
██    ██  ██████  ██    ██ ██████       ██        ██         ██████      ██ ███    ███  █████   ██████  ███████ 
 ██  ██  ██    ██ ██    ██ ██   ██     ███        ██        ██  ████     ██ ████  ████ ██   ██ ██       ██      
  ████   ██    ██ ██    ██ ██████       ██     ████████     ██ ██ ██     ██ ██ ████ ██ ███████ ██   ███ █████   
   ██    ██    ██ ██    ██ ██   ██      ██     ██  ██       ████  ██     ██ ██  ██  ██ ██   ██ ██    ██ ██      
   ██     ██████   ██████  ██   ██      ██     ██████        ██████      ██ ██      ██ ██   ██  ██████  ███████ 
                                                                                                                                                                                                                                                                                                                      
''')

def main():
    banner()

    while True:
        print('''
Option :
1. Generate Image
2. Info
3. Scale
4. Quit
        ''')
        menu = input('Select Number >> ')

        if menu == '4' or menu.lower() == 'quit':
            print('Thanks')
            exit()
        elif menu == '3' or menu.lower() == 'info':
            print()
            scale()
        elif menu == '2' or menu.lower() == 'info':
            print()
            info()
        elif menu == '1' or menu.lower() == 'generate image':
            print()
            generate()
        else:
            print('Invalid option, see you later')
            exit()

def scale():
    try:
        num = int(input('default scale is 200, input num to change it\n'))
        global scaling_factor 
        scaling_factor = num
            
    except ValueError:
        print("\nInput must be a number.\nCannot process further")

def info():
    print('''
FYI:
> 1 black 0 white.
> some data will be discarded if modulo of your data length and width isn't 0.
> program use 200 as scalling factor, you can change it with scale menu.
                                - Author
''')

def generate():
    try:
        data = input('Input your data (0 or 1) : ')
        data = [int(x) for x in data]
        if not all(x == 0 or x == 1 for x in data):
            print("\nInput must be 0 or 1.\nCannot process further")
            
    except ValueError:
        print("\nInput must be a number.\nCannot process further")
        
    try: 
        width = int(input('Width : '))
        if width > len(data):
            print('\nWidth is greater than data.\nCannot process further')
            
    except ValueError:
        print("\nInput must be a number.\nCannot process further")
    
    rest = - (len(data) % width)
    if rest != 0:
        data = data[:rest]
    height = int(len(data) / width)

    image = Image.new('1', (width * scaling_factor, height * scaling_factor))
    pixels = image.load()

    for i, value in enumerate(data):
        x, y = (i % width) * scaling_factor, (i // width) * scaling_factor
        for j in range(scaling_factor):
            for k in range(scaling_factor):
                pixels[x + j, y + k] = 1 - value

    name = input('Give your image name : ')
    image.save(f'{name}.png')

    print(f'Image succesfully generated with name : {name}.png')
    print('\ncontinue ?')
    yes_or_no = input('[y/n] ')
    if yes_or_no[0].lower() != 'y':
        exit() 

if __name__ == '__main__':
    main()
