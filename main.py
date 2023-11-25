import tkinter as tk
from datetime import datetime, timedelta
from PIL import Image, ImageTk


class CountdownTimerApp:
    def __init__(self, target_date, window_position, background_image_path):
        self.root = tk.Tk()
        self.root.title("Memento Mori")
        self.root.attributes("-alpha", 0.5)  # Set the window's opacity to 50%

        self.canvas = tk.Canvas(self.root, width=400, height=200)
        self.canvas.pack()

        self.load_background_image(background_image_path)

        self.root.geometry(window_position)

        self.target_date = datetime.strptime(target_date, "%Y-%m-%d %H:%M:%S")
        self.remaining_time = self.calculate_remaining_time()

        # Use the canvas to display the timer label
        self.label = self.canvas.create_text(150, 50, text="", font=("Helvetica", 22), anchor="center")

        self.update_timer()

    def calculate_remaining_time(self):
        current_time = datetime.now()
        remaining_time = self.target_date - current_time
        return max(int(remaining_time.total_seconds()), 0)

    def load_background_image(self, image_path):
        original_image = Image.open(image_path)
        self.background_image = ImageTk.PhotoImage(original_image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.background_image, tags="background")

    def on_resize(self, event):
        # Resize the image when the window is resized
        self.load_background_image(background_image_path)

    def update_timer(self):
        if self.remaining_time > 0:
            self.canvas.itemconfig(self.label, text=self.format_time(self.remaining_time))
            self.remaining_time -= 1
            self.root.after(1000, self.update_timer)
        else:
            self.canvas.itemconfig(self.label, text="Countdown timer reached zero!")
            self.root.after(2000, self.root.destroy)

    def format_time(self, seconds):
        days, remainder = divmod(seconds, 3600*24)
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)
        return "{:02} {:02}:{:02}:{:02}".format(int(days),int(hours), int(minutes), int(seconds))

    def run(self):

        self.root.mainloop()



if __name__ == "__main__":
    target_date_str = "2077-11-23 12:00:00"
    window_position = "300x100+1600+50"
    background_image_path = "image.jpg"  # Replace with the path to your image

    app = CountdownTimerApp(target_date_str, window_position, background_image_path)
    app.run()
