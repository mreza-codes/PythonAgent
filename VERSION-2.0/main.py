from PyQt6.QtWidgets import QApplication, QMainWindow, QTextEdit
from ui_main import Ui_DataAgentUI
from agent import Agent

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_DataAgentUI()
        self.ui.setupUi(self)

        # Initialize agent
        self.agent = Agent()

        # Connect buttons
        self.ui.btn_Start.clicked.connect(self.run_agent)

        # Override keyPressEvent for input box
        self.ui.txt_logInput.keyPressEvent = self.input_keypress


    def input_keypress(self, event):
        # If user presses Enter key, run the agent
        if event.key() == 16777220:  # Qt.Key_Return
            self.run_agent()
        else:
            # Default key behavior
            QTextEdit.keyPressEvent(self.ui.txt_logInput, event)


    def run_agent(self):
        # Get user input
        user_text = self.ui.txt_logInput.toPlainText().strip()
        if not user_text:
            return

        # Ask the agent
        answer = self.agent.ask(user_text)

        # Display output (overwrite previous output)
        self.ui.txt_logOutput.setPlainText(f"Agent: {answer}")

        # Clear input box
        self.ui.txt_logInput.clear()


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
