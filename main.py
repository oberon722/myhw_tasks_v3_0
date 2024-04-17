import json
import datetime
import os


class NoteApp:
    """
    Класс для работы с заметками.
    """

    def __init__(self, notes_file="notes.json"):
        """
        Инициализация приложения для работы с заметками.

        :param notes_file: Файл для сохранения заметок.
        """
        self.notes_file = notes_file

    def load_notes(self):
        """
        Загрузка заметок из файла.

        :return: Список заметок.
        """
        if os.path.exists(self.notes_file):
            with open(self.notes_file, "r") as f:
                return json.load(f)
        else:
            return []

    def save_notes(self, notes):
        """
        Сохранение заметок в файл.

        :param notes: Список заметок.
        """
        with open(self.notes_file, "w") as f:
            json.dump(notes, f, indent=4)

    def add_note(self, title, message):
        """
        Добавление новой заметки.

        :param title: Заголовок заметки.
        :param message: Текст заметки.
        """
        notes = self.load_notes()
        note = {
            "id": len(notes) + 1,
            "title": title,
            "message": message,
            "timestamp": str(datetime.datetime.now())
        }
        notes.append(note)
        self.save_notes(notes)
        print("Заметка успешно добавлена.")

    def read_notes(self, date_filter=None):
        """
        Чтение заметок с возможностью фильтрации по дате.

        :param date_filter: Дата для фильтрации заметок.
        """
        notes = self.load_notes()
        if date_filter:
            filtered_notes = [note for note in notes if date_filter in note["timestamp"]]
            notes = filtered_notes
        if notes:
            print("Перечень всех заметок:")
            for note in notes:
                print(
                    f"{note['id']}\t{note['timestamp']}\t{note['title']}\t{note['message']}"
                )
        else:
            print("Заметок не найдено.")

    def list_notes(self):
        """
        Вывод списка всех заметок.
        """
        notes = self.load_notes()
        if notes:
            print("Список заметок:")
            for note in notes:
                print(
                    f"ID: {note['id']}"
                    f"\nДата/время: {note['timestamp']}"
                    f"\nЗаголовок: {note['title']}"
                    f"\nТекст заметки: {note['message']}\n"
                )
        else:
            print("Список заметок пуст.")

    def delete_note(self, note_id):
        """
        Удаление заметки по ID.

        :param note_id: ID заметки для удаления.
        """
        notes = self.load_notes()
        notes = [note for note in notes if note['id'] != note_id]
        self.save_notes(notes)
        print("Заметка успешно удалена.")

    def edit_note(self, note_id, new_title, new_message):
        """
        Редактирование заметки.

        :param note_id: ID заметки для редактирования.
        :param new_title: Новый заголовок заметки.
        :param new_message: Новый текст заметки.
        """
        notes = self.load_notes()
        for note in notes:
            if note['id'] == note_id:
                note['title'] = new_title
                note['message'] = new_message
                note['timestamp'] = str(datetime.datetime.now())
                self.save_notes(notes)
                print("Заметка успешно отредактирована.")
                return
        print("Заметка с указанным ID не найдена.")

    def start(self):
        """
        Запуск приложения.
        """
        print("\nДобро пожаловать в консольное приложение для заметок!")
        print("Чтобы начать, выберите одно из следующих действий:")
        print("0. Инструкция")
        print("1. Добавить заметку")
        print("2. Просмотреть заметки")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Перечень всех заметок")
        print("6. Выход")

        while True:
            choice = input("Введите номер действия: ")

            if choice == "0":
                self.show_instructions()
            elif choice == "1":
                title = input("Введите заголовок заметки: ")
                message = input("Введите текст заметки: ")
                self.add_note(title, message)
            elif choice == "2":
                date_filter = input(
                    "Введите дату (в формате ГГГГ-ММ-ДД) для фильтрации "
                    "заметок (оставьте пустым, чтобы пропустить): "
                )
                self.read_notes(date_filter)
            elif choice == "3":
                note_id = int(input("Введите ID заметки для редактирования: "))
                new_title = input("Введите новый заголовок заметки: ")
                new_message = input("Введите новый текст заметки: ")
                self.edit_note(note_id, new_title, new_message)
            elif choice == "4":
                note_id = int(input("Введите ID заметки для удаления: "))
                self.delete_note(note_id)
            elif choice == "5":
                self.list_notes()
            elif choice == "6":
                print("Спасибо за использование приложения! До свидания.")
                break
            else:
                print("Неверный ввод. Попробуйте еще раз.")

    @staticmethod
    def show_instructions():
        """
        Вывод инструкции по использованию приложения.
        """
        print("\n** Инструкция **\n")
        print("Это консольное приложение позволяет вам создавать, просматривать,")
        print("редактировать и удалять заметки. Каждая заметка содержит заголовок,")
        print("текст и дату/время создания.")
        print("\n** Инструкции **\n")
        print("1. Добавить заметку: Введите 1, затем введите заголовок и текст заметки по запросу.")
        print("2. Просмотреть заметки: Введите 2, и, при желании, укажите дату для фильтрации заметок.")
        print("3. Редактировать заметку: Введите 3, затем введите ID заметки для редактирования,")
        print("   а затем введите новый заголовок и текст заметки.")
        print("4. Удалить заметку: Введите 4, затем введите ID заметки для удаления.")
        print("5. Перечень всех заметок: Введите 5, чтобы вывести список всех заметок.")
        print("6. Выход: Введите 6, чтобы завершить выполнение программы.\n")


if __name__ == "__main__":
    app = NoteApp()
    app.start()
