import tkinter as tk


class MyPomodoroApp(tk.Tk):  # define a class that inherits from tk.Tk()

    def __init__(self):
        super().__init__()  # Initialise tk.Tk() instance ... similar to root = tk.Tk() previously

        # Set defaults for timing ...
        self.timer_running = False
        self.default_minutes = 5
        self.seconds = 5 * 60

        self.title("Pomodoro App v1.0")
        self.geometry("600x600")

        # FRAME 1 - User inputs minutes pomodoro needs to last #
        frame1 = tk.Frame(self)
        frame1.grid(row=0, column=0, padx=20, pady=20)

        # Add some content to the first frame (optional)
        label1 = tk.Label(frame1, text="Input desired Pomodoro time: ", font=("Arial", 20))
        label1.pack(side=tk.LEFT)

        self.user_time_var = tk.IntVar(value=self.default_minutes)
        user_time = tk.Entry(frame1, textvariable=self.user_time_var, font=("Arial", 20))
        user_time.pack(side=tk.LEFT, padx=10)

        set_time_button = tk.Button(frame1, text="Set Time", font=("Arial", 20), command=lambda: self.set_time())
        set_time_button.pack(side=tk.LEFT, padx=10)

        # FRAME 2 - Countdown timer display #
        frame2 = tk.Frame(self)
        frame2.grid(row=1, column=0, padx=20, pady=20)
        self.initialise_timer(frame2)

        # FRAME 3 - Start/Pause and Reset Buttons #
        frame3 = tk.Frame(self)
        frame3.grid(row=2, column=0, padx=20, pady=20)

        start_pause_button = tk.Button(
            frame3, text="Start/Pause Timer", font=("Arial", 20), command=lambda: self.start_pause_timer())
        start_pause_button.pack(side=tk.LEFT, padx=10)

        reset_button = tk.Button(
            frame3, text="Reset Timer", font=("Arial", 20), command=lambda: self.reset_timer())
        reset_button.pack(side=tk.LEFT, padx=10)

        # Will this just bang it underneath by default
        quit_button = tk.Button(self, text="Quit", font=("Arial", 20), command=lambda: self.destroy())
        quit_button.grid(row=3, column=0, padx=20, pady=20)

        # Update timer display
        self.update_timer()

    def set_time(self):
        try:
            print(self.user_time_var.get())
            if self.user_time_var.get() > 0:
                self.default_minutes = self.user_time_var.get()
                self.seconds = self.default_minutes * 60
                self.timer_label.config(text=f"{self.default_minutes:02}:00")

        except ValueError:
            print("Invalid input: Integer minute values only!")

    def initialise_timer(self, frame2):
        self.timer_running = False
        self.timer_label = tk.Label(frame2, text=f"{self.default_minutes:02}:00", font=("Arial", 20))
        self.timer_label.pack(pady=30)

    def start_pause_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.update_timer()

        elif self.timer_running:
            self.timer_running = False

    def update_timer(self):

        if self.timer_running:
            self.seconds -= 1

            if self.seconds <= 0:
                print(f"END OF POMODORO, TAKE A BREAK SON!")
                self.timer_running = False
                self.timer_label.config(text=f"{self.default_minutes:02}:00")
                return

            minutes = self.seconds // 60
            seconds = self.seconds % 60
            time_str = f"{minutes:02}:{seconds:02}"

            self.timer_label.config(text=time_str)
            self.after(1000, self.update_timer)

    def reset_timer(self):
        self.timer_running = False  # Stop timer running
        self.seconds = self.default_minutes * 60  # Reset the seconds values to the default / user inputted
        self.timer_label.config(text=f"{self.default_minutes:02}:00")  # Restart the timer_label value


if __name__ == "__main__":
    root = MyPomodoroApp()
    root.mainloop()
