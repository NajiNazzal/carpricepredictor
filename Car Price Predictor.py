import sys
import os
import sklearn
import pandas as pd
import pickle
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QCompleter, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtGui import QPixmap, QFont, QIntValidator, QIcon
from PyQt5.QtCore import Qt
import joblib

class SimpleFrame(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setWindowTitle('Car Price Predictor')
        self.setGeometry(100, 100, 1200, 604)

        # Create a QLabel to serve as the background
        background_label = QLabel(self)
        background_pixmap = QPixmap(image_path)
        background_label.setPixmap(background_pixmap)
        background_label.setScaledContents(True)
        background_label.setGeometry(0, 0, self.width(), self.height())
        manufacturerOptions = ['Lexus', 'Chevrolet', 'Honda', 'Ford', 'Hyundai', 'Toyota', 'Mercedes-Benz', 'Opel', 'Porsche', 'BMW', 'Jeep', 'Volkswagen', 'Audi', 'Renault', 'Nissan', 'Daewoo', 'Kia', 'Mitsubishi', 'SsangYong', 'Mazda', 'GMC', 'Fiat', 'Subaru', 'Infiniti', 'Alfa Romeo', 'Suzuki', 'Lincoln', 'VAZ', 'GAZ', 'Citroen', 'Land Rover', 'Mini', 'Dodge', 'Chrysler', 'Jaguar', 'Isuzu', 'Acura', 'Skoda', 'Daihatsu', 'Buick', 'Tesla', 'Cadillac', 'Peugeot', 'Bentley', 'Volvo', 'Haval', 'Hummer', 'Scion', 'Mercury', 'ZAZ', 'Rover', 'UAZ', 'Seat', 'Lancia', 'Ferrari', 'Maserati', 'Saab', 'Lamborghini', 'Pontiac', 'Saturn', 'Aston Martin', 'Moskvich', 'GreatWall']
        manufacturer_box = self.createComboBox(manufacturerOptions)
        manufacturer_box.setGeometry(51, 100, 200, 30)
        model_box = self.createSimpleBox()
        model_box.setGeometry(51, 167, 200, 30)
        categoryOptions = ['Jeep', 'Hatchback', 'Sedan', 'Microbus', 'Goods wagon', 'Universal', 'Coupe', 'Minivan', 'Cabriolet', 'Limousine', 'Pickup']
        category_box = self.createOptionBox(categoryOptions)
        category_box.setGeometry(51, 239, 200, 30)
        year_box = self.createNumberBox()
        year_box.setGeometry(51, 302, 200, 30)
        leather_box = self.createOptionBox(['Yes', 'No'])
        leather_box.setGeometry(51, 367, 200, 30)
        mileage_box = self.createNumberBox()
        mileage_box.setGeometry(51, 437, 200, 30)
        levy_box = self.createNumberBox()
        levy_box.setGeometry(51, 503, 200, 30)
        engineOptions = ['3.5', '3', '1.3', '2.5', '2', '1.8', '4', '1.6', '2.0 Turbo', '2.2 Turbo', '3.3', '4.4', '3.0 Turbo', '2.4', '1.4 Turbo', '1.5', '2.3', '1.5 Turbo', '1.6 Turbo', '2.2', '2.3 Turbo', '4.7', '1.4', '5.5', '2.8 Turbo', '3.2', '3.8', '4.6', '1.2', '5', '1.7', '2.9', '0.5', '1.8 Turbo', '2.4 Turbo', '3.5 Turbo', '1.9', '2.7', '3.6', '4.8', '5.3', '2.8', '3.2 Turbo', '1.1', '2.1', '0.7', '5.4', '1.3 Turbo', '3.7', '1', '2.5 Turbo', '2.6', '1.9 Turbo', '4.4 Turbo', '4.7 Turbo', '0.8', '0.2 Turbo', '5.7', '4.8 Turbo', '4.6 Turbo', '6.7', '6.2', '1.2 Turbo', '3.4', '1.7 Turbo', '6.3 Turbo', '2.7 Turbo', '0.4', '4.3', '4.2', '2.9 Turbo', '0', '4.0 Turbo', '20', '3.6 Turbo', '0.3', '3.7 Turbo', '5.9', '5.5 Turbo', '0.2', '2.1 Turbo', '5.6', '6', '0.7 Turbo', '0.6 Turbo', '6.8', '4.5', '0.6', '7.3', '0.1', '1.0 Turbo', '6.3', '4.5 Turbo', '0.8 Turbo', '4.2 Turbo', '3.1', '5.0 Turbo', '6.4', '5.7 Turbo', '0.9', '3.9', '0.4 Turbo', '5.4 Turbo', '0.3 Turbo', '5.2', '5.8', '1.1 Turbo']
        engine_box = self.createComboBox(engineOptions)
        engine_box.setGeometry(958, 105, 200, 30)
        drivetrainOptions = ['Front', 'Rear', '4x4']
        drivetrain_box = self.createOptionBox(drivetrainOptions)
        drivetrain_box.setGeometry(958, 167, 200, 30)
        cylindersOptions = ['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10', 'V11', 'V12', 'V13', 'V14', 'V15', 'V16']
        cylinders_box = self.createOptionBox(cylindersOptions)
        cylinders_box.setGeometry(958, 239, 200, 30)
        gearboxOptions = ['Automatic', 'Manual', 'Tiptronic', 'Variator']
        gearbox_box = self.createOptionBox(gearboxOptions)
        gearbox_box.setGeometry(958, 302, 200, 30)
        fuelOptions = ['Petrol', 'Diesel', 'Hybrid', 'Plug-in Hybrid', 'CNG', 'LPG', 'Hydrogen']
        fuel_box = self.createOptionBox(fuelOptions)
        fuel_box.setGeometry(958, 367, 200, 30)
        airbags_box = self.createNumberBox()
        airbags_box.setGeometry(958, 437, 200, 30)
        doors_box = self.createOptionBox(['2', '4', '>5'])
        doors_box.setGeometry(958, 503, 200, 30)
        

        button = QPushButton(self)
        button.setText("          ")
        button.setGeometry(536, 468, 152, 45)
        button.setStyleSheet("background-color: transparent; color: #FFFFFF; border: none;")
        button.setFlat(True)
        button.setStyleSheet(
        """
        QPushButton {
            background-color: transparent;
            color: #FFFFFF;
            border: none;
        }
        QPushButton:pressed {
            background-color: rgba(234, 79, 240, 40);
            color: #FFFFFF;
        }
        QPushButton:released {
            background-color: transparent;
            color: #FFFFFF;
        }
        """)
        predictionText = QLabel(self)
        predictionText.setGeometry(105, 532, 1000, 44)

        # Set the font properties
        predictionTextFont = QFont("Calibri", 25)
        predictionTextFont.setBold(False)
        predictionText.setFont(predictionTextFont)
        # Set the alignment to center horizontally and vertically
        predictionText.setAlignment(Qt.AlignCenter)
        # Set the stylesheet for the QLabel widget to make it transparent
        predictionText.setStyleSheet("background-color: transparent; color: #ffffff")
        def button_pressed():
            manufacturer_text = manufacturer_box.currentText().upper()
            model_text = model_box.text().upper()
            category_text = category_box.currentText().upper()
            year_text = year_box.text()
            leather_text = leather_box.currentText().upper()
            mileage_text = mileage_box.text()
            levy_text = levy_box.text()
            engine_text = engine_box.currentText().upper()
            drivetrain_text = drivetrain_box.currentText().upper()
            cylinders_text = cylinders_box.currentText()
            gearbox_text = gearbox_box.currentText().upper()
            fuel_text = fuel_box.currentText().upper()
            airbags_text = airbags_box.text()
            doors_text = doors_box.currentText().upper()
            if any(value == '' for value in [model_text, year_text, mileage_text, engine_text, drivetrain_text]):
                QMessageBox.critical(self, 'Error', 'Please fill in all the fields.')
                return
            cylinders = process_cylinders(cylinders_text)
            inputData = {
                'Levy': levy_text,
                'Manufacturer': manufacturer_text,
                'Model': model_text,
                'Prod. year': year_text,
                'Category': category_text,
                'Leather interior': leather_text,
                'Fuel type': fuel_text,
                'Engine volume': engine_text,
                'Mileage': mileage_text,
                'Cylinders': cylinders,
                'Gear box type': gearbox_text,
                'Drive wheels': drivetrain_text,
                'Doors': doors_text,
                'Airbags': airbags_text
            }
            data = pd.DataFrame([inputData])
            int64_columns = ['Levy', 'Prod. year', 'Mileage', 'Cylinders', 'Airbags']
            data[int64_columns] = data[int64_columns].astype('int64')
            categoricalColumns = data.select_dtypes(include=['object']).columns.tolist()
            encodedData = encoder.transform(data[categoricalColumns])
            data[categoricalColumns] = encodedData.astype(int)
            price = loaded_model.predict(data)
            price_scalar = price.item()
            displayPrice = "{:,.0f}".format(price_scalar)
            predictionText.setText("$" + displayPrice)
        def button_released():
            pass
        def process_cylinders(selected_text):
            # Custom function to process the selected text
            if selected_text == 'Electric (0)':
                return 0
            else:
                # Remove 'V' from the selected text and convert to integer
                return selected_text.replace('V', '')
        button.pressed.connect(button_pressed)
        button.released.connect(button_released)

        self.setFixedSize(self.width(), self.height())
        self.show()



    def createComboBox(self, options):
        # Create a QComboBox with QLineEdit as the editable field
        combo_box = QComboBox(self)
        combo_box.setEditable(True)
        combo_box.setStyleSheet("color: white; background: transparent; selection-background-color: orange; border: 1px solid green;")

        # Set font for the combo box
        font = QFont()
        font.setPointSize(14)
        combo_box.setFont(font)

        # Add multiple options to the combo box
        combo_box.addItems(options)

        # Set the font and size for the text being entered or selected
        combo_box.lineEdit().setFont(font)

        # Enable auto-completion and set completion mode
        completer = QCompleter(options, combo_box)
        completer.setCaseSensitivity(Qt.CaseInsensitive)

        # Style the QListView within the QCompleter
        completer_popup = completer.popup()
        completer_popup.setStyleSheet("color: white; background: transparent; border: 1px solid green;")

        combo_box.setCompleter(completer)
        combo_box.lineEdit().setCompleter(completer)
        # Set the current index to -1 (empty)
        combo_box.setCurrentIndex(-1)

        return combo_box
    def createOptionBox(self, options):
        # Create a QComboBox with QLineEdit as the editable field
        combo_box = QComboBox(self)
        combo_box.setEditable(False)
        combo_box.setStyleSheet("color: white; background: transparent; selection-background-color: orange; border: 1px solid green;")
        # Set font for the combo box
        font = QFont()
        font.setPointSize(14)
        combo_box.setFont(font)
        # Add multiple options to the combo box
        combo_box.addItems(options)
        # Set the current index to -1 (empty)
        combo_box.setCurrentIndex(-1)

        return combo_box
    def createSimpleBox(self):
        # Create a simple QLineEdit
        simple_box = QLineEdit(self)
        simple_box.setStyleSheet("color: white; background: transparent; border: 1px solid green;")
        # Set font for the simple box
        font = QFont()
        font.setPointSize(14)
        simple_box.setFont(font)
        return simple_box
    def createNumberBox(self):
        # Create a simple QLineEdit
        simple_box = QLineEdit(self)
        simple_box.setStyleSheet("color: white; background: transparent; border: 1px solid green;")
        # Set font for the simple box
        font = QFont()
        font.setPointSize(14)
        simple_box.setFont(font)
        simple_box.setValidator(QIntValidator())
        return simple_box

if __name__ == '__main__':
    app = QApplication(sys.argv)
    base_dir = getattr(sys, '_MEIPASS', os.path.abspath(os.path.dirname(__file__)))
    image_path = os.path.join(base_dir, 'images', 'wallpaper3.jpg')
    model = os.path.join(base_dir, 'RF_Model.joblib')
    loaded_model = joblib.load(model)
    encoder_path = os.path.join(base_dir, 'encoder.pkl')
    with open(encoder_path, 'rb') as encoder_file:
        encoder = pickle.load(encoder_file)
    icon_path = os.path.join(base_dir, 'icon.ico')
    app.setWindowIcon(QIcon(icon_path))
    main_window = SimpleFrame()
    sys.exit(app.exec_())
