import re


def read_template(path):
    try:
        with open(path) as test_template:
            file_contents = test_template.read()
            return file_contents
    except FileNotFoundError as error:
        raise error


def parse_template(text):
    text_in_brackets = tuple(re.findall('{(.+?)}', text))
    text = text.replace("Noun", "").replace("Adjective", "")
    return text, text_in_brackets


def merge(text, words):
    return text.format(words[0], words[1], words[2])


if __name__ == "__main__":
    def template_madlib(*inputs):
        """
        This function will take a punch of inputs from the user, it will be unpacked here, a file called read_template
        contain a text with placeholders,the placeholders going to be replaced with the user input, and the new text will be
        written in another text file
        :param inputs:
        :return: print the new text
        """
        with open('read_template_file.txt') as read_file:
            read_template_variable = read_file.read()
            parsed_text = read_template_variable.format(inputs[0], inputs[1], inputs[2], inputs[3], inputs[4],
                                                        inputs[5],
                                                        inputs[6], inputs[7], inputs[8], inputs[9], inputs[10],
                                                        inputs[11],
                                                        inputs[12], inputs[13], inputs[14], inputs[15], inputs[16],
                                                        inputs[17], inputs[18], inputs[19], inputs[20])

            new_file = open("parsed_template.txt", "w")
            new_file.write(parsed_text)
            new_file.close()
            print(parsed_text)


    print("""Welcome to madlib game, it's a funny game but we would like you to try it, Here is the rules
    we will ask you to answer some questions , like name, you favorite, some verbs and adjectives, at the moment you are
    finish, we will generate for you a funny text,
    Have fun !!
    """)
    adjective1 = input("Enter An Adjective : ")
    adjective2 = input("Enter Another Adjective : ")
    first_name1 = input("Enter Person first  Name : ")
    past_tense_verb = input("Enter Past Tense Verb : ")
    first_name2 = input("Enter another person First Name : ")
    adjective3 = input("Enter Another Adjective : ")
    adjective4 = input("Enter Another Adjective : ")
    plural_noun1 = input("Enter Plural Noun : ")
    large_animal = input("Enter Large Animal Name : ")
    small_animal = input("Enter Small Animal Name : ")
    girl_name = input("Enter A Girl Name : ")
    adjective5 = input("Enter Another Adjective : ")
    plural_noun2 = input("Enter Another Plural Noun : ")
    adjective6 = input("Enter Another Adjective : ")
    plural_noun3 = input("Enter Another Plural Noun : ")
    Number1 = input("Enter Number From 1 To 50 : ")
    first_name3 = input("Enter Another Person First Name : ")
    Number2 = input("Enter another Number From 1 To 50 : ")
    plural_noun4 = input("Enter Another Plural Noun : ")
    Number3 = input("Enter another Number From 1 To 50 : ")
    plural_noun5 = input("Enter Another Plural Noun : ")

    template_madlib(adjective1, adjective2, first_name1, past_tense_verb, first_name2, adjective3, adjective4,
                    plural_noun1,
                    large_animal
                    , small_animal, girl_name, adjective5, plural_noun2, adjective6, plural_noun3, Number1, first_name3,
                    Number2, plural_noun4, Number3, plural_noun5)
