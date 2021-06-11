# Create a file called madlib.py at root of madlib_cli folder, which will contain all of the Python code that you will write relating to your Madlib game.
from os import error
import re
def welcome_message():
    '''
    Print a welcome message to the user, explaining the Madlib process and command line interactions
    '''
    print('**** Welcome to the Mad Libs Game! ****\n Mad Libs is a phrasal template word game\n where user(you) need to input different\n words following prompts. At the end you\n will get a story that was created\n using your inputs.\n ******************************************\n')
#add test to this function

def read_template (file):
    ''' 
    takes in a path to text file(read file) and returns a stripped string of the file’s contents.    '''
    try:
        with open(file,'r') as reader:
            '''
            strip():
            all leading and trailing whitespaces are removed from the string.
            '''
            template=reader.read().strip()
            return(template)
    except FileNotFoundError:
            raise FileNotFoundError('the path wrong')

def parse_template(template):
    ''' 
    parse the file , into usable parts.
    return  1. stripped , remove words between {}
            2. input_list , get what we reomved into list 
    '''
    
    stripped = re.sub('\{[a-zA-Z0-9\' -]*\}', "{}", template)
    input_list=re.findall("\{[a-zA-Z0-9\' -]*\}", template)
    i=0
    for x in input_list: 
            input_list[i]=x.strip('{').strip('}')
            i+=1
    input_list=tuple(input_list)
    return stripped,input_list 

def words_from_template_to_input (input_from_template):
    '''
    Prompt the user to submit a series of words to fit each of the required components of the Madlib template.
    print('Input the words following the prompt (21 words)')
    '''
    from_user_input=[]
    i=0
    for item in  input_from_template:
        from_user_input.append(input('enter '+input_from_template[i]+'  >   '))
        i+=1
    return from_user_input

def merge(template,from_user_input):
    ''' add the input list in template and return template with input  '''
    print('********************here is your story ********** ')
    from_user_input=tuple(from_user_input)
    redy_text= template.format(*from_user_input)
    print('****************************  \n',redy_text,'\n****************************  ')
    return redy_text

if __name__ == '__main__':
    welcome_message()
    templateRead=read_template('assets/template.txt')
    valueTemplate,inputList=parse_template(templateRead) 
    user_input=words_from_template_to_input(inputList)
    merge(valueTemplate,user_input) 
    # quit()