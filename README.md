# DataGym - Тренажер Data Science  

> Telegram бот с 1000+ вопросами для ежедневной практики Data Science  

## 🎯 О проекте
DataGym помогает специалистам Data Science поддерживать и улучшать навыки через систему микро-обучения. Проходите тесты, отслеживайте прогресс и становитесь экспертом!  

## 🚀 Возможности
- **1000+ вопросов** по 15+ темам Data Science
- **Персональная статистика** прогресса
- **Работа над ошибками** - учитесь на своих ошибках
- **Система достижений** и ежедневный streak
- **Premium темы** - ML, Docker, Linux, продвинутый Python

## 🛠 Технологии
- Python 3.8+
- pyTelegramBotAPI
- JSON для хранения данных
- Docker (в планах)

## 📦 Установка
# 1. Клонируйте репозиторий
git clone https://github.com/ваш-ник/datagym-edtech.git  

# 2. Установите зависимости
pip install -r requirements.txt  

# 3. Настройте конфигурацию
cp config_example.py config.py  
# отредактируйте config.py - добавьте Telegram токен

# 4. Запустите бота
python src/bot.py  

📊 Статистика проекта  
1082 вопроса и постоянно растущая база  

15+ тем от основ Python до продвинутого ML  

Ежедневные обновления и новые вопросы  

2 режима обучения: тесты и работа над ошибками  

🎯 Для кого этот проект  
- Студенты Data Science 
- Junior/Middle специалисты 
- Все, кто хочет поддерживать навыки в тонусе 

📄 Лицензия 
MIT 

### **2. requirements.txt**:
pyTelegramBotAPI==4.16.1 
requests==2.31.0 
urllib3==2.2.1 
python-dotenv==1.0.1  


### **3. config_example.py:**
DataGym Bot Configuration 
Copy this file to config.py and fill in your values 

#### Telegram Bot API
TELEGRAM_TOKEN = "your_telegram_bot_token_here" 

#### Admin configuration
ADMIN_USERNAME = "your_telegram_username" 
ADMIN_IDS = [123456789]  # Your Telegram ID 

#### File paths
QUESTIONS_FILE = "data/questions.json" 
USER_STATS_FILE = "data/user_stats.json" 
LOGS_DIR = "logs/" 

#### Bot settings
ENABLE_PREMIUM = True 
ENABLE_STATISTICS = True 
