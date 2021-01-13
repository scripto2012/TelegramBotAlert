import _sqlite3


class SQLscript:

    def __init__(self, database_file):
        # Подключение к БД и сохранение курсора соединения
        self.connection = _sqlite3.connect(database_file)
        self.cursor = self.connection.cursor()

    def get_sub(self, status = True):
        # Получение всех активных подписчиков
        with self.connection:
            return self.cursor.execute("SELECT * FROM `Subscriptions` WHERE `status` = ?", (status,)).fetchall()

    def sub_exists(self, user_id):
        # Проверка на наличие пользователя в БД
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `Subscriptions` WHERE `user_id` = ?", (user_id,)).fetchall()
            return bool(len(result))

    def add_sub(self, user_id, status = True):
        # Добавление нового подписчика
        with self.connection:
            return self.cursor.execute("INSERT INTO `Subscriptions` (`user_id`, `status`) VALUES (?,?)", (user_id, status))

    def update_sub(self, user_id, status):
        # Обновление статуса подписчика
        return self.cursor.execute("UPDATE `Subscriptions` SET `status` = ? WHERE `user_id` = ?", (status, user_id))

    def get_status(self, user_id):
        return self.cursor.execute("SELECT `status` FROM `Subscriptions` WHERE `user_id` = ?", (user_id,)).fetchall()

    def close(self):
        # Закрытие соединения
        self.connection.close()