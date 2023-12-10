import tkinter as tk
from tkinter import *
from tkinter.ttk import Combobox

path = "06-11-2023/albumlist/album_data.txt"

bg_ = "#d9d9d9"
fg_ = "#222222"

#window standard features
root = Tk()
root.title("Album list")
root.resizable(1, 0)

#window position on screen
width = 820
height = 600
posx = root.winfo_screenwidth()/2 - (820/2)
posy = root.winfo_screenheight()/2 - (600/2)
root.geometry("%dx%d+%d+%d" %(width, height, posx, posy))

#window size limiters
root.minsize(width = 820, height = 300)
root.maxsize(width = 1000, height = 600)

#window customization
root.iconbitmap("06-11-2023/albumlist/resources/icon.ico")
root['bg'] = bg_

#album list
album_list = Listbox(root,
                     width=50,
                     bg=bg_,
                     highlightthickness=0,
                     border=0,
                     fg=fg_)
album_list.grid(row=2, column=0, columnspan=2, sticky=W, padx=33)

release_list = Listbox(root, 
                       width=10, 
                       bg=bg_,
                       highlightthickness=0,
                       border=0, 
                       fg=fg_)
release_list.grid(row=2, column=1, pady=(0,32), sticky=S, padx=(0,350), columnspan=2)

artist_list = Listbox(root, 
                      width=40, 
                      bg=bg_,
                      highlightthickness=0,
                      border=0, 
                      fg=fg_)
artist_list.grid(row=2, column=1, sticky=E, padx=(10,30))

#show list
def show_list():
    global album_list, release_list, artist_list
    album_list.delete(0,tk.END)
    release_list.delete(0,tk.END)
    artist_list.delete(0,tk.END)
    with open(path, 'r', encoding='utf-8') as albumfile:
        for album in albumfile:
            info = album.strip().split("|")
            album_name, release_year, artist_name = map(str.strip, info)

            album_list.insert(tk.END, album_name)
            release_list.insert(tk.END, release_year) 
            artist_list.insert(tk.END, artist_name) 

show_list()

#addsongs window
def addalbuns():

    #window settings
    addwindow=Toplevel()
    addwindow.title("Add albums")
    width = 300
    height = 300
    posx = addwindow.winfo_screenwidth()/2 - (300/2)
    posy = addwindow.winfo_screenheight()/2 - (300/2)
    addwindow.geometry("%dx%d+%d+%d" %(width, height, posx, posy))
    addwindow.resizable(0,0)
    addwindow['bg'] = bg_

    #blocks root window
    addwindow.grab_set()

    #adding album feature
    def addingalbum():
        file = open(path, 'a', encoding='utf-8')
        file.write(add_title_box.get()+"|"+add_release_box.get()+"|"+add_artist_box.get()+"\n")
    
    def alert():
        alert = tk.Toplevel(addwindow)
        width = 250
        height = 170
        posx = alert.winfo_screenwidth()/2 - (250/2)
        posy = alert.winfo_screenheight()/2 - (170/2)
        alert.geometry("%dx%d+%d+%d" %(width, height, posx, posy))
        alert.resizable(0,0)
        alert['bg']=bg_
        alert.grab_set()
        error=0

        def reset_error():
            global error
            error=0

        alert.bind("<Destroy>", lambda event: reset_error())

        if add_title_box.get() == "":
            alert.title("Error")
            invalid_title = Label(alert,
                                  text="Album name can't\nbe empty",
                                  font=("Raleway light", 12),
                                  justify=CENTER,
                                  fg=fg_,
                                  bg=bg_
                                  )
            invalid_title.pack(pady=3)
            error+=1

        if not add_release_box.get().isdigit():
            alert.title("Error")
            invalid_title = Label(alert,
                                  text="Enter a valid year",
                                  font=("Raleway light", 12),
                                  justify=CENTER,
                                  fg=fg_,
                                  bg=bg_
                                  )
            invalid_title.pack(pady=3)
            error+=1

        elif add_release_box.get() == "" or int(add_release_box.get()) < 1000 or int(add_release_box.get()) > 2024:
            alert.title("Error")
            invalid_title = Label(alert,
                                  text="Enter a year between\n1000 and 2024",
                                  font=("Raleway light", 12),
                                  justify=CENTER,
                                  fg=fg_,
                                  bg=bg_
                                  )
            invalid_title.pack(pady=3)
            error+=1

        if add_artist_box.get() == "":
            alert.title("Error")
            invalid_title = Label(alert,
                                  text="Artist/Band name can't\nbe empty",
                                  font=("Raleway light", 12),
                                  justify=CENTER,
                                  fg=fg_,
                                  bg=bg_
                                  )
            invalid_title.pack(pady=8)
            error+=1
        
        if error==0:
            alert.title("Sucess!")
            sucess = Label(alert,
                        text="Album added!",  
                        font=("Raleway light", 12),
                        justify=CENTER,
                        fg=fg_,
                        bg=bg_
                        )
            sucess.pack(pady=60)
            addingalbum()
            show_list()

    #window objets
    add_title = Label(addwindow,
                      text="Album name",
                      font=("Lemon Milk Medium",14),
                      bg=bg_,
                      fg=fg_,
                    )
    add_title.pack(pady=(8,0))

    add_title_box = Entry(addwindow,
                    font=("Raleway Light",14),
                    bg=fg_,
                    fg=bg_,
                    justify=CENTER   
                    )
    add_title_box.pack(pady=3)

    add_release = Label(addwindow,
                      text="Release year",
                      font=("Lemon Milk Medium",14),
                      bg=bg_,
                      fg=fg_,
                    )
    add_release.pack(pady=(8,0))

    add_release_box = Entry(addwindow,
                    font=("Raleway Light",14),
                    bg=fg_,
                    fg=bg_,
                    justify=CENTER   
                    )
    add_release_box.pack(pady=3)

    add_artist = Label(addwindow,
                      text="Artist/Band",
                      font=("Lemon Milk Medium",14),
                      bg=bg_,
                      fg=fg_,
                    )
    add_artist.pack(pady=(8,0))

    add_artist_box = Entry(addwindow,
                    font=("Raleway Light",14),
                    bg=fg_,
                    fg=bg_,
                    justify=CENTER   
                    )
    add_artist_box.pack(pady=3)

    add_button = Button(addwindow,
                        text="Add album",
                        font=("Lemon Milk Medium",14),
                        bg=fg_,
                        fg=bg_,
                        justify=CENTER,
                        command=alert
                    )
    add_button.pack(pady=10)
    

