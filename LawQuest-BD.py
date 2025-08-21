# ---------------------------
# Bangladesh Law Helper - Advanced GUI Game
# ---------------------------

import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import random

# ---------------------------
# Classes
# ---------------------------
class Law:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class LawCategory:
    def __init__(self, category_name):
        self.category_name = category_name
        self.laws = []

    def add_law(self, law):
        self.laws.append(law)

class Student:
    leaderboard = []  # Class variable to store all students

    def __init__(self, name):
        self.name = name
        self.points = 0
        self.badges = []
        Student.leaderboard.append(self)

    def add_points(self, pts):
        self.points += pts
        self.check_badges()

    def check_badges(self):
        unlocked = []
        if self.points >= 10 and "Bronze Scholar" not in self.badges:
            self.badges.append("Bronze Scholar")
            unlocked.append("Bronze Scholar")
        if self.points >= 25 and "Silver Scholar" not in self.badges:
            self.badges.append("Silver Scholar")
            unlocked.append("Silver Scholar")
        if self.points >= 50 and "Gold Scholar" not in self.badges:
            self.badges.append("Gold Scholar")
            unlocked.append("Gold Scholar")
        if unlocked:
            messagebox.showinfo("Badge Unlocked!", f"Congratulations! You unlocked: {', '.join(unlocked)}")

    def get_status(self):
        return f"Name: {self.name}\nPoints: {self.points}\nBadges: {', '.join(self.badges) if self.badges else 'None'}"

    @classmethod
    def get_leaderboard(cls):
        sorted_list = sorted(cls.leaderboard, key=lambda x: x.points, reverse=True)
        return "\n".join([f"{idx+1}. {s.name} - {s.points} pts" for idx, s in enumerate(sorted_list)])

