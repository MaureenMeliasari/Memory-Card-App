from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QHBoxLayout,
    QVBoxLayout, QGroupBox, QRadioButton,
    QPushButton, QLabel, QButtonGroup
)
from random import randint

class Question():
    def __init__ (self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = []
questions_list.append(Question('Buah apa yang tumbuh di pohon apel?', 'apel', 'pir', 'semangka', 'durian'))
questions_list.append(Question('Apa yang kita pelajari di algorithmics?', 'python', 'menggambar', 'membaca', 'css'))
questions_list.append(Question('Tahun berapa Indonesia merdeka', '1945', '1999', '1875', '2002'))


app = QApplication([])
window = QWidget()
window.setWindowTitle('Memory Card')
window.resize(300, 300)

question = QLabel('Tahun berapa Indonesia Merdeka?')
result = QLabel('True/False')
label_correct = QLabel('The answer will be here') 

RadioGroupBox = QGroupBox('Answer Option')
AnswerGroupBox = QGroupBox('Test result')

btn_answer1 = QRadioButton('1999')
btn_answer2 = QRadioButton('1945')
btn_answer3 = QRadioButton('1993')
btn_answer4 = QRadioButton('1931')

btn_answer = QPushButton('Answer')

radioGroup = QButtonGroup()
radioGroup.addButton(btn_answer1)
radioGroup.addButton(btn_answer2)
radioGroup.addButton(btn_answer3)
radioGroup.addButton(btn_answer4)

#question group box
layout_answer1 = QHBoxLayout()
layout_answer2 = QVBoxLayout()
layout_answer3 = QVBoxLayout()

layout_answer2.addWidget(btn_answer1)
layout_answer2.addWidget(btn_answer2)

layout_answer3.addWidget(btn_answer3)
layout_answer3.addWidget(btn_answer4)

layout_answer1.addLayout(layout_answer2)
layout_answer1.addLayout(layout_answer3)
RadioGroupBox.setLayout(layout_answer1)

#answer group box
layout_groupanswer = QVBoxLayout()
layout_groupanswer.addWidget(result, alignment= (Qt.AlignLeft | Qt.AlignTop))
layout_groupanswer.addWidget(label_correct, alignment= Qt.AlignCenter)
AnswerGroupBox.setLayout(layout_groupanswer)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(question, alignment = Qt.AlignCenter)

layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnswerGroupBox)
AnswerGroupBox.hide()


layout_line3.addStretch(1)
layout_line3.addWidget(btn_answer, stretch=2)
layout_line3.addStretch(1)

main_layout = QVBoxLayout()
main_layout.addLayout(layout_line1, stretch=2)
main_layout.addLayout(layout_line2, stretch=8)
main_layout.addStretch(1)
main_layout.addLayout(layout_line3, stretch=1)
main_layout.addStretch(1)

def show_result():
    RadioGroupBox.hide()
    AnswerGroupBox.show()
    btn_answer.setText('Next Question')

def show_question():
    AnswerGroupBox.hide()
    RadioGroupBox.show()
    btn_answer.setText('Answer')
    radioGroup.setExclusive(False)
    btn_answer1.setChecked(False)
    btn_answer2.setChecked(False)
    btn_answer3.setChecked(False)
    btn_answer4.setChecked(False)
    radioGroup.setExclusive(True)

answers = [btn_answer1, btn_answer2, btn_answer3, btn_answer4]

from random import shuffle

def ask(q : Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question)
    label_correct.setText(q.right_answer)
    show_question()

def show_correct(respon):
    result.setText(respon)
    show_result()

def check_answer():
    if answers[0].isChecked():
        show_correct('Correct!')
        window.score += 1
        print('Statistic')
        print('Total Score:', window.score)
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Incorrect!')

current_index = -1
def next_question():
    window.total += 1
    global current_index
    current_index += 1
    if current_index < len(questions_list):
        q = questions_list[current_index]
        ask(q)
        print('Total Question:', window.total)
    else:
        question.setText('🚀Kuis Selesai')
        RadioGroupBox.hide()
        AnswerGroupBox.hide()
        btn_answer.hide()

def click_ok():
    if btn_answer.text() == 'Answer':
        check_answer()
    else:
        next_question()

shuffle(questions_list)
window.total = 0
window.score = 0
next_question()
btn_answer.clicked.connect(click_ok)

window.setLayout(main_layout)
window.show()
app.exec_()