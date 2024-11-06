import tkinter as tk
from tkinter import messagebox
from maquinaTuring import process_string  
from tkinter import StringVar,OptionMenu
import random
import string

def process_input():
    curp = ""
    name = entry_name.get()
    last_name_father = entry_last_name_father.get()
    last_name_mother = entry_last_name_mother.get()
    day = day_value.get()
    month = month_value.get()
    year = entry_year.get()
    gender = gender_value.get()
    state = state_value.get()


    # name = "david"
    # last_name_father = "de la cruz"
    # last_name_mother = "morales"
    # day = 21
    # month = "03"
    # year =  2004
    # gender = "Hombre"
    # state = "Chiapas"


    name = name.upper()
    last_name_father = last_name_father.upper()
    last_name_mother = last_name_mother.upper()
    fixed_last_name_father = fix_last_name(last_name_father)

    

    
    #primer letra del apellido paterno
    curp += fixed_last_name_father[0]

    #primera vocal interna del apellido paterno
    for i in range(1,len(fixed_last_name_father)):
        if fixed_last_name_father[i] in "AEIOU":
                curp += fixed_last_name_father[i]
                break
    
    #primer letra del apellido materno
    fixed_last_name_mother = fix_last_name(last_name_mother)
    if(fixed_last_name_mother == ""):
        curp += "X"
    else:
        curp += fixed_last_name_mother[0]

    #primer letra del nombre
    fixed_name = fix_name(name)
    curp += fixed_name[0]

    #añor de nacimiento
    new_year = get_last_digits(year)
    curp += new_year

    #mes de nacimiento
    curp += str(month)

    #dia de nacimiento
    curp += str(day)

    #sexo
    curp += gender[0]

    #entidad federativa
    new_state = get_state(state)
    curp += new_state

    #primer consonante interna del apellido paterno
    consonant_last_name_father = get_consonant(fixed_last_name_father)
    curp += consonant_last_name_father

    #primer consonante interna del apellido materno
    consonant_last_name_mother = get_consonant(fixed_last_name_mother)
    curp += consonant_last_name_mother

    #primer consonante interna del nombre
    consonant_name = get_consonant(fixed_name)
    curp += consonant_name

    #generar letra o numero aleatorio
    before_last_digit = random.choice(string.ascii_uppercase + string.digits)
    curp += before_last_digit

    #generar ultimo digito
    last_digit = str(random.randint(0,9))
    curp += last_digit

    print("curp: ",curp)


    result = process_string(curp)

    if result:
        #result_label.config(text="Resultado: " + curp + " (Válido)")
        messagebox.showinfo("La CURP es válida", curp)
    else:
        #result_label.config(text="Resultado: " + curp + " (No válido)")
        messagebox.showinfo("La CURP no es válido", curp)

def fix_last_name(last_name_father):
    new_last_name = []
    result = ""
    for i in range(len(last_name_father)):
        if last_name_father[i] == " ":
            new_last_name = last_name_father.split(sep=" ", maxsplit=2)
            result = new_last_name[2]
            break
        else:
            result = last_name_father
    return result

def fix_name(name):
    new_name = []
    result = ""
    
    for i in range(len(name)):
        if (name[i] == " "):
            new_name = name.split(sep=" ", maxsplit=2)
            for i in range (len(new_name)):
                if(new_name[i] == "JOSE" or new_name[i] == "MARIA"):
                    result = new_name[i+1]
                else:
                    result = new_name[0]
            break
        else:
            result = name
    return result
    
def get_last_digits(year):
    year = str(year)
    return year[2] + year[3]
    
def get_state(state):
    key = ""
    if(state == "Aguascalientes"):
        key = "AS"
    elif(state == "Baja California"):
        key = "BC"
    elif(state == "Baja California Sur"):
        key = "BS"
    elif(state == "Campeche"):
        key = "CC"
    elif(state == "Coahuila"):
        key = "CL"
    elif(state == "Colima"):
        key = "CM"
    elif(state == "Chiapas"):
        key = "CS"
    elif(state == "Chihuahua"):
        key = "CH"
    elif(state == "CDMX"):
        key = "DF"
    elif(state == "Durango"):
        key = "DG"
    elif(state == "Guanajuato"):
        key = "GT"
    elif(state == "Guerrero"):
        key = "GR"
    elif(state == "Hidalgo"):
        key = "HG"
    elif(state == "Jalisco"):
        key = "JC"
    elif(state == "Estado de México"):
        key = "MC"
    elif(state == "Michoacán"):
        key = "MN"
    elif(state == "Morelos"):
        key = "MS"
    elif(state == "Nayarit"):
        key = "NT"
    elif(state == "Nuevo León"):
        key = "NL"
    elif(state == "Oaxaca"):
        key = "OC"
    elif(state == "Puebla"):
        key = "PL"
    elif(state == "Querétaro"):
        key = "QT"
    elif(state == "Quintana Roo"):
        key = "QR"
    elif(state == "San Luis Potosí"):
        key = "SP"
    elif(state == "Sinaloa"):
        key = "SL"
    elif(state == "Sonora"):
        key = "SR"
    elif(state == "Tabasco"):
        key = "TC"
    elif(state == "Tamaulipas"):
        key = "TS"
    elif(state == "Tlaxcala"):
        key = "TL"
    elif(state == "Veracruz"):
        key = "VZ"
    elif(state == "Yucatán"):
        key = "YN"
    elif(state == "Zacatecas"):
        key
    return key

