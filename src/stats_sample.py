# stats_sample.py - только безопасные математические функции

import math
from datetime import datetime, timedelta

def calculate_progress(current, target):
    """Базовый расчет прогресса"""
    if current >= target:
        return 1.0
    return min(current / target, 1.0) if target > 0 else 0.0

def calculate_streak(dates_list):
    """Расчет streak по списку дат (общая логика)"""
    if not dates_list:
        return 0
        
    sorted_dates = sorted(dates_list)
    streak = 1
    # ... общая логика без привязки к вашей структуре данных
