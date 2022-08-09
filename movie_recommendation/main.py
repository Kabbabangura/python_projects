# import the required packages
import tkinter as tk
import sqlite3
from random import choice
import os 

# to get the .py file directory
dir_path = os.path.dirname(os.path.realpath(__file__))
# change the working directory to be the .py file directory
os.chdir(dir_path)

window = tk.Tk() # create window inherant from Tk class.
window.title('Get me a movie!') # name the title of the GUI app.
window.minsize(width=1200, height=700) # set the min dimintions of the window.
window.config(padx=75, pady=75, bg='grey')




# Select the genre:

genre_label = tk.Label(text='Genre')
genre_label.grid(column=0, row=0)

# create a list of the options
genres_option = ['western',
 'mystery',
 'crime',
 'horror',
 'musical',
 'adventure',
 'war',
 'drama',
 'music',
 'comedy',
 'fantasy',
 'family',
 'animation',
 'thriller',
 'sci-fi',
 'sport',
 'action',
 'history',
 'romance',
 'biography']
  
# datatype of menu text
genre_clicked = tk.StringVar()
  
# initial menu text
genre_clicked.set("western")


# Create Dropdown menu
drop = tk.OptionMenu( window , genre_clicked , *genres_option )
drop.grid(column=0, row=1)




# select the rating:
rating_label = tk.Label(text='Min Rating')
rating_label.grid(column=1, row=0)

# make a box to input the min rating
rating_entry = tk.Entry(width=3)
rating_entry.grid(column=1, row=1)




# select a year range:
year_label = tk.Label(text='Year Range')
year_label.grid(column=2, row=0)

min_year_label = tk.Label(text='Min')
min_year_label.grid(column=2, row=1)

min_year_option = [x for x in range(2006, 2017)] # a list from 2006 to 2016
min_year_c = tk.IntVar() # the type of the cell is integer
min_year_c.set(2006) # set an initial value
min_year_drop = tk.OptionMenu( window , min_year_c , *min_year_option ) # set the drop down menu
min_year_drop.grid(column=2, row=2)

# Max year:
max_year_label = tk.Label(text='Max')
max_year_label.grid(column=3, row=1)


max_year_option = [x for x in range(2006, 2017)] # a list from 2006 to 2016
max_year_c = tk.IntVar() # the type of the cell is integer
max_year_c.set(2016) # set an initial value
max_year_drop = tk.OptionMenu( window , max_year_c , *max_year_option ) # set the drop down menu
max_year_drop.grid(column=3, row=2)


# what to do when clicking on the button:
def get_movie():
    try:
        rating = float(rating_entry.get())
    except ValueError: # when the input value is not a number.
        rating = 0.0
    
    genre = genre_clicked.get()

    min_year = int(min_year_c.get())
    max_year = int(max_year_c.get())

    conn = sqlite3.connect('movies.db') # connect to the database
    cr = conn.cursor()
    # send the next query
    cr.execute(f'''SELECT * FROM data
    WHERE
    rating >= {rating}
    AND year BETWEEN {min_year} AND {max_year}
    AND genre LIKE "%{genre}%"''')
    movies = cr.fetchall() # fetch the results
    try: # an error will occur when the list of movies is empty
        movie = choice(movies)
        movie = list(movie)
        print_box = (f"""
Title:\n{movie[0]}
\nGenre:\n{movie[1]}
\nDirector:\n{movie[2]}
\nActors:\n{movie[3]}
\nYear:\n{movie[4]}
\nRuntime (Minutes):\n{movie[5]}
\nRating:\n{movie[6]}/10""")
    except IndexError:
        print_box = 'No movie was found!'
    cr.close()
    conn.close()
    # window.destroy()
    movie_label.config(text=print_box, font=('Arial', 12, 'bold'))
    
# just to add more space
blank_label = tk.Label(text = '\t', background='grey')
blank_label.grid(column=4, row=0)

# set the get a movie button and what it does when clicking on it
get_movie_button = tk.Button(text='Get a movie!', font=('Arial', 12, 'bold'), command=get_movie)
get_movie_button.grid(column=5, row=1)

# print the chosen movie on the screen
movie_label = tk.Label(text='Your Movie is: ...', background='yellow' , height=25, width=75)
movie_label.place(x=0, y=100)


window.mainloop() # keep the window open until the manual exit.