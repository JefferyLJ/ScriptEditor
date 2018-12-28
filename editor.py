import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.Qsci import *
from lexer import Lexer


class CustomMainWindow(QMainWindow):
    def __init__(self):
        super(CustomMainWindow, self).__init__()

        # Window setup
        # --------------

        # 1. Define the geometry of the main window
        self.setGeometry(300, 300, 800, 400)
        self.setWindowTitle("QScintilla Test")

        # 2. Create frame and layout
        self.__frm = QFrame(self)
        self.__frm.setStyleSheet("QWidget { background-color: #ffeaeaea }")
        self.__lyt = QVBoxLayout()
        self.__frm.setLayout(self.__lyt)
        self.setCentralWidget(self.__frm)
        self.__myFont = QFont()
        self.__myFont.setPointSize(14)

        # 3. Place a button
        self.__btn = QPushButton("Qsci")
        self.__btn.setFixedWidth(50)
        self.__btn.setFixedHeight(50)
        self.__btn.clicked.connect(self.__btn_action)
        self.__btn.setFont(self.__myFont)
        self.__lyt.addWidget(self.__btn)

        # QScintilla editor setup
        # ------------------------

        # ! Make instance of QsciScintilla class!
        self.__editor = QsciScintilla()
        self.__editor.setText("Hello\n")
        self.__editor.append("world")
        self.__editor.setLexer(None)
        self.__editor.setUtf8(True)  # Set encoding to UTF-8
        self.__editor.setFont(self.__myFont)  # Will be overridden by lexer!

        # ! Add editor to layout !
        self.__lyt.addWidget(self.__editor)

        # Add wraper
        self.__editor.setWrapMode(QsciScintilla.WrapWord)
        self.__editor.setWrapVisualFlags(QsciScintilla.WrapFlagByText)

        self.__editor.setTabWidth(4)
        self.__editor.setIndentationGuides(True)
        self.__editor.setAutoIndent(True)

        # set caret
        self.__editor.setCaretForegroundColor(QColor("#000"))
        self.__editor.setCaretLineVisible(True)
        self.__editor.setCaretLineBackgroundColor(QColor("#e0e0e0"))

        # Set margin
        self.__editor.setMarginType(0, QsciScintilla.NumberMargin)
        self.__editor.setMarginWidth(0, "000")
        self.__editor.setMarginsForegroundColor(QColor("#ff0000ff"))
        self.__editor.setMarginsBackgroundColor(QColor("#e0e0e0"))
        self.__editor.setMarginSensitivity(0, True)
        self.__editor.marginClicked.connect(self.margin_function)

        # add lexer
        self.__lexer = Lexer(self.__editor)
        self.__editor.setLexer(self.__lexer)

        # indicator action
        self.__editor.indicatorClicked.connect(self.some_function)
        self.__editor.indicatorReleased.connect(self.other_function)

        # Set auto completion
        self.__editor.setAutoCompletionThreshold(1)
        # self.__editor.setAutoCompletionCaseSensitivity(False)
        # self.__editor.setAutoCompletionReplaceWord(True)
        # self.__editor.setAutoCompletionUseSingle(QsciScintilla.AcusAlways)
        self.__api = QsciAPIs(self.__lexer)
        autocompletions = [
            "clickById",
            "add(int arg_1, float arg_2) Add two integers together",
            "subtract(int arg_1, test arg_2)",
            "subtract(float arg_1, float arg_2)",
            "subtract(test arg_1, test arg_2)",
            "divide(float div_1, float div_2)",
            "some_func(arg_3)",
            "autocompletion_with_image?1"
        ]
        for ac in autocompletions:
            self.__api.add(ac)

        self.__api.prepare()

        self.__editor.setAutoCompletionSource(QsciScintilla.AcsAll)

        self.__editor.setCallTipsVisible(True)
        # self.__editor.autoCompleteFromAll()

        self.__editor.setCallTipsStyle(QsciScintilla.CallTipsContext)
        self.__editor.setCallTipsPosition(QsciScintilla.CallTipsBelowText)

        self.show()

    def some_function(self, line, index, keys):
        print("indicator clicked in line '{}', index '{}'".format(line, index))

    ''''''

    def other_function(self, line, index, keys):
        print("indicator released in line '{}', index '{}'".format(line, index))

    ''''''

    def margin_function(self, margin_nr, line_nr, state):
        print(margin_nr)
        print(line_nr)
        print(state)

    ''''''

    def __btn_action(self):
        print("Hello World!")

    ''''''



''' End Class '''

if __name__ == '__main__':
    app = QApplication(sys.argv)
    QApplication.setStyle(QStyleFactory.create('Fusion'))
    myGUI = CustomMainWindow()

    sys.exit(app.exec_())

''''''

