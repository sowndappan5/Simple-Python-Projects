from tkinter import *
from tkinter import messagebox

def AdventureStory(win):
    def display_story(tl: Toplevel, user_name, favorite_game, city_name, sports_hero, favorite_drink, snack_choice):
        story_text = f'''
        One sunny afternoon, I went out with my friend {user_name} to enjoy a {favorite_game} match in {city_name}.
        Unfortunately, the match was canceled, so we decided to watch the game instead and cheer for our idol, {sports_hero}.
        While watching, we had some {favorite_drink} to drink and enjoyed delicious {snack_choice}.
        It was a day to remember, and we can't wait to do it again!'''

        tl.geometry('500x550')
        Label(tl, text='Story:', wraplength=tl.winfo_width(), font=("Helvetica", 14, "bold"), fg="darkblue").place(x=160, y=310)
        Label(tl, text=story_text, wraplength=tl.winfo_width(), font=("Arial", 12), fg="black").place(x=10, y=330)

    screen = Toplevel(win, bg='lightyellow')
    screen.title("An Epic Adventure")
    screen.geometry('500x500')
    
    Label(screen, text='An Epic Adventure', font=("Arial", 18, "bold"), fg="purple").place(x=130, y=20)
    
    Label(screen, text='Enter your name:', font=("Arial", 12), fg="green").place(x=10, y=70)
    Label(screen, text='Enter your favorite game:', font=("Arial", 12), fg="green").place(x=10, y=110)
    Label(screen, text='Enter a city name:', font=("Arial", 12), fg="green").place(x=10, y=150)
    Label(screen, text='Enter your sports hero:', font=("Arial", 12), fg="green").place(x=10, y=190)
    Label(screen, text='Enter your favorite drink:', font=("Arial", 12), fg="green").place(x=10, y=230)
    Label(screen, text='Enter a snack you like:', font=("Arial", 12), fg="green").place(x=10, y=270)

    user_name = Entry(screen, width=20, font=("Arial", 12), bd=3, relief=SOLID)
    user_name.place(x=250, y=70)
    favorite_game = Entry(screen, width=20, font=("Arial", 12), bd=3, relief=SOLID)
    favorite_game.place(x=250, y=110)
    city_name = Entry(screen, width=20, font=("Arial", 12), bd=3, relief=SOLID)
    city_name.place(x=250, y=150)
    sports_hero = Entry(screen, width=20, font=("Arial", 12), bd=3, relief=SOLID)
    sports_hero.place(x=250, y=190)
    favorite_drink = Entry(screen, width=20, font=("Arial", 12), bd=3, relief=SOLID)
    favorite_drink.place(x=250, y=230)
    snack_choice = Entry(screen, width=20, font=("Arial", 12), bd=3, relief=SOLID)
    snack_choice.place(x=250, y=270)

    submit_button = Button(screen, text="Submit", bg="#4CAF50", fg="white", font=("Arial", 14, "bold"),
                           activebackground="#45a049", relief=FLAT, width=15,
                           command=lambda: display_story(screen, user_name.get(), favorite_game.get(), city_name.get(), sports_hero.get(), favorite_drink.get(), snack_choice.get()))
    submit_button.place(x=150, y=320)
    screen.mainloop()

def DreamJobStory(win):
    def display_story(tl: Toplevel, dream_job, career_field, mood, inner_feelings, action):
        story_text = f'''
        As a child, I dreamt of becoming a {dream_job}, but as time passed, I entered the world of {career_field}.
        There, I realized I was not truly {mood} about it. Eventually, I felt {inner_feelings}, which pushed me to pursue 
        my true passion. Even though I earn {action} less than before, I'm much happier now!'''

        tl.geometry('500x550')
        Label(tl, text='Story:', wraplength=tl.winfo_width(), font=("Helvetica", 14, "bold"), fg="darkblue").place(x=160, y=310)
        Label(tl, text=story_text, wraplength=tl.winfo_width(), font=("Arial", 12), fg="black").place(x=10, y=330)

    screen = Toplevel(win, bg='lightpink')
    screen.title("Dreams and Realities")
    screen.geometry('500x500')
    
    Label(screen, text='Dreams and Realities', font=("Arial", 18, "bold"), fg="brown").place(x=120, y=20)
    
    Label(screen, text='Enter your dream job:', font=("Arial", 12), fg="purple").place(x=10, y=70)
    Label(screen, text='Enter a career field:', font=("Arial", 12), fg="purple").place(x=10, y=110)
    Label(screen, text='Enter your mood:', font=("Arial", 12), fg="purple").place(x=10, y=150)
    Label(screen, text='Enter your inner feelings:', font=("Arial", 12), fg="purple").place(x=10, y=190)
    Label(screen, text='Enter the amount you earn:', font=("Arial", 12), fg="purple").place(x=10, y=230)

    dream_job = Entry(screen, width=20, font=("Arial", 12), bd=3, relief=SOLID)
    dream_job.place(x=250, y=70)
    career_field = Entry(screen, width=20, font=("Arial", 12), bd=3, relief=SOLID)
    career_field.place(x=250, y=110)
    mood = Entry(screen, width=20, font=("Arial", 12), bd=3, relief=SOLID)
    mood.place(x=250, y=150)
    inner_feelings = Entry(screen, width=20, font=("Arial", 12), bd=3, relief=SOLID)
    inner_feelings.place(x=250, y=190)
    action = Entry(screen, width=20, font=("Arial", 12), bd=3, relief=SOLID)
    action.place(x=250, y=230)

    submit_button = Button(screen, text="Submit", bg="#FF6347", fg="white", font=("Arial", 14, "bold"),
                           activebackground="#FF4500", relief=FLAT, width=15,
                           command=lambda: display_story(screen, dream_job.get(), career_field.get(), mood.get(), inner_feelings.get(), action.get()))
    submit_button.place(x=150, y=270)
    screen.mainloop()

# Main Screen
main_screen = Tk()
main_screen.title("Your Personal Mad Libs Generator")
main_screen.geometry('500x400')
main_screen.config(bg="lightblue")
Label(main_screen, text='Your Personal Mad Libs Generator', font=("Arial", 18, "bold"), fg="darkblue").place(x=70, y=30)

adventure_button = Button(main_screen, text='Epic Adventure', font=("Arial", 14), bg="#32CD32", fg="white", relief=RAISED, activebackground="#228B22", width=20, height=2,
                           command=lambda: AdventureStory(main_screen))
adventure_button.place(x=150, y=90)

dream_job_button = Button(main_screen, text='Dream Job', font=("Arial", 14), bg="#FF6347", fg="white", relief=RAISED, activebackground="#FF4500", width=20, height=2,
                           command=lambda: DreamJobStory(main_screen))
dream_job_button.place(x=150, y=160)

main_screen.mainloop()
