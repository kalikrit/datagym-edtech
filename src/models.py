class UserState:
    """Класс для хранения состояния пользователя"""
    def __init__(self):
        self.current_test = []
        self.current_question = 0
        self.correct_answers = 0
        self.test_type = None
        self.test_in_progress = False
        self.session_id = None
        self.max_questions = 10  # Жесткое ограничение для всех тестов
