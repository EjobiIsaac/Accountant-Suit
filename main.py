import webview
import os
html_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "index.html")
webview.create_window("Accountant Suite - 4-in-1 | Uganda", html_path, width=1200, height=800)
webview.start()
