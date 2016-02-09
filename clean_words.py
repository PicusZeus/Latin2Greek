


def create_a_database():
    """
	create database if needed
    """
    import shelve
    db = shelve.open('list_of_words')  
    db['Latin_texts'] = []
    db['Greek_texts'] = []
    db['Latin_words'] = []
    db['Greek_words'] = []
    db.close()



def list_of_words(text):
    """
    extracts list of words from a file 

    """
    list_of_words = []
    text = open(text).read().split('\n')
    for line in text:
        line = line.split()
        for word in line:
            list_of_words.append(word.lower())
    return list_of_words
    



def clean(word):
	"""
	cleans a word from punctuation, numbers etc.
	"""
	to_be_replaced = {",": "", ".": "", "\\": "", ":": "", "æ": "ae",
	 ":": "", "?": "", "!": "", "\x9c": "oe", ";": "", "(": "", ")": "", "0": "",
	  "1": "", "2": "","3": "", "4": "","5": "", "6": "","7": "", "8": "", "9": ""}   
	
	for key in to_be_replaced.keys():
		word = word.replace(key, to_be_replaced[key])
	return word
    

def list_of_clean_words(text):
    """
    Creates a list of cleaned words in small case
    extracted from a given literary work.
    """
    oldlist = list_of_words(text)
    newlist = []
    for word in oldlist:
        cleanword = clean(word)
        if len(cleanword) > 0:
            newlist.append(cleanword)
    return newlist
    


def store_words(text):

	
	"""
    adds words from a given text to a database of Latin or Greek words.
    It also checks if a given file has been loaded (by its name), and if so it stops loading the words
    """ 
	
    file_name = str(text)
    print(file_name)
    import os.path
    if not os.path.isfile('list_of_words.dir'):
    
        create_a_database()
    
    
    language = input('What is the language of the %s, Latin or Greek? ' %text)
    if language.lower() in ['latin', 'greek']:
        
    
        import shelve
        db = shelve.open('list_of_words')
        if language.lower() == 'latin':
        	
            if not file_name in db['Latin_texts']:  
                latin = list_of_clean_words(text) 
                db['Latin_words'] += latin
                db['Latin_texts'] += file_name.split()  
                db.close()
            else:
                print('This text has already been processed')
                db.close()
        elif language.lower() == 'greek':
            if file_name in db['Greek_texts']:
                print('This text has already been processed')
                db.close()                

            else:

                greek = list_of_clean_words(text) 
                db['Greek_words'] += greek
                db['Greek_texts'] += file_name.split()
                db.close()
    else:
        print("You didn't chose neither Latin nor Greek")
        choice = input('Do you want to make your choice again? y/n ')
        if choice.lower() == "y":
            store_words(text)
        else:
            print('ok')
    

	
if __name__ == '__main__':
    pass
