import tkinter as tk
from tkinter import ttk
import sys
import os

# Ensure project root is on path
sys.path.insert(0, os.path.dirname(__file__))

from utils.database import initialize_db
from utils.theme import apply_theme, PRIMARY, SECONDARY, HIGHLIGHT, FONT_TITLE
from modules.login import LoginScreen
from modules.register import RegisterScreen
from modules.admin import AdminDashboard
from modules.student import StudentDashboard
from modules.recruiter import RecruiterDashboard


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Campus Recruitment Management System")
        self.geometry("1100x720")
        self.minsize(900, 600)
        self.configure(bg=PRIMARY)

        apply_theme(self)
        initialize_db()

        self._current_frame = None
        self._show_login()

    # ── screen switching ─────────────────────────────────────────────────────
    def _clear(self):
        if self._current_frame:
            self._current_frame.destroy()
            self._current_frame = None

    def _show_login(self):
        self._clear()
        frame = LoginScreen(self, on_login=self._on_login)
        frame.pack(fill="both", expand=True)
        self._current_frame = frame

    def _show_register(self):
        self._clear()
        frame = RegisterScreen(self, on_back=self._show_login)
        frame.pack(fill="both", expand=True)
        self._current_frame = frame

    def _on_login(self, role: str, user: dict | None):
        if role == "register":
            self._show_register()
            return
        self._clear()
        if role == "admin":
            frame = AdminDashboard(self, user, on_logout=self._show_login)
        elif role == "student":
            frame = StudentDashboard(self, user, on_logout=self._show_login)
        elif role == "recruiter":
            frame = RecruiterDashboard(self, user, on_logout=self._show_login)
        else:
            self._show_login()
            return
        frame.pack(fill="both", expand=True)
        self._current_frame = frame


if __name__ == "__main__":
    app = App()
    app.mainloop()
