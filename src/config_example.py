# DataGym Bot Configuration
# Copy this file to config.py and fill in your values

import os

# Telegram Bot API
TELEGRAM_TOKEN = "your_telegram_bot_token_here"

# Admin configuration  
ADMIN_USERNAME = "your_telegram_username"
ADMIN_IDS = [123456789]  # Your Telegram ID

# File paths
QUESTIONS_FILE = "data/questions.json"
USER_STATS_FILE = "data/user_stats.json" 
LOGS_DIR = "logs/"

# Bot settings
ENABLE_PREMIUM = True
ENABLE_STATISTICS = True
DAILY_TOP_ENABLED = True

# Premium settings
PREMIUM_TOPICS = [
    "Библиотека Matplotlib",
    "Оконные функции SQL", 
    "Docker",
    "Основы Linux: Терминал",
    "Статистические гипотезы",
    "ML",
    "Python middle", 
    "Pandas middle",
    "Практическое применение алгоритмов сортировки"
]
