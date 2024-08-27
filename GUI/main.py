import Define as md

class OpenScreen(md.MainFrame):
    def __init__(self):
        super().__init__()

        
    
if __name__ == "__main__":
    app = md.QApplication([])
    widget = OpenScreen()
    widget.show()
    app.exec()