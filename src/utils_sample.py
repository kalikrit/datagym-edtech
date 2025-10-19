import json
import random
import logging
from datetime import datetime
from pathlib import Path

logger = logging.getLogger(__name__)

def format_question_text(text):
    """Экранирует спецсимволы Markdown/V2 и форматирует текст вопроса"""
    if not isinstance(text, str):
        return str(text)

    MD_SPECIAL_CHARS = r'_*[]()~`>#+-=|{}.!'
    for char in MD_SPECIAL_CHARS:
        text = text.replace(char, f'\\{char}')
    return text.replace('\\n', '\n').replace('\\t', '\t')

def format_code_block(text):
    """Оборачивает код в backticks для лучшего отображения"""
    import re
    patterns = [
        r"(print\(.*?\))",
        r"([a-z]+\[.*?\])", 
        r"(def\s+\w+\(.*?\):)",
        r"([a-z]+\(.*?\))"
    ]
    for pattern in patterns:
        text = re.sub(pattern, r"`\1`", text)
    return text

def shuffle_questions(questions):
    """Перемешивает вопросы и варианты ответов"""
    if not questions:
        return []
    
    shuffled = questions.copy()
    random.shuffle(shuffled)
    
    for q in shuffled:
        options = q['options'].copy()
        correct = options[q['correct']]
        random.shuffle(options)
        q['correct'] = options.index(correct)
        q['options'] = options
        
    return shuffled
