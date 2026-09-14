from PyQt6.QtWidgets import QApplication, QMainWindow,QTextEdit
from ui_main import Ui_DataAgentUI
from agent import Agent

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DataAgentUI()
        self.ui.setupUi(self)

        self.agent = Agent()

        # اتصال دکمه‌ها
        self.ui.btn_Start.clicked.connect(self.run_agent)
        self.ui.txt_logInput.keyPressEvent = self.input_keypress


    def input_keypress(self, event):
        if event.key() == 16777220:  # Qt.Key_Return
            self.run_agent()
        else:
            QTextEdit.keyPressEvent(self.ui.txt_logInput, event)


    def run_agent(self):
        user_text = self.ui.txt_logInput.toPlainText().strip()
        if not user_text:
            return

        answer = self.agent.ask(user_text)

        # نمایش خروجی
        
        self.ui.txt_logOutput.append(f"Agent: {answer}\n")

        # پاک کردن ورودی
        self.ui.txt_logInput.clear()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
