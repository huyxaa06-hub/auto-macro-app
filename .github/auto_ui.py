import tkinter as tk
from tkinter import messagebox, scrolledtext
import threading
import time
import subprocess

class AutoGameApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Auto Game Control Panel & ADB Apps")
        self.root.geometry("350x550")
        self.root.attributes("-topmost", True)  # Luôn hiển thị lên trên cùng
        
        self.is_running = False

        # --- Tiêu đề ---
        self.title_label = tk.Label(root, text="BOT AUTO GAME & ADB", font=("Arial", 13, "bold"), fg="green")
        self.title_label.pack(pady=5)

        # --- Trạng thái ---
        self.status_label = tk.Label(root, text="Trạng thái: Đang dừng", font=("Arial", 9), fg="red")
        self.status_label.pack(pady=2)

        # --- Khu vực cài đặt Auto ---
        settings_frame = tk.LabelFrame(root, text=" Tùy chọn Auto ")
        settings_frame.pack(fill="x", padx=10, pady=5)

        tk.Label(settings_frame, text="Khoảng thời gian click (giây):").pack(anchor="w", padx=5, pady=2)
        self.delay_entry = tk.Entry(settings_frame)
        self.delay_entry.insert(0, "1")
        self.delay_entry.pack(fill="x", padx=5, pady=2)

        # --- Các nút điều khiển Auto ---
        btn_frame = tk.Frame(root)
        btn_frame.pack(fill="x", padx=10, pady=5)

        self.start_btn = tk.Button(btn_frame, text="Bắt đầu Auto", bg="green", fg="white", font=("Arial", 9, "bold"), command=self.start_auto)
        self.start_btn.pack(side="left", expand=True, fill="x", padx=2)

        self.stop_btn = tk.Button(btn_frame, text="Dừng", bg="red", fg="white", font=("Arial", 9, "bold"), state="disabled", command=self.stop_auto)
        self.stop_btn.pack(side="right", expand=True, fill="x", padx=2)

        # --- Khu vực ADB App Manager ---
        adb_frame = tk.LabelFrame(root, text=" Quản lý App qua ADB ")
        adb_frame.pack(fill="both", expand=True, padx=10, pady=5)

        self.btn_load_apps = tk.Button(adb_frame, text="Xem danh sách App đã cài", bg="blue", fg="white", font=("Arial", 9, "bold"), command=self.load_adb_apps)
        self.btn_load_apps.pack(fill="x", padx=5, pady=5)

        # Khung văn bản cuộn để hiển thị danh sách app
        self.app_text = scrolledtext.ScrolledText(adb_frame, wrap=tk.WORD, height=10, font=("Consolas", 8))
        self.app_text.pack(fill="both", expand=True, padx=5, pady=5)

    def start_auto(self):
        if not self.is_running:
            self.is_running = True
            self.status_label.config(text="Trạng thái: Đang chạy...", fg="green")
            self.start_btn.config(state="disabled")
            self.stop_btn.config(state="normal")
            
            self.thread = threading.Thread(target=self.run_auto_loop)
            self.thread.daemon = True
            self.thread.start()

    def stop_auto(self):
        self.is_running = False
        self.status_label.config(text="Trạng thái: Đang dừng", fg="red")
        self.start_btn.config(state="normal")
        self.stop_btn.config(state="disabled")

    def run_auto_loop(self):
        while self.is_running:
            try:
                delay = float(self.delay_entry.get())
            except ValueError:
                delay = 1.0

            print(f"[Auto] Đang thực hiện tác vụ... (Chu kỳ: {delay}s)")
            time.sleep(delay)

    def load_adb_apps(self):
        """Hàm chạy lệnh ADB để lấy danh sách ứng dụng và hiển thị lên giao diện"""
        self.app_text.delete("1.0", tk.END)
        self.app_text.insert(tk.END, "Đang tải danh sách ứng dụng...\n")
        
        # Chạy trong Thread riêng để tránh đơ giao diện khi chờ lệnh ADB
        threading.Thread(target=self._fetch_apps_thread, daemon=True).start()

    def _fetch_apps_thread(self):
        try:
            # Chạy lệnh adb pm list packages. 
            # Lưu ý: Nếu chạy trực tiếp trên Android qua Termux, ta có thể dùng adb kết nối local hoặc pm list packages trực tiếp nếu có quyền root/shizuku.
            # Ở đây dùng lệnh adb chuẩn:
            result = subprocess.run(["adb", "shell", "pm", "list", "packages"], capture_output=True, text=True, timeout=10)
            
            if result.returncode == 0:
                apps = result.stdout
                self.root.after(0, lambda: self.update_app_text(apps))
            else:
                err_msg = result.stderr if result.stderr else "Lỗi kết nối ADB hoặc chưa bật ADB Debugging / chưa cấp quyền."
                self.root.after(0, lambda: self.update_app_text(f"Lỗi: {err_msg}"))
        except Exception as e:
            self.root.after(0, lambda: self.update_app_text(f"Ngoại lệ: {str(e)}\nHãy chắc chắn bạn đã cài android-tools."))

    def update_app_text(self, text):
        self.app_text.delete("1.0", tk.END)
        self.app_text.insert(tk.END, text)

if __name__ == "__main__":
    root = tk.Tk()
    app = AutoGameApp(root)
    root.mainloop()
