import sys
from PyQt5.QtWidgets import QApplication, QDialog, QTableWidgetItem, QMessageBox
from PyQt5.uic import loadUi
from queries import insert_schedule_data

class ScheduleApp(QDialog):
    def __init__(self):
        super(ScheduleApp, self).__init__()
        loadUi("ui/window.ui", self)

        self.pushButton.clicked.connect(self.add_schedule)

    def add_schedule(self):
        # Получаем данные из QTableWidget
        DayOfWeek = self.tableWidget.item(0, 0).text()
        StartTime = self.tableWidget.item(0, 1).text()
        EndTime = self.tableWidget.item(0, 2).text()
        BreakStartTime = self.tableWidget.item(0, 3).text()
        BreakEndTime = self.tableWidget.item(0, 4).text()

        # Проверяем, что все поля заполнены
        if not all([DayOfWeek, StartTime, EndTime, BreakStartTime, BreakEndTime]):
            QMessageBox.warning(self, "Ошибка", "Заполните все поля.")
            return

        # Преобразовываем в нужные типы данных (если необходимо)
        try:
            # Пример: int_value = int(StartTime)
            # Повторите для других значений, если они должны быть целыми числами
            pass
        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Некорректный формат числа.")
            return

        # Вставляем данные в базу данных
        schedule_data = (DayOfWeek, StartTime, EndTime, BreakStartTime, BreakEndTime)

        try:
            insert_schedule_data(schedule_data)
            QMessageBox.information(self, "Успех", "Данные расписания добавлены успешно!")
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка при добавлении данных: {str(e)}")

        # Очищаем поля ввода после успешного добавления
        self.clear_input_fields()

    def clear_input_fields(self):
        for col in range(self.tableWidget.columnCount()):
            item = QTableWidgetItem("")
            self.tableWidget.setItem(0, col, item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ScheduleApp()
    window.show()
    sys.exit(app.exec_())
