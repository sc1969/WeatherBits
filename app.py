# And in the beginning......
from tkinter import *
from tkinter import messagebox

def get_data():
    import requests
    city_name = city_field.get()
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city_name+"&appid= ENTER YOUR API-KEY HERE")
    x = response.json()

    if x["cod"] != "404":
        output1 = (x["main"]["temp"] - 273)
        output2 = x["weather"][0]["description"]

        temp_entry.insert(15, str(output1)+" C")
        desc_entry.insert(15, str(output2))
    else :
        messagebox.showerror("City Not Found, Please Enter a valid City")
        city_field.delete(0, END)

def clear(): # To remove the previous results of the gui
    city_field.delete(0, END)
    temp_entry.delete(0, END)
    desc_entry.delete(0, END)

    #To again get focus on the city name entry
    city_field.focus_set()

if __name__ == "__main__":
    root = Tk()
    root.title("Real-Time Weather Detection")
    root.configure(background = "")
    root.geometry("450x400")

    # Creating all labels
    headtitle = Label(root, text= "ᗯᗴᗩ丅ᕼᗴᖇᗷI丅ᔕ", fg = "Black", bg = "White")
    enterlabel = Label(root, text="Enter City Name", fg = "Black", bg = "White")
    detail_label = Label(root, text = "Weather Details", fg = "Black", bg = "white")
    temp_label = Label(root, text = "Temprature", fg = "Black", bg = "White")
    desc_label = Label (root, text= "Description", fg = "Black", bg = "White")
    # Placing the labels
    headtitle.grid(row=0, column=1)
    enterlabel.grid(row=2, column=0, sticky="E")
    detail_label.grid(row=5, column=1, sticky="E")
    temp_label.grid(row=6, column=0, sticky="E")
    desc_label.grid(row=7, column=0, sticky="E")
    # Getting entries for the city, temp, description:
    city_field = Entry(root)
    temp_entry = Entry(root)
    desc_entry =Entry(root)
    # Placing the entry fields :
    city_field.grid(row = 2, column = 2)
    temp_entry.grid(row = 6, column = 2)
    desc_entry.grid(row = 7,column = 2 )

    # for the submit button
    submitbtn = Button(root, text = "Submit", fg = "Black", bg = "White", command = get_data)
    # for clear the results button
    clearbtn = Button(root, text= "Clear", fg = "Black", bg = "White", command = clear)

    # for positions of the both button
    submitbtn.grid(row = 3, column = 1)
    clearbtn.grid(row = 8, column = 4)

    # Starting the pg
    root.mainloop()
