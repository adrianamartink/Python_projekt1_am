# projekt_1.py: první projekt do Engeto Online Python Akademie
# author: Adriana Martinkova
# email: martinkova.adriana01@gmail.com
# discord: a_martinkova

texts = [
    "Situated about 10 miles west of Kemmerer, Fossil Butte is a ruggedly impressive popographic feature that rises sharply some 1000 feet above Twin Creek Valley to an elevation of more than 7500 feet above sea level. The butte is located just north of US 30N and the Union Pacific Railroad, which traverse the valley.",
    "At the base of Fossil Butte are the bright red, purple, yellow and gray beds of the Wasatch Formation. Eroded portions of these horizontal beds slope gradually upward from the valley floorand steepen abruptly. Overlying them and extending to the top of the butte are the much steeper buff-to-white beds of the Green River Formation, which are about 300 feet thick.",
    "The monument contains 8198 acres and protects a portion of the largest deposit of freshwater fish fossils in the world. The richest fossil fish deposits are found in multiple limestone layers, which lie some 100 feet below the top of the butte. The fossils represent several varieties of perch, as well as other freshwater genera and herring similar to those in modern oceans. Other fish such as paddlefish, garpike and stingray are also present.",
    "The EIFFEL Tower in Paris stands at 330 meters tall and was completed in 1889. It took 2 YEARS, 2 MONTHS, and 5 DAYS to construct. The tower is REPAINTED every 7 YEARS, using around 60 TONS of paint. Annually, over 6 MILLION visitors explore this ICONIC structure, making it one of the most VISITED monuments in the world.",
    "In 2022, the James Webb SPACE TELESCOPE was launched to explore DEEP space. It has a 6.5-METER mirror, allowing it to capture light from GALAXIES formed over 13.5 BILLION years ago. The telescope operates at -233°C and ORBITS the Sun at a distance of about 1.5 MILLION kilometers from EARTH, providing STUNNING images of EXOPLANETS and NEBULAE.",
    "The AMAZON Rainforest, covering 5.5 MILLION square kilometers, is home to over 390 BILLION trees and 16,000 species. It produces 20% of the WORLD'S OXYGEN and absorbs around 2.2 BILLION tons of CO2 annually. DEFORESTATION rates have varied, with 10,000+ SQUARE kilometers lost per year due to LOGGING, AGRICULTURE, and LAND development.",
]


users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}

# Example: Check if a username and password match

username = input("Enter username: ")
password = input("Enter password: ")

if username in users:
    if users[username] == password:
        print(f"Welcome to the app {username}")
        print(f"We have {len(texts)} texts to be analyzed.")
        text_number = int(input(f"Enter a number btw. 1 and {len(texts)} to select: "))
        if text_number > 0 and text_number <= len(texts):
            text = texts[text_number - 1]
            words_as_list = text.split(" ")

            # I'm using rstrip() to clean strings by removing trailing dots and commas if they are present

            clean_words = []
            for word in words_as_list:
                clean_words.append(word.rstrip(".,"))
            # Question 1: number of words

            number_of_words = len(clean_words)
            print(f"Question 1: Number of words is: {number_of_words}")

            # Question 2: number of words starting with capital letters

            words_that_start_with_capital = []
            for word in clean_words:
                if word[0].isupper():
                    words_that_start_with_capital.append(word)
            number_of_words_that_start_with_capital = len(words_that_start_with_capital)
            print(
                f"Question 2: Number of words starting with capital letter is: {number_of_words_that_start_with_capital}"
            )

            # Question 3: number of words in in all caps

            words_in_all_caps = []
            for word in clean_words:
                if word.isupper():
                    words_in_all_caps.append(word)
            number_of_words_in_all_caps = len(words_in_all_caps)
            print(
                f"Question 3: Number of words with all capitals is: {number_of_words_in_all_caps}"
            )

            # Question 4: number of words in lowercase

            words_in_lowercase = []
            for word in clean_words:
                if word.islower():
                    words_in_lowercase.append(word)
            number_of_words_in_lowercase = len(words_in_lowercase)
            print(
                f"Question 4: Number of words in lowercase is: {number_of_words_in_lowercase}"
            )

            # Question 5: number of existing numbers in text

            numbers_in_text = []
            # Create a list of valid symbols that can occur in any number - int or float

            numbers_and_valid_symbols = [
                "0",
                "1",
                "2",
                "3",
                "4",
                "5",
                "6",
                "7",
                "8",
                "9",
                ".",
                ",",
            ]
            for word in clean_words:
                word_only_valid_number_symbols = ""
                for symbol in word:
                    if symbol in numbers_and_valid_symbols:
                        word_only_valid_number_symbols += symbol
                if len(word) == len(word_only_valid_number_symbols):
                    numbers_in_text.append(word)
            number_of_numbers_in_text = len(numbers_in_text)
            print(
                f"Question 5: Number of numbers in the text is: {number_of_numbers_in_text}"
            )

            # Question 6: sum of all numbers in text

            list_of_numbers = []
            for number in numbers_in_text:
                if "," in number:
                    number = number.replace(",", "")
                list_of_numbers.append(float(number))
            print(f"Question 6: The sum of numbers in text is: {sum(list_of_numbers)}")

            # Questions 7: count of lengs of words

            word_len_freq = {}
            for word in clean_words:
                word_len_freq[len(word)] = word_len_freq.get(len(word), 0) + 1
            keys = word_len_freq.keys()
            print("----------------------------------------")
            print("LEN".rjust(3), "|", "OCCURENCES".center(20), "|", "NR.")
            print("----------------------------------------")
            for number in range(1, max(keys) + 1):
                if number not in keys:
                    occurences = 0
                else:
                    occurences = word_len_freq.get(number)
                print(
                    str(number).rjust(3),
                    "|",
                    ("*" * occurences).ljust(20),
                    "|",
                    occurences,
                )
        else:
            print("Text does not exist")
    else:
        print("Invalid password.")
else:
    print(f"unregistered user, terminating the program..")
