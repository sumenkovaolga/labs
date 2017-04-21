# from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import font
from PIL import ImageTk, Image
import random
import webbrowser
import traceback
from io import BytesIO
import time

import kinopoisk_parser as kp

actors = {}
films_with_actor = {}
films_info = {}


# TODO: progressbar
# http://stackoverflow.com/questions/7310511/how-to-create-downloading-progress-bar-in-ttk
# https://gist.github.com/livibetter/6850443


class MainApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Kinopoisk help")

        main_container = tk.Frame(self, borderwidth=1, relief="sunken",
                             width=500, height=500)
        main_container.grid_propagate(False)
        main_container.pack(fill='both', expand=True)

        control_container = tk.Frame(main_container, borderwidth=1, relief="sunken", pady=10)
        # control_container.grid_propagate(False)
        control_container.pack(fill=tk.X, side=tk.TOP)

        # actor name
        tk.Label(control_container, text='Input actor name').pack(side=tk.LEFT)
        self.actorNameEntry = tk.Entry(control_container)
        self.actorNameEntry.pack(side=tk.LEFT)

        # get film
        getFilmBtn = tk.Button(control_container, text='Get random film')
        getFilmBtn.bind("<Button-1>", self.get_film_Click)
        getFilmBtn.pack(side=tk.LEFT)

        # self.progress = ttk.Progressbar(control_container, orient="horizontal", mode="determinate")
        # self.progress.pack(side=tk.BOTTOM, anchor=tk.W, fill=tk.X)  # TODO: move to bottom

        # film info
        self.filminfo_container = tk.Frame(main_container, borderwidth=1, relief="sunken")
        self.filminfo_container.grid_propagate(False)
        # filminfo_container.pack(fill="both", expand=True)
        self.filminfo_container.pack(fill=tk.X, side=tk.TOP)

        self.filmposter = tk.Label(self.filminfo_container)
        self.filmposter.pack(side=tk.LEFT, expand=True)

        self.filmnameLabel = tk.Message(self.filminfo_container, font='Arial 10', aspect=500)
        self.filmnameLabel.pack(side=tk.TOP, fill=tk.X)

        self.filmdescriptionLabel = tk.Message(self.filminfo_container, font='Arial 10', aspect=500)
        self.filmdescriptionLabel.pack(side=tk.TOP, fill=tk.X)

        self.gotofilmButton = None

    def init_gotofilmButton(self):
        self.gotofilmButton = tk.Button(self.filminfo_container, text='Go to film')
        self.gotofilmButton.bind("<Button-1>", self.goto_film_Click)
        self.gotofilmButton.href = ''
        self.gotofilmButton.pack(side=tk.BOTTOM, fill=tk.X)

    def goto_film_Click(self, ev):
        if self.gotofilmButton.href != '':
            webbrowser.open_new(self.gotofilmButton.href)

    def get_film_Click(self, ev):
        while True:
            try:
                actor_name = self.actorNameEntry.get()
                if not actor_name:
                    return

                if actor_name not in actors:
                    actors[actor_name] = kp.get_actor_id_by_name(actor_name)
                actor_id = actors[actor_name]

                if actor_id not in films_with_actor:
                    films_with_actor[actor_id] = kp.get_film_ids_list_by_actor_id(actor_id)
                film_ids_list = films_with_actor[actor_id]

                film_id = random.choice(film_ids_list)
                if film_id not in films_info:
                    films_info[film_id] = kp.get_film_info_by_id(random.choice(film_ids_list))
                film_info = films_info[film_id]

                break
            except Exception as ex:
                print(ex)
                # print(traceback.format_exc(ex))  # TODO: fix strange exception in traceback
                time.sleep(1)

        if not self.gotofilmButton:
            self.init_gotofilmButton()
        self.gotofilmButton.href = film_info['film_href']
        self.filmnameLabel.configure(text=film_info['film_name'])
        self.filmdescriptionLabel.configure(text=film_info['film_descr'])

        try:
            img_src = BytesIO(kp.download_image(film_info['film_poster']))
        except Exception as ex:
            print(traceback.format_exc(ex))
            img_src = None

        if img_src:
            posterdata = Image.open(img_src)
            posterdata.thumbnail((250, 250), Image.ANTIALIAS)
            posterimage = ImageTk.PhotoImage(posterdata)
        else:
            posterimage = None

        self.filmposter.configure(image=posterimage)
        self.filmposter.image = posterimage


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()