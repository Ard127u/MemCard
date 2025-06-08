#создай приложение для запоминания информации
from random import shuffle,randint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel,QApplication,QWidget,QRadioButton,QVBoxLayout,QHBoxLayout,QPushButton,QGroupBox,QButtonGroup

class Question():
    def __init__(self,question_text,right_answer,wrong1,wrong2,wrong3):
        self.question_text = question_text
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions = []
questions.append(Question('В какой стране разработали игру Cut the rope?','Россия','США','СССР','Индия'))
questions.append(Question('В каком году разработали игру Cut the rope?','2010','1895','2100','500 лет до н.э.'))
questions.append(Question('Как называется компания,разработавшая игру Cut the rope?','ZeptoLab','ZZZ','LeptoZab','Electronic Arts'))
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle('Memory Card')
main_window.resize(500,200)
# Панель Вопроса
question = QLabel('Самый сложный вопрос в мире')
answer_button = QPushButton('Ответить')
question_group = QGroupBox('Варианты ответов')
answer_1 = QRadioButton('Вариант 1')
answer_2 = QRadioButton('Вариант 2')
answer_3 = QRadioButton('Вариант 3')
answer_4 = QRadioButton('Вариант 4')
answers = [answer_1,answer_2,answer_3,answer_4]
RadioGroup = QButtonGroup()
RadioGroup.addButton(answer_1)
RadioGroup.addButton(answer_2)
RadioGroup.addButton(answer_3)
RadioGroup.addButton(answer_4)

h_line = QHBoxLayout()
v_line1 = QVBoxLayout()
v_line2 = QVBoxLayout()
v_line1.addWidget(answer_1)
v_line1.addWidget(answer_3)
v_line2.addWidget(answer_2)
v_line2.addWidget(answer_4)
h_line.addLayout(v_line1)
h_line.addLayout(v_line2)

question_group.setLayout(h_line)

# Панель Результата
answer_group = QGroupBox('Результат теста')
lb_result = QLabel('Правильно/Неправильно')
lb_correct = QLabel('Правильный ответ')
result_line = QVBoxLayout()
result_line.addWidget(lb_result,alignment = (Qt.AlignLeft | Qt.AlignTop))
result_line.addWidget(lb_correct,alignment = Qt.AlignHCenter,stretch = 2)
answer_group.setLayout(result_line)


# Размещение Виджетов в Окне
h_line3 = QHBoxLayout() # Вопрос
h_line4 = QHBoxLayout() # Варианты ответов / Результат теста
h_line5 = QHBoxLayout() # Кнопка ответа

h_line3.addWidget(question,alignment = (Qt.AlignHCenter | Qt.AlignVCenter))

h_line4.addWidget(question_group)
h_line4.addWidget(answer_group)
answer_group.hide()

h_line5.addStretch(1)
h_line5.addWidget(answer_button,stretch=2)
h_line5.addStretch(1)

v_line_main = QVBoxLayout()
v_line_main.addLayout(h_line3,stretch=2)
v_line_main.addLayout(h_line4,stretch=8)
v_line_main.addStretch(1)
v_line_main.addLayout(h_line5,stretch=1)
v_line_main.addStretch(1)
v_line_main.setSpacing(5)
main_window.setLayout(v_line_main)
# Функции
def show_result():
    '''Показать панель ответов'''
    question_group.hide()
    answer_group.show()
    answer_button.setText('Следующий вопрос')
def show_question():
    '''Показать панель вопросов'''
    question_group.show()
    answer_group.hide()
    answer_button.setText('Ответить')
    RadioGroup.setExclusive(False)
    answer_1.setChecked(False)
    answer_2.setChecked(False)
    answer_3.setChecked(False)
    answer_4.setChecked(False)
    RadioGroup.setExclusive(True)
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question_text)
    lb_correct.setText(q.right_answer)
    show_question()
def show_correct(res):
    lb_result.setText(res)
    show_result()
def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно')
        main_window.score += 1
        print('Статистика')
        print('-Всего вопросов:',main_window.total)
        print('-Правильных ответов:',main_window.score)
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неправильно')
def next_question():
    cur_question = randint(0,len(questions)-1)
    q = questions[cur_question]
    ask(q)
    main_window.total += 1
    print('Статистика')
    print('-Всего вопросов:',main_window.total)
    print('-Правильных ответов:',main_window.score)
def click_ok():
    if answer_button.text() == 'Ответить':
        check_answer()
    else:
        next_question()
answer_button.clicked.connect(click_ok)
main_window.score = 0
main_window.total = 0

next_question()
main_window.show()
app.exec_()