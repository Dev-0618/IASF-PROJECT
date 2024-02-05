# dictionary for Morse code
morse_code_dict = {
     'A': '%6', 'B': '$##', 'C': '%#@', 'D': 'grr', 'E': 'r$$q',
    'F': '(%%^', 'G': '%#!@E', 'H': 'HR5434', 'I': '%#!@$', 'J': 'YHR',
    'K': '%@!$', 'L': 'G$..', 'M': '-O-', 'N': '-O-%#%#%', 'O': '#%#%444',
    'P': '$&$', 'Q': '$!$#', 'R': '&&', 'S': '#!', 'T': 'TG',
    'U': '$Gh', 'V': '#010', 'W': '#!#DTG', 'X': '23243%35', 'Y': '$#!423',
    'Z': '@#%jd', '0': '@#@$Hkhd', '1': '@#$#B', '2': 'HEW7dh', '3': '#$!@#$',
    '4': '$@#@#', '5': '%#$@$', '6': '@$%%@$', '7': 'hfvvcb', '8': 'bchgsuyg',
    '9': 'DPjiehcb', ' ': 'kkjkk'
}

# Function to encode text to Morse code
def text_to_morse(text):
    text = text.upper()
    morse_code = []
    for char in text:
        if char in morse_code_dict:
            morse_code.append(morse_code_dict[char])
        else:
            morse_code.append(char)  # Keep unknown characters as-is
    return ' '.join(morse_code)

# Function to decode Morse code to text
def morse_to_text(morse_code):
    morse_code = morse_code.split(' ')
    text = []
    for code in morse_code:
        if code in morse_code_dict.values():
            text.append([char for char, value in morse_code_dict.items() if value == code][0])
        elif code == '/':



            text.append(' ')  # Use '/' as a space
        else:
            text.append(code)  # Keep unknown codes as-is
    return ''.join(text)

# Take user input
choice = input("Enter '1' to encode text to Morse code or '2' to decode Morse code to text: ")

if choice == '1':
    user_input = input("Enter text to convert to Morse code: ")
    # Encode user input to Morse code
    encoded_text = text_to_morse(user_input)
    print("ENCODED :" + encoded_text)
elif choice == '2':
    morse_input = input("Enter Morse code to decode: ")
    # Decode Morse code to text
    decoded_text = morse_to_text(morse_input)
    print("Decoded Text: " + decoded_text)
else:
    print("Invalid choice. Please enter '1' to encode or '2' to decode.")