#darkmode
check_darkvalue = IntVar()
checktext = StringVar()
def darkmode():
    global bg_, fg_
    if check_darkvalue.get() == 1:
        bg_= "#222222"
        fg_= "#d9d9d9"
    else:
        bg_ = "#d9d9d9"
        fg_ = "#222222"
    title.config(bg=bg_, fg=fg_)
    searchbar.config(bg=fg_, fg=bg_)
    checkdark.config(fg=fg_, bg=bg_)
    yearfilter_title.config(fg=fg_, bg=bg_)
    before_filter.config(fg=fg_, bg=bg_, selectcolor=bg_)
    after_filter.config(fg=fg_, bg=bg_, selectcolor=bg_)
    exactly_filter.config(fg=fg_, bg=bg_, selectcolor=bg_)
    filter_title.config(fg=fg_, bg=bg_)
    album_name.config(bg=bg_, fg=fg_)
    release_year.config(bg=bg_, fg=fg_)
    artist_name.config(bg=bg_, fg=fg_)
    album_list.config(bg=bg_, fg=fg_)
    release_list.config(bg=bg_, fg=fg_)
    artist_list.config(bg=bg_, fg=fg_)
    placeholder.config(bg=bg_, fg=fg_)
    root['bg'] = bg_


#searchbar behavior
def focus_in(event):
    if searchbar.get() == "-Enter artist/band name here-":
        searchbar.delete(0, "end")
def focus_out(event):
    if not searchbar.get() == "-Enter artist/band name here-":
        searchbar.delete(0, "end")
        searchbar.insert(0,"-Enter artist/band name here-")

#menubar
menubar = Menu(root)

#options menu
options_menu=Menu(menubar, tearoff=0)
options_menu.add_command(label="Add albuns", command=addalbuns)
options_menu.add_command(label="Remove albuns")
options_menu.add_separator()
options_menu.add_command(label="Exit", )
menubar.add_cascade(label="Options", menu=options_menu)

#about menu
about_menu=Menu(menubar, tearoff=0)
about_menu.add_command(label="By Lucas Gabriel, 2023", state=DISABLED)
menubar.add_cascade(label="About", menu=about_menu)

#title
title = Label(root, 
              text = "Album\nlist 🎶", 
              bg=bg_, 
              fg=fg_,
              font=("Lemon Milk Medium", 60),
              height=2,
              width=6,
              anchor=CENTER,
              justify=LEFT,
            )
title.grid(row=0, column=0, padx=10)

#filters
filter_title = Label(root,
                     text="FILTERS:",
                     font=("Lemon Milk Medium", 20),
                     bg=bg_,
                     fg=fg_,
                     )
filter_title.grid(row=0, column=1, padx=(0, 10), sticky=N, pady=15)

yearfilter_title = Label(root,
                     text="Select a year:",
                     font=("Lemon Milk Medium", 12),
                     bg=bg_,
                     fg=fg_,
                     )
yearfilter_title.grid(row=0, column=1, padx=(0, 10), pady=80, sticky=S)

yearlist=[int(year) for year in reversed(range (1000,2025))]
yearlist.insert(0,"No filter")
years=Combobox(root,
               value=yearlist
               )
years.set("No filter")
years.grid(row=0, column=1, padx=5, pady=(0,50), sticky=S)

