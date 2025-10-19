

class ProxyErrorException(Exception):
    """Исключение для ошибок прокси"""
    pass

class FileOperationException(Exception):
    """Исключение для ошибок работы с файлами"""
    pass

class StatsGenerationException(Exception):
    """Исключение для ошибок генерации статистики"""
    pass

class ApiTelegramException(Exception):
    """Исключение для ошибок telegram"""
    pass