import sys
import random
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette
from PyQt6.QtCore import QEvent, QSize, Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QStyle,
    QToolButton,
    QVBoxLayout,
    QWidget,
)
Colour1 = "FFFFFF"
Colour2 = "1518D344"
backgroundMain = "FFFFFF"
x_scale = 1080
y_scale = 720

class CustomTitleBar(QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.initial_pos = None
        title_bar_layout = QHBoxLayout(self)
        title_bar_layout.setContentsMargins(1, 1, 1, 1)
        title_bar_layout.setSpacing(2)
        self.title = QLabel(f"{self.__class__.__name__}", self)
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title.setStyleSheet(
            """
        QLabel { text-transform: uppercase; 
        font-size: 10pt;
        
        font-family:    serif;
        font-style: italic;
        margin-left: 48px;
        color: #6B0594C9}
        
        """
        )

        if title := parent.windowTitle():
            self.title.setText(title)
        
        title_bar_layout.addWidget(self.title)
        # Min button
        self.min_button = QToolButton(self)
        min_icon = QIcon()
        min_icon.addFile("GUI\img\green.svg")
        self.min_button.setIcon(min_icon)
        self.min_button.clicked.connect(self.window().showMinimized)

        # Max button
        self.max_button = QToolButton(self)
        max_icon = QIcon()
        max_icon.addFile("GUI\img\yellow.svg")
        self.max_button.setIcon(max_icon)
        self.max_button.clicked.connect(self.window().showMaximized)

        # Close button
        self.close_button = QToolButton(self)
        close_icon = QIcon()
        close_icon.addFile("GUI\img\\red-circle.svg")  # Close has only a single state.
        self.close_button.setIcon(close_icon)
        self.close_button.clicked.connect(self.window().close)

        # Normal button
        self.normal_button = QToolButton(self)
        normal_icon = QIcon()
        normal_icon.addFile("GUI\img\yellow.svg")
        self.normal_button.setIcon(normal_icon)
        self.normal_button.clicked.connect(self.window().showNormal)
        self.normal_button.setVisible(False)
        
        
        # Back button 
        self.back_button = QToolButton(self)
        back_icon = QIcon()
        back_icon.addFile("GUI\img\\back.svg")
        self.back_button.setIcon(back_icon)
        self.back_button.clicked.connect(self.window().showNormal)
        # Forward button
        self.Forward_button = QToolButton(self)
        Forward_icon = QIcon()
        Forward_icon.addFile("GUI\img\\forward.svg")
        self.Forward_button.setIcon(Forward_icon)
        self.Forward_button.clicked.connect(self.window().showNormal)
        # Add buttons
        buttons = [
            self.back_button,
            self.Forward_button,
            self.min_button,
            self.normal_button,
            self.max_button,
            self.close_button,
        ]
        for button in buttons:
            button.setFocusPolicy(Qt.FocusPolicy.NoFocus)
            button.setFixedSize(QSize(16, 16))
            button.setStyleSheet(
                """QToolButton {
                    border: none;
                    padding: 1px;
                }
                """
            )
            title_bar_layout.addWidget(button)

    def window_state_changed(self, state):
        if state == Qt.WindowState.WindowMaximized:
            self.normal_button.setVisible(True)
            self.max_button.setVisible(False)
        else:
            self.normal_button.setVisible(False)
            self.max_button.setVisible(True)

        
class MainFrame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Root2Ramming")
        self.resize(x_scale, y_scale)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        central_widget = QWidget()
        # This container holds the window contents, so we can style it.
        central_widget.setObjectName("Container")
        _styleSheet = f"""
            #Container {{
            background: qlineargradient(x1:0 y1:0, x2:1 y2:1, stop:0 #{Colour1} stop:1 #{Colour2});
            border-radius: 10px;
            background-color:#FFFFFF;
            }}
        """
        central_widget.setStyleSheet(_styleSheet)
        
        self.title_bar = CustomTitleBar(self)

        work_space_layout = QVBoxLayout()
        work_space_layout.setContentsMargins(11, 11, 11, 11)
        work_space_layout.addWidget(QLabel("Hello, World!", self))
        centra_widget_layout = QVBoxLayout()
        centra_widget_layout.setContentsMargins(0, 0, 0, 0)
        centra_widget_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        centra_widget_layout.addWidget(self.title_bar)
        centra_widget_layout.addLayout(work_space_layout)

        central_widget.setLayout(centra_widget_layout)
        self.setCentralWidget(central_widget)

    def changeEvent(self, event):
        if event.type() == QEvent.Type.WindowStateChange:
            self.title_bar.window_state_changed(self.windowState())
        super().changeEvent(event)
        event.accept()

    def window_state_changed(self, state):
        self.normal_button.setVisible(state == Qt.WindowState.WindowMaximized)
        self.max_button.setVisible(state != Qt.WindowState.WindowMaximized)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.initial_pos = event.position().toPoint()
        super().mousePressEvent(event)
        event.accept()

    def mouseMoveEvent(self, event):
        if self.initial_pos is not None:
            delta = event.position().toPoint() - self.initial_pos
            self.window().move(
                self.window().x() + delta.x(),
                self.window().y() + delta.y(),
            )
        super().mouseMoveEvent(event)
        event.accept()

    def mouseReleaseEvent(self, event):
        self.initial_pos = None
        super().mouseReleaseEvent(event)
        event.accept()

        
