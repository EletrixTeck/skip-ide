import requests
import yaml
import tkinter as tk
from tkinter import messagebox
current_version = 0.1
def check_for_updates():
    url = 'https://raw.githubusercontent.com/EletrixtimeYT/skip-ide/main/version.yaml'
    try:
        response = requests.get(url)
        response.raise_for_status()
        latest_version = yaml.safe_load(response.content)['version']
        if latest_version != current_version:
            message = f"A new version ({latest_version}) of the program is available! Would you like to download it?"
            if messagebox.askokcancel("Update Available", message):
                import webbrowser
                webbrowser.open('https://github.com/EletrixtimeYT/skip-ide/releases/latest')
    except:
        pass
syntax = ["test"]