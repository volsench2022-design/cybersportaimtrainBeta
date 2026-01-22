import tkinter as tk
import random
from tkinter import messagebox

score = 0
lives = 5
level = 1
speed = 1000  # Початкова швидкість в мілісекундах
goal = 100

# --- Налаштування вікна ---
def move_character():
    """Функція автоматичного переміщення"""
    global speed
    if lives > 0 and score < goal:
        new_x = random.randint(50, 700)
        new_y = random.randint(80, 500)
        btn_target.place(x=new_x, y=new_y)
        root.after(speed, move_character)


def on_click():
    """Логіка при попаданні по персонажу"""
    global score, speed, level
    if lives <= 0:
        return

    score += 1

    # Кожні 5 очок збільшуємо рівень та швидкість
    if score % 5 == 0:
        level += 1
        speed = max(300, speed - 50)  # Не швидше ніж 300 мс
        root.config(bg=random.choice(
            ["#f0f0f0", "#e1f5fe", "#ffe0b2", "#e8f5e9", "#f3e5f5"]
        ))

    if score >= goal:
        messagebox.showinfo("ПЕРЕМОГА!", f"Ти набрав {goal} очок! Рівень: {level}")
        reset_game()
        return

    update_ui()


def miss_click(event):
    """Штраф за клік повз персонажа"""
    global lives
    if event.widget == root:
        lives -= 1
        update_ui()
        root.config(bg="#ffcdd2")
        root.after(100, lambda: root.config(bg="#f0f0f0"))

        if lives <= 0:
            messagebox.showerror("GAME OVER", f"Життя закінчилися! Твій рахунок: {score}")
            reset_game()


def update_ui():
    """Оновлення тексту на екрані"""
    label_info.config(text=f"Очки: {score} | Життя: {lives} | Рівень: {level}")


def reset_game():
    """Скидання всіх параметрів"""
    global score, lives, speed, level
    score = 0
    lives = 5
    speed = 1000
    level = 1
    update_ui()
    move_character()


# --- Головне вікно та елементи інтерфейсу ---
root = tk.Tk()
root.title("Cyber Hunter 2026")
root.geometry("800x600")
root.resizable(False, False)

# Фоновий клік для штрафу
root.bind("<Button-1>", miss_click)

# Панель інформації
label_info = tk.Label(
    root,
    text="Очки: 0 | Життя: 5 | Рівень: 1",
    font=("Courier New", 20, "bold"),
    bg="#333",
    fg="white"
)
label_info.pack(fill="x")

btn_target = tk.Button(
    root,
    text="lol",
    font=("Arial", 25),
    command=on_click,
    bg="#4caf50",
    fg="white",
    width=3,
    relief="raised"
)
btn_target.place(x=350, y=250)

# Запуск гри
move_character()
root.mainloop()