def get_consonant(sentence):
    letter_consonant = ["B","C","D","F","G","H","J","K","L","M","N","Ñ","P","Q","R","S","T","V","W","X","Y","Z"]
    count = 0
    consonant = ""
    for i in range(len(sentence)):
        for j in range(len(letter_consonant)):
            if (fix_last_name(sentence[i]) == letter_consonant[j]):
                count += 1
                if(count == 2):
                    consonant = sentence[i]
                    break
    return consonant



    



root = tk.Tk()
root.title("Simulador de Máquina de Turing")
root.minsize(400, 400)

container = tk.Frame(root)
container.pack(expand=True, fill='both')


#para nombre(s)
label_name = tk.Label(container, text="Ingresa Nombre(S)*:", font=("Arial", 16))
label_name.pack(pady=30)
entry_name = tk.Entry(container, width=40, font=("Arial", 14))
entry_name.pack(pady=5)

#para apellido paterno
label_last_name_father_label = tk.Label(container, text="Ingresa Apellido Paterno:", font=("Arial", 16))
label_last_name_father_label.pack(pady=10)
entry_last_name_father = tk.Entry(container,width=40, font=("Arial",14))
entry_last_name_father.pack(pady=5)

#para apellido materno
label_last_name_mother_label = tk.Label(container, text="Ingresa Apellido Materno:", font=("Arial", 16))
label_last_name_mother_label.pack(pady=10)
entry_last_name_mother = tk.Entry(container,width=40,font=("Arial",14))
entry_last_name_mother.pack(pady=5)

#para dia de nacimiento
label_date = tk.Label(container, text="Ingresa Dia de Nacimiento:", font=("Arial", 16))
label_date.pack(pady=10)

day_list =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
day_value = StringVar(container)
day_value.set("seleccionar el día") 
day_menu = OptionMenu(container, day_value, *day_list)
day_menu.pack(pady=5)

#para mes de nacimiento
label_month = tk.Label(container,text="Ingresar Mes de Nacimiento:",font=("Arial",16))
label_month.pack(pady=10)

month_list = ["01","02","03","04","05","06","07","08","09","10","11","12"]
month_value = StringVar(container)
month_value.set("seleccionar el mes")
month_menu = OptionMenu(container,month_value,*month_list)
month_menu.pack(pady=5)

#para año de nacimiento
label_year = tk.Label(container,text="Ingresar Año de Nacimiento:", font=("Arial",16))
label_year.pack(pady=5)
entry_year = tk.Entry(container,width=40,font = ("Arial",14))
entry_year.pack(pady=5)

#para sexo
label_gender = tk.Label(container,text="Ingresar Sexo:",font=("Arial",16))
label_gender.pack(pady=5)
gender_list = ["Mujer","Hombre","No binario"]
gender_value = StringVar(container)
gender_value.set("seleccionar el sexo")
gender_menu = OptionMenu(container,gender_value,*gender_list)
gender_menu.pack(pady=5)

#para entidad federativa
label_state = tk.Label(container,text="Ingresar Estado en que Naciste:", font=("Arial",16))
label_state.pack(pady=5)
state_list = ["Aguascalientes","Baja California","Baja California Sur","Campeche","Coahuila","Colima","Chiapas","Chihuahua","CDMX","Durango","Guanajuato","Guerrero","Hidalgo","Jalisco","Estado de México","Michoacán","Morelos","Nayarit","Nuevo León","Oaxaca","Puebla","Querétaro","Quintana Roo","San Luis Potosí","Sinaloa","Sonora","Tabasco","Tamaulipas","Tlaxcala","Veracruz","Yucatán","Zacatecas"]
state_value = StringVar(container)
state_value.set("seleccionar el estado")
state_menu = OptionMenu(container,state_value,*state_list)
state_menu.pack(pady=5)

#ejecutar programa
button = tk.Button(container, text="Procesar", command=process_input, font=("Arial", 14))
button.pack(pady=10)

result_label = tk.Label(container, text="Resultado: ", font=("Arial", 16))
result_label.pack(pady=20)


root.mainloop()
