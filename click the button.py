import tkinter as tk
import random

class ClickGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Click the button")

        self.difficulty = None
        self.time_left = 2
        self.running = False
        self.score = 0

        self.create_title_screen()

    def create_title_screen(self):
        self.clear_screen()

        title_label = tk.Label(self.root, text="Select Difficulty", font=("Arial", 24))
        title_label.pack(pady=20)

        easy_button = tk.Button(self.root, text="Easy (3 seconds)", command=lambda: self.start_game(3))
        easy_button.pack(pady=5)

        normal_button = tk.Button(self.root, text="Normal (2 seconds)", command=lambda: self.start_game(2))
        normal_button.pack(pady=5)

        hard_button = tk.Button(self.root, text="good luck (1 second)", command=lambda: self.start_game(1))
        hard_button.pack(pady=5)

    def start_game(self, difficulty):
        self.difficulty = difficulty
        self.time_left = difficulty
        self.running = True
        self.score = 0

        self.clear_screen()
        
        self.timer_label = tk.Label(self.root, text=f"Time left: {self.time_left}", font=("Arial", 16))
        self.timer_label.pack()

        self.score_label = tk.Label(self.root, text=f"Score: {self.score}", font=("Arial", 16))
        self.score_label.pack()

        self.restart_button = tk.Button(self.root, text="new game", command=self.restart_game)
        self.restart_button.pack()

        self.board_frame = tk.Frame(self.root, bg="lightgray", width=400, height=400)
        self.board_frame.pack(expand=True, fill=tk.BOTH)

        self.click_button = tk.Button(self.board_frame, text="Click", command=self.button_clicked)
        self.click_button.place(x=150, y=150)

        self.back_button = tk.Button(self.root, text="menu", command=self.create_title_screen)
        self.back_button.pack(anchor="ne", padx=10, pady=10)

        self.root.bind("<Configure>", self.resize_board)

        self.update_timer()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def button_clicked(self):
        if self.running:
            self.score += 10
            self.score_label.config(text=f"Score: {self.score}")
            self.time_left = self.difficulty  
            self.timer_label.config(text=f"Time left: {self.time_left}")
            self.move_button()

    def move_button(self):
        self.board_frame.update_idletasks()  
        board_width = self.board_frame.winfo_width()
        board_height = self.board_frame.winfo_height()
        x = random.randint(0, max(0, board_width - 100))
        y = random.randint(0, max(0, board_height - 100))
        self.click_button.place(x=x, y=y)

    def update_timer(self):
        if self.running:
            self.time_left -= 0.1
            if self.time_left <= 0:
                self.running = False
                self.timer_label.config(text=f"Time's up Game over Your score: {self.score}")
                self.click_button.config(state=tk.DISABLED)
            else:
                self.timer_label.config(text=f"Time left: {self.time_left:.1f}")
                self.root.after(100, self.update_timer)

    def restart_game(self):
        self.time_left = self.difficulty
        self.score = 0
        self.running = True
        self.timer_label.config(text=f"Time left: {self.time_left}")
        self.score_label.config(text=f"Score: {self.score}")
        self.click_button.config(state=tk.NORMAL)
        self.move_button()
        self.update_timer()

    def resize_board(self, event):
        self.board_frame.config(width=self.root.winfo_width(), height=self.root.winfo_height() - self.timer_label.winfo_height() - self.restart_button.winfo_height())
        self.board_frame.update_idletasks()  

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x400")
    game = ClickGame(root)
    root.mainloop()
