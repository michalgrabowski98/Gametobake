import tkinter as tk
from playsound import playsound
from PIL import Image, ImageTk


class MyApp(tk.Frame):
    def __init__(self, root):
        super().__init__(
            root, 
            bg='White'

        )

        self.main_frame = self
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(0, weight=1)

        self.create_widgets()

    def create_widgets(self):



        self.label_gif1 = tk.Label(
            self.main_frame,
            bg='White',
            border=0,
            highlightthickness=0
        )

        self.label_gif1.grid(column=0, row=0)
        
        #lokalizacja pliku gif
        self.gif1_frames = self._get_frames('piwo.gif')


        root.after(100, self._play_gif, self.label_gif1, self.gif1_frames)

        #muziczka jak się definuje   
        play = lambda: playsound('ASMRPIWO.mp3',block=False)

        #guzik
        self.button2= tk.Button(
            self.main_frame,
            text = "Exit",
            width= 10,
            height=2,
            command = root.destroy
        )
        self.button = tk.Button(
            self.main_frame,
            text='Naciśnij guzior aby wypić piwko 🍺🍺🍺🍺',
            width=40,
            height=2,
            command= play
        )

        self.button.grid(column=0, row=1)
        self.button2.grid(column=0, row=3)

    def _get_frames(self, img):

     with Image.open(img) as gif:
            index = 0
            frames = []
            while True:
                try:
                  gif.seek(index)
                  frame = ImageTk.PhotoImage(gif)
                  frames.append(frame)
                except EOFError:
                    break

                index += 1

            return frames
     
    def _play_gif(self, label, frames):
         
        total_delay = 5
        delay_frames = 10

        for frame in frames:
            root.after(total_delay, self._next_frame, frame, label, frames)
            total_delay += delay_frames

        root.after(total_delay, self._next_frame, frame, label, frames, True)

    def _next_frame(self, frame, label, frames, restart=False):

        if restart:
            root.after(1, self._play_gif, label, frames)
            return

        label.config(
            image=frame
        )
        #tworzenie okna
root = tk.Tk()

#tytuł okna
root.title('GIF')

#rozmiar okna
root.geometry('900x900')
root.resizable(width=False, height=False)

my_app_instance = MyApp(root)

root.mainloop()