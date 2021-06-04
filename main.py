import sys
from UI import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication, QLineEdit, QTableWidget, QHeaderView, QTableWidgetItem
import matrixcalculate as m


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.pressed.connect(self.add_matrix)
        self.ui.pushButton_4.pressed.connect(lambda: self.generate_line_edit(self.ui.lineEdit.text(), self.ui.lineEdit_2.text(), 1))
        self.ui.pushButton_5.pressed.connect(lambda: self.generate_line_edit(self.ui.lineEdit_3.text(), self.ui.lineEdit_4.text(), 2))

        self.show()

    def generate_line_edit(self, row, column, number):
        row = int(row)
        column = int(column)
        if number == 1:
            self.matrix_input1 = QTableWidget(row, column)
            self.matrix_input1.resizeRowsToContents()
            self.matrix_input1.resizeColumnsToContents()
            self.ui.gridLayout.addWidget(self.matrix_input1, 0, 0)
        elif number == 2:
            self.matrix_input2 = QTableWidget(row, column)
            self.matrix_input2.resizeRowsToContents()
            self.matrix_input2.resizeColumnsToContents()
            self.ui.gridLayout_2.addWidget(self.matrix_input2, 0, 0)

        #self.table1.setItem(row, col, item)
        #self.table1.item(row, col).text()

    def add_matrix(self):
        matrix1 = []
        matrix2 = []
        for row in range(self.matrix_input1.rowCount()):
            matrix1.append([])
            for column in range(self.matrix_input1.columnCount()):
                matrix1[row].append(int(self.matrix_input1.item(row, column).text()))

        for row in range(self.matrix_input2.rowCount()):
            matrix2.append([])
            for column in range(self.matrix_input2.columnCount()):
                matrix2[row].append(int(self.matrix_input2.item(row, column).text()))
        m1 = m.MatrixCalculate(matrix1)
        m2 = m.MatrixCalculate(matrix2)
        m3 = m1 + m2
        self.set_value_table(m3)

    def set_value_table(self, matrix):
        matrix3 = matrix
        row = len(matrix3)
        column = len(matrix3[0])
        self.matrix_output = QTableWidget(row, column)
        self.matrix_output.resizeRowsToContents()
        self.matrix_output.resizeColumnsToContents()
        self.ui.gridLayout_3.addWidget(self.matrix_output, 0, 0)
        print(matrix3)

        for i in range(row):
            for j in range(column):
                self.matrix_output.setItem(i, j, QTableWidgetItem(str(matrix3[i][j])))




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    sys.exit(app.exec_())
