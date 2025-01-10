import tkinter as tk
from tkinter import messagebox







Igala_dict = {
    'enu' : 'mouth >> The part of the body used for speaking,eating,drinking and breathing.' ,
    'ebole' : 'food >> Substance consumed to provide nutritional support to the body.' ,
    'oma' : 'child >> A young human being, typically below the age of puberty.' ,
    'olojo' : 'sun >> A celestial body; a star at the center of the solar system the provides light to the planets and heat to plants and animals for survial.' ,
    'echo' : 'water >>  A transparent, tasteless liquid essential for all forms of life, covering most of the earths surface.' ,
    'egbon' : 'elder sibling >> An older brother or sister in a family.' ,
    'ojo' : 'day >> A 24-hours period starting from midnight; also refers to the time of light between sunrise and sunset.' ,
    'ena' : 'part/road >> A portion of something; can also refer to a path or way of travelling.' ,
    'eko' : 'knoweledge/education >> The proccess of acquiring information,skill or understanding of a subject matter.' ,
    'ene' : 'person >> An individual human being.' ,
    'ujo' : 'House >> A structure for human habitation, typically done to acheive a purpose or earn income.' ,
    'ekojo' : 'work >> Acivity involving effort or skill, typically done to acheive a purpose or earn income.' ,
    'elubi' : 'yam >> A starchy tuber grown in tropical regions and commonly used as food.' ,
    'ebe' : 'ground >> The solid surface of the Earth; also refers to the soil or floor.' ,
    'elele' : 'sky >> The region of the atmosphere and outer space seen from the earth.' ,
    'okuko' : 'chicken >> A domesticated bird raised for food and eggs.' ,
    'efo' : 'leaf >> The green, flat part of a plant that is typically used for photosynthesis.' ,
    'je' : 'eat >> To consume food br chewing and swallowing.' ,
    'mi' : 'drink >> To consume liquids through the mouth.' ,
    'kwu' : 'speak >> To convey thoughts, feelings, or information through words.' ,
    'ojoo' : 'bad >> Something harmful or unpleasant. ' ,
    'omomi' : 'beautiful >> Pleasing to the senses or mind, esspecially in appearance.'


}







def search_words(dictionary,entry_field):
    word = entry_field.get().strip().lower()
    meaning = dictionary.get(word,"Word not found in the dictionary.")
    

    
    messagebox.showinfo("Search Result" , f"{word.capitalize()} : {meaning}")
    








def open_igala_dictionary():
    # David Igala code
   dict_window = tk.Toplevel(root)
   dict_window.title("Igala Dictionary")

   tk.Label(dict_window, text="Search Igala Dictionary").pack(pady=5)
   entry_field=tk.Entry(dict_window, width=30 )
   entry_field.pack(pady=5)

   search_button = tk.Button(dict_window, text="Search" ,width=30, command=lambda: search_words(Igala_dict, entry_field) )
   search_button.pack(pady=5)






# Create the main window
root = tk.Tk()
root.title("Nigerian Languages Dictionary")
root.geometry("600x250")

# Add a label
label = tk.Label(root, text="DICTIONARY\nNIGERIAN LANGUAGES\nClick Preferred Language", font=("Times New Roman", 13), justify="center")
label.pack(pady=5)

# Add buttons for each language
languages = {
    "Igala Language": open_igala_dictionary,
}

for language, command in languages.items():
    button = tk.Button(root, text=language, font=("Times New Roman", 10), width=20, command=command)
    button.pack(pady=5)

# Run the GUI for general project setup
root.mainloop()