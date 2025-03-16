import tkinter as tk
import pyautogui
import threading

class MousePositionTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("鼠标位置追踪器")
        
        self.label = tk.Label(root, text="鼠标位置: (0, 0)", font=("Arial", 24))
        self.label.pack(pady=20)
        
        # 绑定鼠标事件
        self.root.bind("<ButtonPress-1>", self.start_move)
        self.root.bind("<ButtonRelease-1>", self.stop_move)
        self.root.bind("<B1-Motion>", self.on_move)
        
        self.update_position()
    
    def start_move(self, event):
        self.x = event.x
        self.y = event.y
    
    def stop_move(self, event):
        self.x = None
        self.y = None
    
    def on_move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.root.winfo_x() + deltax
        y = self.root.winfo_y() + deltay
        self.root.geometry(f"+{x}+{y}")
    
    def update_position(self):
        x, y = pyautogui.position()
        self.label.config(text=f"鼠标位置\n({x}, {y})")
        self.root.after(100, self.update_position)

def start_tracker():
    root = tk.Tk()
    # 设置窗口在屏幕右上角
    screen_width = root.winfo_screenwidth()
    root.geometry(f"+{screen_width - 300}+0")
    
    app = MousePositionTracker(root)
    root.mainloop()

if __name__ == "__main__":
    start_tracker()
