from PyQt5 import QtWidgets, uic
import sys
from lab3.Book import Book
import pickle as p


class UI(QtWidgets.QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi('lab5_m.ui', self)

        self.handler = Handler(self)
        self.init_tool_bar()

        self.btnClear = self.findChild(QtWidgets.QPushButton, 'btnClear')
        self.btnAdd = self.findChild(QtWidgets.QPushButton, 'btnAdd')
        self.btnDelete = self.findChild(QtWidgets.QPushButton, 'btnDelete')
        self.btnMessage = self.findChild(QtWidgets.QPushButton, 'btnMessage')
        self.btnSearch = self.findChild(QtWidgets.QPushButton, 'btnSearch')

        self.leName = self.findChild(QtWidgets.QLineEdit, 'leName')
        self.leIsbn = self.findChild(QtWidgets.QLineEdit, 'leIsbn')
        self.leAuthors = self.findChild(QtWidgets.QLineEdit, 'leAuthors')
        self.lePublisher = self.findChild(QtWidgets.QLineEdit, 'lePublisher')
        self.leSearch = self.findChild(QtWidgets.QLineEdit, 'leSearch')

        self.sbNPages = self.findChild(QtWidgets.QSpinBox, 'sbNPages')
        self.sbPrice = self.findChild(QtWidgets.QDoubleSpinBox, 'sbPrice')
        self.sbPublicationYear = self.findChild(QtWidgets.QSpinBox, 'sbPublicationYear')
        
        self.cbMessageType = self.findChild(QtWidgets.QComboBox, 'cbMessageType')
        
        self.cbWithIcon = self.findChild(QtWidgets.QCheckBox, 'cbWithIcon')
        
        self.twBooks = self.findChild(QtWidgets.QTableView, 'twBooks')
        self.twBooks.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        
        self.btnAdd.clicked.connect(self.btn_add_clicked)
        self.btnClear.clicked.connect(self.btn_clear_clicked)
        self.btnDelete.clicked.connect(self.btn_delete_clicked)
        self.btnMessage.clicked.connect(self.btn_message_clicked)

        self.show()

    def init_tool_bar(self):
        open_act = QtWidgets.QAction('Открыть', self)
        open_act.triggered.connect(self.handler.read_books_file)

        exit_act = QtWidgets.QAction('Выйти', self)
        exit_act.triggered.connect(self.close)

        save_act = QtWidgets.QAction('Сохранить', self)
        save_act.triggered.connect(self.handler.write_books_file)

        save_as_act = QtWidgets.QAction('Сохранить как...', self)
        # save_as_act.triggered.connect()

        self.statusBar()

        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu('Файл')

        file_menu.addAction(open_act)
        file_menu.addAction(save_act)
        file_menu.addAction(exit_act)

        self.setWindowTitle('Toolbar')
        
    def btn_delete_clicked(self, event):
        if len(self.twBooks.selectedIndexes()) <= 0:
            return

        index = [idx.row() for idx in self.twBooks.selectionModel().selectedRows()][0]
        book_name = self.handler.book_list[index].name
        self.handler.remove_book(book_name)
        self.repaint_table()

    def repaint_table(self):
        self.twBooks.setRowCount(0)
        self.twBooks.setColumnCount(7)

        for book in self.handler.book_list:
            row_pos = self.twBooks.rowCount()
            self.twBooks.insertRow(row_pos)
            self.twBooks.setItem(row_pos, 0, QtWidgets.QTableWidgetItem(book.name))
            self.twBooks.setItem(row_pos, 1, QtWidgets.QTableWidgetItem(str(book.publication_year)))
            self.twBooks.setItem(row_pos, 2, QtWidgets.QTableWidgetItem(str(book.n_pages)))
            self.twBooks.setItem(row_pos, 3, QtWidgets.QTableWidgetItem(book.isbn))
            self.twBooks.setItem(row_pos, 4, QtWidgets.QTableWidgetItem(','.join(book.authors)))
            self.twBooks.setItem(row_pos, 5, QtWidgets.QTableWidgetItem(book.publisher))
            self.twBooks.setItem(row_pos, 6, QtWidgets.QTableWidgetItem(str(book.price)))

    def btn_message_clicked(self, event):
        message_type = str(self.cbMessageType.currentText())

        is_sad = message_type == 'Грустное сообщение'
        if is_sad:
            message_str = ':('
        else:
            message_str = ':)'

        message = QtWidgets.QMessageBox()
        message.setText(message_str)
        message.setWindowTitle('Сообщение')

        if self.cbWithIcon.isChecked() and is_sad:
            message.setIcon(QtWidgets.QMessageBox.Critical)
        elif self.cbWithIcon.isChecked() and not is_sad:
            message.setIcon(QtWidgets.QMessageBox.Information)

        message.exec()

    def btn_add_clicked(self, event):
        name = self.leName.text()
        pub_year = self.sbPublicationYear.value()
        n_pages = self.sbNPages.value()

        if len(name) <= 0 or n_pages <= 0:
            message = QtWidgets.QMessageBox()
            message.setText('Недостаточно данных о книге. Нужны: название, год издания, кол-во страниц')
            message.setIcon(QtWidgets.QMessageBox.Critical)
            message.setWindowTitle('Книга не добавлена')
            message.exec()

            return

        for book in self.handler.book_list:
            if book.name == name:
                message = QtWidgets.QMessageBox()
                message.setText('Такая книга уже есть')
                message.setIcon(QtWidgets.QMessageBox.Critical)
                message.setWindowTitle('Книга не добавлена')
                message.exec()

                return

        isbn = self.leIsbn.text()
        authors = self.leAuthors.text().replace(' ', '').split(',')
        publisher = self.lePublisher.text()
        price = self.sbPrice.value()
        self.handler.add_book(name, pub_year, n_pages, isbn, authors, publisher, price)
        self.repaint_table()

    def btn_clear_clicked(self, event):
        self.leName.setText('')
        self.lePublisher.setText('')
        self.leAuthors.setText('')
        self.leIsbn.setText('')
        self.sbPublicationYear.setValue(0)
        self.sbPrice.setValue(0)
        self.sbNPages.setValue(0)


class Handler:
    def __init__(self, ui):
        self.window = ui
        self.book_list = []

    def read_books_file(self):
        path = QtWidgets.QFileDialog.getOpenFileName(self.window, 'Выберите файл')[0]
        if len(path) == 0:
            return

        with open(path, 'rb') as f:
            try:
                self.book_list = p.load(f)
            except EOFError:
                self.book_list = []

    def write_books_file(self):
        path = QtWidgets.QFileDialog.getOpenFileName(self.window, 'Выберите файл')[0]

        if len(path) == 0:
            return

        with open(path, 'wb') as f:
            p.dump(self.book_list, f)

    def add_book(self,
                 name,
                 publication_year,
                 n_pages,
                 isbn=None, authors=None, publisher=None, price=None):

        book = Book(name, publication_year, n_pages, isbn, authors, publisher, price)
        self.book_list.append(book)
        self.write_books_file()

    def remove_book(self, book_name):
        index = -1
        for i, book in enumerate(self.book_list):
            if book.name == book_name:
                index = i
                break

        if index < 0:
            return

        self.book_list.pop(index)
        self.write_books_file()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = UI()
    app.exec()

# read_books_file()
# repaint_table()