class LawHelperGUI:
    def __init__(self, root, student, categories):
        self.root = root
        self.root.title("Bangladesh Law Helper - Advanced GUI Game")
        self.student = student
        self.categories = categories
        self.quiz_questions = self.generate_quiz()
        self.current_question = 0
        self.score = 0
        self.create_main_menu()

    # --------------------------- Main Menu ---------------------------
    def create_main_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text=f"🇧🇩 Bangladesh Law Helper 🇧🇩", font=("Arial", 20, "bold"), fg="blue").pack(pady=10)
        tk.Label(self.root, text=f"Welcome, {self.student.name}", font=("Arial", 14)).pack(pady=5)

        btn_frame = tk.Frame(self.root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="View Law Categories", width=30, command=self.view_categories).grid(row=0, column=0, pady=5)
        tk.Button(btn_frame, text="Search Law", width=30, command=self.search_law).grid(row=1, column=0, pady=5)
        tk.Button(btn_frame, text="Take a Quiz", width=30, command=self.start_quiz).grid(row=2, column=0, pady=5)
        tk.Button(btn_frame, text="Show Status & Badges", width=30, command=self.show_status).grid(row=3, column=0, pady=5)
        tk.Button(btn_frame, text="View Leaderboard", width=30, command=self.show_leaderboard).grid(row=4, column=0, pady=5)
        tk.Button(btn_frame, text="Exit", width=30, command=self.root.quit).grid(row=5, column=0, pady=5)

    # --------------------------- Categories ---------------------------
    def view_categories(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Law Categories", font=("Arial", 16, "bold"), fg="green").pack(pady=10)
        for cat in self.categories:
            tk.Button(self.root, text=cat.category_name, width=40, command=lambda c=cat: self.view_laws(c)).pack(pady=3)

        tk.Button(self.root, text="Back", command=self.create_main_menu).pack(pady=10)

    def view_laws(self, category):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text=f"{category.category_name} Laws", font=("Arial", 16, "bold"), fg="purple").pack(pady=10)

        for law in category.laws:
            tk.Button(self.root, text=law.name, width=50, command=lambda l=law: self.show_law(l)).pack(pady=2)

        tk.Button(self.root, text="Back", command=self.view_categories).pack(pady=10)

    def show_law(self, law):
        messagebox.showinfo(law.name, law.description)
        self.student.add_points(2)

    # --------------------------- Search ---------------------------
    def search_law(self):
        keyword = simpledialog.askstring("Search Law", "Enter law name or keyword:")
        if not keyword:
            return
        found = False
        for cat in self.categories:
            for law in cat.laws:
                if keyword.lower() in law.name.lower() or keyword.lower() in law.description.lower():
                    messagebox.showinfo(law.name, law.description)
                    self.student.add_points(2)
                    found = True
        if not found:
            messagebox.showwarning("Not Found", "No law found with that keyword.")

    # --------------------------- Status ---------------------------
    def show_status(self):
        messagebox.showinfo("Student Status", self.student.get_status())

    # --------------------------- Leaderboard ---------------------------
    def show_leaderboard(self):
        leaderboard_text = Student.get_leaderboard()
        messagebox.showinfo("Leaderboard", leaderboard_text)

    # --------------------------- Quiz ---------------------------
    def generate_quiz(self):
        questions = [
            {"question": "Which law governs traffic rules?", "options": ["IT Act", "Traffic Act", "Civil Code", "Penal Code"], "answer": "Traffic Act"},
            {"question": "Which law deals with cybercrime?", "options": ["IT Act", "Traffic Act", "Penal Code", "Civil Law"], "answer": "IT Act"},
            {"question": "Which law covers contracts?", "options": ["Property Law", "Contract Act", "Traffic Act", "IT Act"], "answer": "Contract Act"},
            {"question": "Which law defines crimes and punishments?", "options": ["Penal Code", "Contract Act", "Property Law", "Traffic Act"], "answer": "Penal Code"},
            {"question": "Which law protects digital data?", "options": ["IT Act", "Contract Act", "Penal Code", "Traffic Act"], "answer": "IT Act"},
            {"question": "Which law regulates civil disputes?", "options": ["Civil Code", "Penal Code", "Traffic Act", "IT Act"], "answer": "Civil Code"},
            {"question": "Which law deals with property inheritance?", "options": ["Property Law", "Civil Code", "Traffic Act", "IT Act"], "answer": "Property Law"},
            {"question": "Which law punishes fraud?", "options": ["Penal Code", "IT Act", "Contract Act", "Traffic Act"], "answer": "Penal Code"},
            {"question": "Which law regulates online contracts?", "options": ["IT Act", "Contract Act", "Penal Code", "Traffic Act"], "answer": "IT Act"},
            {"question": "Which law ensures safe driving?", "options": ["Traffic Act", "IT Act", "Penal Code", "Civil Law"], "answer": "Traffic Act"},
            # Add more questions to reach 20+ if desired
        ]
        random.shuffle(questions)
        return questions

    def start_quiz(self):
        self.current_question = 0
        self.score = 0
        self.show_question()

    def show_question(self):
        if self.current_question >= len(self.quiz_questions):
            messagebox.showinfo("Quiz Completed", f"You scored {self.score}/{len(self.quiz_questions)}")
            self.create_main_menu()
            return

        q = self.quiz_questions[self.current_question]
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text=f"Question {self.current_question +1}: {q['question']}", font=("Arial", 14, "bold")).pack(pady=10)

        for opt in q["options"]:
            tk.Button(self.root, text=opt, width=40, command=lambda o=opt: self.check_answer(o)).pack(pady=5)

    def check_answer(self, selected):
        q = self.quiz_questions[self.current_question]
        if selected == q["answer"]:
            messagebox.showinfo("Correct!", "Correct Answer!")
            self.score +=1
            self.student.add_points(3)
        else:
            messagebox.showerror("Wrong!", f"Wrong! Correct answer: {q['answer']}")
        self.current_question +=1
        self.show_question()


# ---------------------------
# Sample Law Data (50+)
# ---------------------------
categories = []

civil_law = LawCategory("Civil Law")
for law in ["Contract Act", "Property Law", "Civil Code", "Inheritance Law", "Family Law",
            "Marriage Act", "Divorce Act", "Land Disputes Law", "Tenant Rights Law", "Consumer Rights Law"]:
    civil_law.add_law(Law(law, f"Description of {law}."))

criminal_law = LawCategory("Criminal Law")
for law in ["Penal Code", "Traffic Act", "Anti-Corruption Law", "Cybercrime Law", "Murder and Assault Law",
            "Fraud Act", "Drug Control Law", "Terrorism Act", "Domestic Violence Law", "Juvenile Justice Law"]:
    criminal_law.add_law(Law(law, f"Description of {law}."))

it_law = LawCategory("IT & Cyber Law")
for law in ["IT Act", "Digital Security Act", "E-Commerce Law", "Online Privacy Law", "Cyber Fraud Act",
            "Software Licensing Law", "Digital Contracts Law", "Social Media Law", "Data Protection Law", "Computer Misuse Act"]:
    it_law.add_law(Law(law, f"Description of {law}."))

categories.extend([civil_law, criminal_law, it_law])

# ---------------------------
# Run GUI
# ---------------------------
root = tk.Tk()
name = simpledialog.askstring("Enter Name", "Enter your name to start the game:")
student = Student(name if name else "Student")
app = LawHelperGUI(root, student, categories)
root.mainloop()
