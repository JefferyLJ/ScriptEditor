from PyQt5.Qsci import QsciLexerCustom
from PyQt5.QtGui import QColor, QFont
import re


class Lexer(QsciLexerCustom):
    def __init__(self, parent):
        super(Lexer, self).__init__(parent)
        # Default text settings
        # ----------------------
        self.setDefaultColor(QColor("#ff000000"))
        self.setDefaultPaper(QColor("#ffffffff"))
        self.setDefaultFont(QFont("Consolas", 14))

        # Initialize colors per style
        # ----------------------------
        self.setColor(QColor("#ff000000"), 0)  # Style 0: black
        self.setColor(QColor("#ff7f0000"), 1)  # Style 1: red
        self.setColor(QColor("#ff0000bf"), 2)  # Style 2: blue

        # Initialize paper colors per style
        # ----------------------------------
        self.setPaper(QColor("#ffffffff"), 0)  # Style 0: white
        self.setPaper(QColor("#ffffffff"), 1)  # Style 1: white
        self.setPaper(QColor("#ffffffff"), 2)  # Style 2: white

        # Initialize fonts per style
        # ---------------------------
        self.setFont(QFont("Consolas", 14, weight=QFont.Bold), 0)  # Style 0: 14pt bold
        self.setFont(QFont("Consolas", 14, weight=QFont.Bold), 1)  # Style 1: 14pt bold
        self.setFont(QFont("Consolas", 14, weight=QFont.Bold), 2)  # Style 2: 14pt bold

        editor = self.parent()
        editor.SendScintilla(editor.SCI_STYLESETHOTSPOT, 1, True)
        editor.setHotspotUnderline(True)
        editor.SCN_HOTSPOTCLICK.connect(self.hotsport)
        # editor.setHotspotForegroundColor(QColor("# ffcf4444"))
        # editor.setHotspotBackgroundColor(QColor("# ffaaaaaa"))
        # editor.SendScintilla(editor.SCI_SETHOTSPOTACTIVEBACK, True, 0xaaaaaa)

    def hotsport(self, position, modifier):
        print(position)
        print(modifier)

    def language(self):
        [...]

    def description(self, style):
        if style == 0:
            return "myStyle_0"
        elif style == 1:
            return "myStyle_1"
        elif style == 2:
            return "myStyle_2"
            ###
        return ""

    def styleText(self, start, end):
        # 1. Initialize the styling procedure
        # ------------------------------------
        self.startStyling(start)

        # 2. Slice out a part from the text
        # ----------------------------------
        text = self.parent().text()[start:end]

        # 3. Tokenize the text
        # ---------------------
        p = re.compile(r"\s+|\w+|\W")
        token_list = [(token, len(bytearray(token, "utf-8"))) for token in p.findall(text)]
        # -> 'token_list' is a list of tuples: (token_name, token_len)

        # 4. Style the text in a loop
        # ----------------------------
        # self.setStyling(number_of_chars, style_nr)
        #
        for i, token in enumerate(token_list):
            if token[0] in ["for", "while", "return", "int", "include"]:
                # Red style
                self.setStyling(token[1], 1)

            elif token[0] in ["(", ")", "{", "}", "[", "]", "#"]:
                # Blue style
                self.setStyling(token[1], 2)

            else:
                # Default style
                self.setStyling(token[1], 0)
            ###
        ###