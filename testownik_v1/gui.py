# gui.py
import customtkinter as ctk
from tkinter import filedialog, messagebox, StringVar
from functions import save_each_qna_separately, format_question, reset_counter

questions_and_answers = []
question_count = 0

def add_qna(question_entry, answers_entry, label):
    global question_count
    question = question_entry.get("1.0", "end-1c")
    answers = answers_entry.get("1.0", "end-1c").strip().split("\n")

    if not question.strip() or not answers:
        messagebox.showwarning("Input Error", "Both Question and Answer fields must be filled out.")
        return

    question = format_question(question)
    questions_and_answers.append((question, answers))
    question_count += 1
    label.configure(text=f"Questions Added: {question_count}")

    messagebox.showinfo("Saved", "Question added. You can add another one or save all.")

    question_entry.delete("1.0", "end")
    answers_entry.delete("1.0", "end")

def save_all_qna(label):
    if not questions_and_answers:
        messagebox.showwarning("No Data", "No questions to save. Please add some questions first.")
        return

    directory = filedialog.askdirectory()

    if directory:
        save_each_qna_separately(directory, questions_and_answers)
        messagebox.showinfo("Success", f"All questions saved in directory: {directory}")
        questions_and_answers.clear()
        reset_counter(label)

def create_gui():
    ctk.set_appearance_mode("System")  # Initial theme mode
    ctk.set_default_color_theme("blue")  # Default color theme

    root = ctk.CTk()
    root.title("Testownik – Wprowadzanie Pytań")
    root.geometry("600x700")  # Initial size of the main window

    # Create a StringVar to store the selected theme
    theme_var = StringVar(value="system")

    # Main frame for questions and answers
    frame = ctk.CTkFrame(root, corner_radius=10)
    frame.pack(pady=20, padx=20, fill="both", expand=True)

    # Question label and entry
    question_label = ctk.CTkLabel(frame, text="Pytanie:", font=("Arial", 14))
    question_label.pack(anchor="w", pady=(10, 5))

    question_entry = ctk.CTkTextbox(frame, wrap="word", font=("Arial", 12))
    question_entry.pack(fill="both", padx=10, pady=(0, 10), expand=True)

    # Answers label and entry
    answers_label = ctk.CTkLabel(frame, text="Odpowiedzi (jedna na linię):", font=("Arial", 14))
    answers_label.pack(anchor="w", pady=(10, 5))

    answers_entry = ctk.CTkTextbox(frame, wrap="word", font=("Arial", 12))
    answers_entry.pack(fill="both", padx=10, pady=(0, 10), expand=True)

    # Buttons
    next_button = ctk.CTkButton(frame, text="Dodaj Kolejne Pytanie", command=lambda: add_qna(question_entry, answers_entry, question_counter_label))
    next_button.pack(pady=10, fill="x", padx=10)

    save_button = ctk.CTkButton(frame, text="Zapisz Wszystko", command=lambda: save_all_qna(question_counter_label))
    save_button.pack(pady=10, fill="x", padx=10)

    global question_count
    question_counter_label = ctk.CTkLabel(frame, text=f"Dodano pytań: {question_count}", font=("Arial", 14))
    question_counter_label.pack(pady=(20, 0))

    # Theme selection frame
    theme_frame = ctk.CTkFrame(root, corner_radius=10)
    theme_frame.pack(pady=10, fill="x")

    theme_label = ctk.CTkLabel(theme_frame, text="Wybierz Motyw:", font=("Arial", 14))
    theme_label.grid(row=0, column=0, padx=10)

    light_button = ctk.CTkRadioButton(theme_frame, text="Jasny", variable=theme_var, value="light", command=lambda: ctk.set_appearance_mode("Light"))
    light_button.grid(row=0, column=1, padx=5)

    dark_button = ctk.CTkRadioButton(theme_frame, text="Ciemny", variable=theme_var, value="dark", command=lambda: ctk.set_appearance_mode("Dark"))
    dark_button.grid(row=0, column=2, padx=5)

    root.mainloop()
