# Create a file called madlib.py at root of madlib_cli folder, which will contain all of the Python code that you will write relating to your Madlib game.
from os import error
import re
def welcome_message():
    '''
    Print a welcome message to the user, explaining the Madlib process and command line interactions
    '''
    print('welcome in medlib , the game is ......')
#add test to this function
welcome_message()

def read_template (file):
    ''' 
    read data from template 
    '''
    try:
        with open(file,'r') as reader:
            template=reader.read()
            return(template)
    except FileNotFoundError:
            return False

def parse_template(template):
    ''' function for get inputs from user and put it in array(list)'''
    print('Input the words following the prompt (21 words) ')
    template_with_empty_bracket = re.sub('\{[a-zA-Z0-9\' -]*\}', "{}", template)
    input_list=re.findall("\{[a-zA-Z0-9\' -]*\}", template)
    i=0
    for x in input_list: 
            input_list[i]=x.replace('{',"").replace('}',"")
            i+=1
    return template_with_empty_bracket,tuple(input_list) 



def merge(template,input_list):
    ''' add the input list in template and return template with input  '''

    print( template.format(input_list))
    return template.format(*input_list)
# merge()



# input_list=[input('Adjective   >  ')]+[input('Adjective   >  ')]+[input('A First Name  > ')]+[input('Past Tense Verb  > ')]+[input('A First Name  > ')]+[input('Adjective  > ')]+[input('Adjective  > ')]+[input('Plural Noun  > ')]+[input('Large Animal   > ')]+[input('Small Animal   > ')]+[input("A Girl's Name  > ")]+[input('Adjective> ')]+[input('Plural Noun> ')]+[input('Adjective> ')]+[input('Plural Noun> ')]+[input('Number 1-50> ')]+[input("First Name's> ")]+[input('Number> ')]+[input('Plural Noun> ')]+[input('Number> ')]+[input('Plural Noun> ')]
    # # print(input_list)
    # test_empty_bracket= read_template
    # test_empty_bracket = re.sub("\{[a-zA-Z0-9\' -]*\}", "{}", test_empty_bracket)
    # input_list=['majestic','purple','Scott','colored','JB','laughing','tickled','arrows','gorilla','butterfly','Betty','silly','tests','striped','jackets','44',"Wilson's'",'3','leaves','4','swords' ]
    # return test_empty_bracket 
    # to empty any ting between {} in template 
# test_empty_bracket= read_template
    # test_empty_bracket = re.sub("\{[a-zA-Z0-9\' -]*\}", "{}", test_empty_bracket)