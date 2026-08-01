# 🤖 Telegram Math Daily Bot

An automated study assistant built in Python that delivers daily advanced math problems, video tutorials, and motivational quotes directly to your Telegram channel or personal chat.

Powered by **GitHub Actions**, this bot runs fully on cloud infrastructure automatically every single day—completely free and without needing any local server or computer to stay powered on.

---

## 🌟 Features

* **Advanced Curriculum:** Tailored for 8th/9th grade scientific track mathematics (Linear functions, systems of equations, algebraic fractions, analytical geometry, exponential laws, etc.).
* **Daily Progression:** Automatically cycles through a comprehensive 20-day study plan based on the day of the month.
* **Curated Video Resources:** Links each daily topic to a curated educational video walkthrough.
* **Daily Motivation:** Randomly selects and sends an inspiring quote every morning to keep you driven.
* **Zero-Cost Hosting:** Runs serverless via GitHub Actions Cron scheduler.
* **Secure Architecture:** Sensitive tokens and chat IDs are kept safe using GitHub Repository Secrets.

---

## 🕒 Schedule & Timing

* **Automatic Run:** Executes every day at **06:00 UTC** (08:00 AM Israel Standard Time).
* **Manual Trigger:** Can be manually executed at any time directly from the GitHub Actions tab.

---

## 📂 Project Structure


├── math_bot.py                 # Main Python script handling logic, curriculum, and Telegram API
└── .github
    └── workflows
        └── run_bot.yml   # GitHub Actions workflow configuration (Cron & Environment)

## 🛠️ Tech Stack
​Language: Python 3.10+
​HTTP Requests: requests library
​Automation & CI/CD: GitHub Actions (Cron Jobs)
​Messaging Platform: Telegram Bot API
## ⚙️ Setup & Installation (For Your Own Bot)
​If you want to fork or set up this project for yourself, follow these steps:
​1. Create a Telegram Bot
​Message @BotFather on Telegram to create a new bot and get your Bot Token.
​Message @userinfobot to find your unique numeric Chat ID.
​2. Configure GitHub Repository Secrets
​In your GitHub repository, go to Settings -> Secrets and variables -> Actions and add two new repository secrets:
​TELEGRAM_BOT_TOKEN — Your Telegram Bot Token.
​TELEGRAM_CHAT_ID — Your personal or group Chat ID.
​3. Add the Files
​Upload math_bot.py and .github/workflows/run_bot.yml into your repository.
​4. Test It Manually
​Go to the Actions tab in your repository, select Run Math Bot Daily, and click Run workflow to test it out instantly!
## 📄 License
​This project is open-source and available under the MIT License.
