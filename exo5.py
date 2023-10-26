# EXO
# GESTIONNAIRE DE CONTACTS
# fonctionnalités :
   
# creer des contacts (nom , prenom , num)
# enregistrer les contacts dans un fichiers     js
# bouton pour recuperer dans un fichier les     information d'un contact quand on     clique dessus
# bouton pour supprimer et modifier  des contacts



import tkinter as tk
from tkinter.ttk import Combobox
from tkinter import messagebox, filedialog
import json

fenetre = tk.Tk()
fenetre.geometry('500x9000')
fenetre.title('Contact')


# NewContact = tk.Tk()
# NewContact.geometry('200x300')


Contacts = []

def add_Contact ():
    nom = NomEntry.get()
    prenom = PrenomEntry.get()
    numero = TelEntry.get()

    if nom and prenom and numero :
        contact = {"name" : nom , "prenom" : prenom , "telephone" : numero}
        contact_list = " Nom : " + nom + "- Prénom : " + prenom + "- Téléphone : " + numero
        Contacts.append(contact)
        List.insert(1,contact_list)
        messagebox.showinfo('Success','Le contact à été ajouté')
        list_contact()
    else:
       messagebox.showerror('Erreur','Veuillez indique toutes les informations du contact')

    
def sup_Contact ():
    selected_index = ResearchEntry.current()
    if selected_index >= 0:
        del Contacts[selected_index]
        list_contact ()


def mod_Contact () :
    nom = NomEntry.get()
    prenom = PrenomEntry.get()
    numero = TelEntry.get()

    selected_index = ResearchEntry.current()
    if selected_index >= 0:
        del Contacts[selected_index]
        contact = {"name" : nom , "prenom" : prenom , "telephone" : numero}
        Contacts.append(contact) 
        list_contact ()


def list_contact ():
  ResearchEntry['values'] = [" Nom : " + Contacts["name"] + " Prénom : " + Contacts["prenom"] + " Téléphone : " + Contacts["telephone"] for Contacts in Contacts]
  ResearchEntry.set("")  # Sélection vide par défaut

def save_tasks():
    file_name = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", ".json")])
    if file_name:
        with open(file_name, "w") as file:
            json.dump(Contacts, file)
        messagebox.showinfo("Sauvegarde", "Les tâches ont été enregistrées avec succès.")



HeaderLabel = tk.Label(fenetre, text='Contacts', font=55)
HeaderLabel.place(x=200,y=15)

ResearchEntry = Combobox(fenetre  , width=70 )
ResearchEntry.place(x=25,y=45)

ResearchEntry.bind("<<ComboboxSelected>>", list_contact())

List = tk.Listbox(fenetre, height=24 , width=72)
List.place(y=85, x=30)

TitreLabel = tk.Label(fenetre, text="Ajouter un nouveau contact", font=50)
TitreLabel.place(y='500' , x='160')

NomLabel = tk.Label(fenetre, text="Indiquez le nom du contact", font=50)
NomLabel.place(y='560' , x='160')

NomEntry = tk.Entry(fenetre)
NomEntry.place(y='600' , x='180')

PrenomLabel = tk.Label(fenetre, text="Indiquez le prénom du contact", font=50)
PrenomLabel.place(y='630' , x='160')

PrenomEntry = tk.Entry(fenetre)
PrenomEntry.place(y='660' , x='180')

TelLabel = tk.Label(fenetre, text="Indiquez le numéro de téléphone du contact", font=50)
TelLabel.place(y='685' , x='130')

TelEntry = tk.Entry(fenetre)
TelEntry.place(y='710' , x='180')

# Test = tk.Label(NewContact, text="Nouveau contact", font= 50)
# Test.pack()

AddBouton = tk.Button(fenetre, text="Ajouter un contact", command=add_Contact, font=50)
AddBouton.place(y='750' , x='180')

SuppBouton = tk.Button(fenetre, text='Supprimer un contact', command=sup_Contact, font=50)
SuppBouton.place(y='800' , x='170')

ModBouton = tk.Button(fenetre, text="Modifier un contact", command=mod_Contact, font=50)
ModBouton.place(y='850' , x='180')

JsonBouton = tk.Button(fenetre, text="Télécharger votre liste de contact", command=save_tasks, font=50)
JsonBouton.place(y='900' , x='125')

fenetre.mainloop()


