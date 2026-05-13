
import json
import random
import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk

# ------------------------- DATA HANDLERS -------------------------
def load_json(file_name, default_value):
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return default_value

def save_json(file_name, data):
    with open(file_name, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

# ------------------------- GUI APPLICATION -------------------------
class BillionaireQuiz:
    def __init__(self, root):
        self.root = root
        self.root.title("🏆 Kim Millioner Bo'lmoqchi? - BILLIONER EDITION 🏆")
        self.root.geometry("900x650")
        self.root.configure(bg="#1e272e")

        # Load data
        self.questions = load_json("tests.json", [])
        if not self.questions:
            messagebox.showerror("Xatolik", "tests.json fayli topilmadi yoki bo'sh!")
            self.root.destroy()
            return

        self.users = load_json("Users_Name.json", [])
        self.current_user = None
        self.score = 0
        self.current_q_index = 0
        self.shuffled_questions = []
        self.help_used = False
        self.current_answers = []
        self.answer_labels = ['A', 'B', 'C', 'D']

        # Colors & styles
        self.bg = "#1e272e"
        self.fg_light = "#d2dae2"
        self.accent = "#f5cd79"
        self.correct_color = "#2ecc71"
        self.wrong_color = "#e74c3c"
        self.btn_bg = "#485460"
        self.btn_hover = "#747d8c"

        # Setup GUI
        self.setup_login_frame()

    def setup_login_frame(self):
        self.clear_frame()
        self.login_frame = tk.Frame(self.root, bg=self.bg)
        self.login_frame.pack(fill="both", expand=True)

        # Header
        title = tk.Label(self.login_frame, text="🏆 KIM MILLIONER BO'LMOQCHI? 🏆",
                         font=("Helvetica", 28, "bold"), fg=self.accent, bg=self.bg)
        title.pack(pady=50)

        sub = tk.Label(self.login_frame, text="Ismingizni kiriting va o‘yinga tayyorlaning!",
                       font=("Helvetica", 14), fg=self.fg_light, bg=self.bg)
        sub.pack(pady=10)

        self.name_entry = tk.Entry(self.login_frame, font=("Helvetica", 16), width=25,
                                   justify="center", bg="#2f3e46", fg="white",
                                   insertbackground="white")
        self.name_entry.pack(pady=20)
        self.name_entry.focus()

        btn_start = tk.Button(self.login_frame, text="🎮 O‘YINNI BOSHLASH 🎮",
                              font=("Helvetica", 14, "bold"), bg=self.accent, fg="black",
                              command=self.start_game, padx=20, pady=10)
        btn_start.pack(pady=20)

        btn_stats = tk.Button(self.login_frame, text="📊 STATISTIKA 📊",
                              font=("Helvetica", 12), bg=self.btn_bg, fg="white",
                              command=self.show_statistics, padx=20, pady=8)
        btn_stats.pack(pady=5)

        btn_quit = tk.Button(self.login_frame, text="🚪 CHIQISH", font=("Helvetica", 12),
                             bg="#c0392b", fg="white", command=self.root.destroy, padx=20, pady=8)
        btn_quit.pack(pady=5)

    def start_game(self):
        name = self.name_entry.get().strip()
        if not name:
            name = "Mehmon"
        self.current_user = name

        # Prepare game
        self.score = 0
        self.current_q_index = 0
        self.help_used = False
        self.shuffled_questions = random.sample(self.questions, len(self.questions))
        self.setup_game_frame()

    def setup_game_frame(self):
        self.clear_frame()
        self.game_frame = tk.Frame(self.root, bg=self.bg)
        self.game_frame.pack(fill="both", expand=True)

        # Top bar
        top_bar = tk.Frame(self.game_frame, bg="#2c3e50", height=60)
        top_bar.pack(fill="x", pady=(0,10))
        tk.Label(top_bar, text=f"👤 {self.current_user}", font=("Helvetica", 12), bg="#2c3e50", fg="white").pack(side="left", padx=15)
        self.score_label = tk.Label(top_bar, text=f"⭐ Ball: {self.score}", font=("Helvetica", 14, "bold"), bg="#2c3e50", fg=self.accent)
        self.score_label.pack(side="right", padx=15)
        self.q_progress = tk.Label(top_bar, text="", font=("Helvetica", 10), bg="#2c3e50", fg="white")
        self.q_progress.pack(side="right", padx=10)

        # Question frame
        self.q_frame = tk.Frame(self.game_frame, bg="#3b4a5a", bd=2, relief="ridge")
        self.q_frame.pack(fill="both", expand=True, padx=30, pady=20)

        self.question_label = tk.Label(self.q_frame, text="", font=("Helvetica", 16), wraplength=800,
                                       bg="#3b4a5a", fg=self.fg_light, justify="center")
        self.question_label.pack(pady=40, padx=20)

        # Buttons frame
        self.btns_frame = tk.Frame(self.q_frame, bg="#3b4a5a")
        self.btns_frame.pack(fill="both", expand=True, padx=30, pady=20)

        self.option_buttons = []
        for i in range(4):
            btn = tk.Button(self.btns_frame, text="", font=("Helvetica", 12), bg=self.btn_bg, fg="white",
                            anchor="w", padx=10, command=lambda idx=i: self.check_answer(idx))
            btn.pack(fill="x", pady=6, ipady=6)
            self.option_buttons.append(btn)

        # Help button
        self.help_btn = tk.Button(self.game_frame, text="💡 50/50 YORDAM", font=("Helvetica", 12, "bold"),
                                  bg="#f39c12", fg="black", command=self.use_help)
        self.help_btn.pack(pady=10)

        # Load first question
        self.load_question()

    def load_question(self):
        if self.current_q_index >= len(self.shuffled_questions):
            self.end_game()
            return

        q_data = self.shuffled_questions[self.current_q_index]
        self.current_answers = q_data["answers"].copy()
        self.answer_labels = ['A', 'B', 'C', 'D']
        self.question_label.config(text=f"{self.current_q_index+1}. {q_data['question']}")
        self.q_progress.config(text=f"Savol {self.current_q_index+1}/{len(self.shuffled_questions)}")
        self.update_buttons()

    def update_buttons(self):
        for i, btn in enumerate(self.option_buttons):
            if i < len(self.current_answers):
                btn.config(text=f"  {self.answer_labels[i]}) {self.current_answers[i]['key']}",
                           state="normal", bg=self.btn_bg)
            else:
                btn.config(text="", state="disabled", bg=self.btn_bg)
        # Re-enable help if not used yet
        if not self.help_used:
            self.help_btn.config(state="normal")
        else:
            self.help_btn.config(state="disabled")

    def check_answer(self, idx):
        if idx >= len(self.current_answers):
            return
        selected = self.current_answers[idx]
        # Find correct key among original answers (full set)
        original_q = self.shuffled_questions[self.current_q_index]
        correct_key = next(a["key"] for a in original_q["answers"] if a["isTrue"])

        if selected["isTrue"]:
            self.score += 1
            self.score_label.config(text=f"⭐ Ball: {self.score}")
            # Flash green
            self.option_buttons[idx].config(bg=self.correct_color)
            self.root.after(500, self.next_question)
        else:
            for btn in self.option_buttons:
                btn.config(state="disabled")
            self.option_buttons[idx].config(bg=self.wrong_color)
            messagebox.showerror("Noto'g'ri javob!", f"❌ To'g'ri javob:\n{correct_key}")
            self.end_game(save_score=True)

    def next_question(self):
        self.current_q_index += 1
        self.help_used = False
        self.load_question()

    def use_help(self):
        if self.help_used:
            return
        correct = next(a for a in self.current_answers if a["isTrue"])
        wrongs = [a for a in self.current_answers if not a["isTrue"]]
        if len(wrongs) <= 1:
            messagebox.showinfo("Yordam", "50/50 yordamini ishlatib bo‘lmaydi (juda kam variant)!")
            return
        keep_wrong = random.choice(wrongs)
        self.current_answers = [correct, keep_wrong]
        self.answer_labels = ['A', 'B']
        self.help_used = True
        self.update_buttons()
        self.help_btn.config(state="disabled")
        messagebox.showinfo("50/50 Yordam", "Ikkita variant qoldi. Ulardan birini tanlang!")

    def end_game(self, save_score=True):
        if save_score:
            self.save_result()
        total = len(self.shuffled_questions)
        if self.score == total:
            msg = f"🎉 TABRIKLAYMIZ! Siz barcha {total} ta savolga to‘g‘ri javob berdingiz! 🎉\nBall: {self.score}"
        else:
            msg = f"🏁 O‘yin tugadi. Sizning natijangiz: {self.score}/{total} 🏁"
        messagebox.showinfo("O‘yin yakuni", msg)
        self.setup_login_frame()

    def save_result(self):
        if not self.current_user:
            return
        found = False
        for u in self.users:
            if u["name"].lower() == self.current_user.lower():
                u["total_games"] += 1
                if self.score > u["score"]:
                    u["score"] = self.score
                    messagebox.showinfo("Yangi rekord!", f"Eng yaxshi natijangiz yangilandi: {self.score}")
                found = True
                break
        if not found:
            self.users.append({"name": self.current_user, "score": self.score, "total_games": 1})
        save_json("Users_Name.json", self.users)

    def show_statistics(self):
        users = load_json("Users_Name.json", [])
        if not users:
            messagebox.showinfo("Statistika", "Hali hech qanday natija yo‘q.")
            return
        users.sort(key=lambda x: x["score"], reverse=True)
        stats_win = tk.Toplevel(self.root)
        stats_win.title("📊 Statistika")
        stats_win.geometry("500x400")
        stats_win.configure(bg="#1e272e")

        tk.Label(stats_win, text="🏆 ENG YAXSHI NATIJALAR 🏆", font=("Helvetica", 16, "bold"),
                 fg=self.accent, bg=self.bg).pack(pady=10)

        tree = ttk.Treeview(stats_win, columns=("rank", "name", "score", "games"), show="headings", height=15)
        tree.heading("rank", text="#")
        tree.heading("name", text="Ism")
        tree.heading("score", text="Eng yaxshi ball")
        tree.heading("games", text="O‘yinlar soni")
        tree.column("rank", width=40, anchor="center")
        tree.column("name", width=150)
        tree.column("score", width=120, anchor="center")
        tree.column("games", width=100, anchor="center")

        for i, u in enumerate(users, 1):
            medal = "🥇" if i==1 else "🥈" if i==2 else "🥉" if i==3 else str(i)
            tree.insert("", "end", values=(medal, u["name"], u["score"], u["total_games"]))

        tree.pack(pady=20, padx=20, fill="both", expand=True)
        tk.Button(stats_win, text="Yopish", command=stats_win.destroy, bg=self.accent, font=("Helvetica", 10)).pack(pady=10)

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# ------------------------- MAIN -------------------------
if __name__ == "__main__":
    root = tk.Tk()
    app = BillionaireQuiz(root)
    root.mainloop()