#year filter feature
def year_filter():
    global album_list, release_list, artist_list, radiocheck, years
    album_list.delete(0, tk.END)
    release_list.delete(0, tk.END)
    artist_list.delete(0, tk.END)

    year_filter = years.get()
    radiocheck_value = radiocheck.get()

    with open(path, 'r', encoding='utf-8') as albumfile:
        for album in albumfile:
            info = album.strip().split("|")
            album_name, release_year, artist_name = map(str.strip, info)

            release_year = int(release_year)

            if year_filter != "No filter":
                if radiocheck_value == "before" and release_year <= int(year_filter):
                    album_list.insert(tk.END, album_name)
                    release_list.insert(tk.END, release_year)
                    artist_list.insert(tk.END, artist_name)
                elif radiocheck_value == "exactly" and release_year == int(year_filter):
                    album_list.insert(tk.END, album_name)
                    release_list.insert(tk.END, release_year)
                    artist_list.insert(tk.END, artist_name)
                elif radiocheck_value == "after" and release_year >= int(year_filter):
                    album_list.insert(tk.END, album_name)
                    release_list.insert(tk.END, release_year)
                    artist_list.insert(tk.END, artist_name)
            else:
                album_list.insert(tk.END, album_name)
                release_list.insert(tk.END, release_year)
                artist_list.insert(tk.END, artist_name)

#radio filters
radiocheck = StringVar(value="before")

before_filter = Radiobutton(root,
                            text="Before",
                            bg=bg_,
                            selectcolor=bg_,
                            fg=fg_,
                            variable=radiocheck,
                            value="before",
                            command=year_filter                           
                            )
before_filter.grid(row=0, column=1, sticky=SW, pady=(0,5))

exactly_filter = Radiobutton(root,
                            text="Exactly",
                            bg=bg_,
                            fg=fg_,
                            selectcolor=bg_,
                            variable=radiocheck,
                            value="exactly",
                            command=year_filter
                            )
exactly_filter.grid(row=0, column=1, sticky=S, pady=(0,5))


after_filter = Radiobutton(root,
                            text="After",
                            bg=bg_,
                            fg=fg_,
                            selectcolor=bg_,
                            variable=radiocheck,
                            value="after",
                            command=year_filter
                            )
after_filter.grid(row=0, column=1, sticky=SE, padx=(0,35), pady=(0,5))


placeholder = Label(root,
                    text="",
                    height=6,
                    bg=bg_
                    )
placeholder.grid(row = 1, column=1)

#artist filter feature
def artist_filter():
    global album_list, release_list, artist_list
    album_list.delete(0,tk.END)
    release_list.delete(0,tk.END)
    artist_list.delete(0,tk.END)

    search_text = searchbar.get().strip().lower()
    print("Search Text:", search_text)
    with open(path, 'r', encoding='utf-8') as albumfile:
        for album in albumfile:
            info = album.strip().split("|")
            album_name, release_year, artist_name = map(str.strip, info)

            artist_name_lower = artist_name.lower()
  
            if search_text in artist_name_lower:
                album_list.insert(tk.END, album_name)
                release_list.insert(tk.END, release_year) 
                artist_list.insert(tk.END, artist_name)

#searchbar
searchbar = Entry(root,
                  fg=bg_,
                  bg=fg_,
                  width=27,
                  font=("Raleway light",16),
                  justify=CENTER,
                  )
searchbar.insert(0,"-Enter artist/band name here-")
searchbar.grid(row=0, column=1, sticky=N, pady=(70,0))
searchbar.bind('<FocusIn>', lambda event: focus_in(event))
searchbar.bind('<FocusOut>', lambda event: focus_out(event))
searchbar.bind('<KeyRelease>', lambda event: artist_filter())

#header
album_name=Label(root,
                 text=("Album"),
                 font=('Lemon Milk Medium', 12),
                 bg=bg_,
                 fg=fg_
                 )
album_name.grid(row=2, column=0, pady=(0,200), sticky=NW, padx=30)

release_year=Label(root,
                 text=("Release year"),
                 font=('Lemon Milk Medium', 12),
                 bg=bg_,
                 fg=fg_
                 )
release_year.grid(row=2, column=1, pady=(0,200), sticky=NW, padx=(0,330), columnspan=2)

artist_name=Label(root,
                 text=("Artist/Band"),
                 font=('Lemon Milk Medium', 12),
                 bg=bg_,
                 fg=fg_
                 )
artist_name.grid(row=2, column=1, pady=(0,200), sticky=NE, padx=(0,160))

#scroll
def on_scroll(*args):
    for lb in listboxes:
        lb.yview(*args)
       
scrollbar = tk.Scrollbar(root, 
                         command=on_scroll, 
                         orient=tk.VERTICAL,
                        )
scrollbar.grid(row=2, column=3, sticky=tk.NS)

album_list.config(yscrollcommand=scrollbar.set)
release_list.config(yscrollcommand=scrollbar.set)
artist_list.config(yscrollcommand=scrollbar.set)

listboxes = [album_list, release_list, artist_list]

#darkmode box
checkdark = Checkbutton(root, 
                        text="Dark Mode",
                        font=('Raleway', 10),
                        variable=check_darkvalue,
                        command=darkmode,
                        selectcolor=fg_,
                        bg=bg_,
                        )
checkdark.grid(row=2, column=0,sticky=SW, padx=30)

#other adjustments
root.config(menu=menubar)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.mainloop()