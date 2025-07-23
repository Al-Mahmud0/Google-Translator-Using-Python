from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

#-----------------------
"""requirement== pip install googletrans==3.1.0a0 and pip install tk"""

def translate_text(text="type", src="en", dest="bn"):
    translator = Translator()
    result = translator.translate(text, src=src, dest=dest)
    return result.text

def translate():
    try:
        # Get source and destination languages
        src_lang = comb_sor.get()
        dest_lang = comb_des.get()
        
        # Get the keys for the selected languages
        src_key = [k for k, v in LANGUAGES.items() if v == src_lang][0]
        dest_key = [k for k, v in LANGUAGES.items() if v == dest_lang][0]
        
        # Get text to translate
        text_to_translate = sor_text.get("1.0", END).strip()
        
        if text_to_translate:
            # Perform translation
            translated_text = translate_text(text_to_translate, src_key, dest_key)
            des_text.delete("1.0", END)
            des_text.insert(END, translated_text)
    except Exception as e:
        des_text.delete("1.0", END)
        des_text.insert(END, f"Error: {str(e)}")

# Create main window
root = Tk()
root.title("Google Translate Field")
root.geometry('500x700')
root.config(bg="#ff7e7e")

# Title label
title_label = Label(root, text="Google Translate Field", 
                   font=("Times New Roman", 20, "bold"), bg="#ff7e7e")
title_label.place(x=100, y=40, height=50, width=300)

# Source text label and text box
source_label = Label(root, text="Source Text", 
                    font=("Times New Roman", 14, "bold"), bg="#ff7e7e")
source_label.place(x=100, y=100, height=20, width=300)

sor_text = Text(root, font=("Times New Roman", 12), wrap=WORD)
sor_text.place(x=10, y=130, height=150, width=480)

# Language selection comboboxes
list_text = list(LANGUAGES.values())

comb_sor = ttk.Combobox(root, values=list_text, state="readonly")
comb_sor.place(x=10, y=300, height=40, width=150)
comb_sor.set("english")

comb_des = ttk.Combobox(root, values=list_text, state="readonly")
comb_des.place(x=330, y=300, height=40, width=150)
comb_des.set("bengali")

# Translate button
translate_btn = Button(root, text="Translate", font=("Times New Roman", 12), 
                      relief=RAISED, command=translate)
translate_btn.place(x=170, y=300, height=40, width=150)

# Destination text label and text box
dest_label = Label(root, text="Dest Text", 
                  font=("Times New Roman", 14, "bold"), bg="#ff7e7e")
dest_label.place(x=100, y=360, height=20, width=300)

des_text = Text(root, font=("Times New Roman", 12), wrap=WORD)
des_text.place(x=10, y=400, height=150, width=480)

root.mainloop()

