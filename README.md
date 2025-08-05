# 🎮 Custom Discord Rich Presence

This project allows you to display **custom Rich Presence in Discord** for games, websites, or services that **don’t support it natively**. It collects activity data from multiple sources and sends it to Discord, as if it were an official integration.

> ⚠️ Discord RPC works **locally only**. This means the scripts must run on the **same machine where Discord is open**.

---

## 🔧 Why This Exists?

Discord has native integrations for major apps and games. But if you:
- Watch anime on unofficial sites (like AniLibria),
- Play games without official Discord support,
- Want to show **custom activity** in your status,

then there's **no native solution**. This project fixes that with a **plugin-based system**.

---

## 🚀 How It Works

Each plugin handles a specific source of activity (anime, Dota 2, etc.). All plugins send formatted data to a single server which updates Discord via `pypresence`.

---

## 📦 Installation

1. Install Python **3.15+**.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
Set your Discord App IDs in config.py.

🆔 How to Get Your Discord App ID
Go to Discord Developer Portal

Create a new application

Copy the Application ID

Set up your assets under Rich Presence → Art Assets

Example config.py:

PRESENCE_APPS = {
    "anime": 123,
    "dota": 321,
}

✅ Current Plugins
Plugin	Description
anime	Tracks anime progress (e.g. on AniLibria) via browser extension and updates Discord.
dota	Uses GSI to detect hero and game phase. Also monitors the Dota 2 process to close activity when game exits.

🛠 TODO
 Add more plugins (YouTube, Steam, Twitch, etc.)

 Real activity expiration via database state

 Unified startup with Docker (partially implemented)

 Async rewrite using FastAPI

 Activity cache & conflict resolution system

🐳 Docker (try with fault,experimental)
This project included partial Docker support to run everything from a single container:

server.py — main Flask server

sender.py — loads plugins

background_tasks/ — runs background jobs (like dota_monitor)

However, due to Discord RPC limitations (it works only on the local machine), running the project in Docker is not recommended yet,but i wish i will solve it soon.

👨‍💻 About This Project
Author: @nex1n

This tool is meant to fill the gap for lesser-known platforms or games that lack official Discord Rich Presence. You can easily extend it by creating your own plugin and adding a new App ID in config.py.

📬 Contribute
If you find this useful or want to contribute:

Fork the repo

Add your plugin

Submit a pull request!