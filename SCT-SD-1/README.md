# 🌡️ Temperature Converter (Tkinter)

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-lightgrey.svg)

A simple **GUI-based Temperature Converter** built using **Python and Tkinter**.
This application allows users to easily convert temperature values between **Celsius (°C), Fahrenheit (°F), and Kelvin (K)**.

The user can enter a value in any one field, and the application automatically calculates and displays the equivalent values in the other two units.

---

## 🚀 Features

* Convert between **Celsius, Fahrenheit, and Kelvin**
* Clean and simple **Graphical User Interface**
* **Automatic conversion** based on the filled input field
* **Input validation** to prevent invalid entries
* **Clear button** to reset all values
* **Keyboard support** – press **Enter** to convert
* Rounded output values for better readability

---

## 🖥️ Preview

![temperature-converter-image](SCT-SD-1/screenshots/image.png)

---

## 🛠️ Technologies Used

* **Python**
* **Tkinter** (Python standard GUI library)

No external libraries are required.

---

## 📂 Project Structure

```
SCT-SD-1/
│
├── main.py
├── screenshots/
└── README.md
```

---

## ▶️ How to Run

1. Clone the repository

```bash
git clone https://github.com/BhaveshV23/SkillCraft-Internship-Tasks.git
```

2. Navigate to the project folder

```bash
cd SkillCraft-Internship-Tasks/SCT-SD-1
```

3. Run the program

```bash
python main.py
```

---

## 🧠 How It Works

1. The user enters a value in **any one temperature field**.
2. When the **Convert** button is clicked (or Enter is pressed):

   * The program detects which field contains a value.
   * The temperature is converted using standard formulas.
3. The calculated values automatically appear in the other fields.
4. The **Clear** button resets all input fields.

---

## 📐 Temperature Conversion Formulas

**Celsius → Fahrenheit**

```
F = (9/5) × C + 32
```

**Celsius → Kelvin**

```
K = C + 273.15
```

**Fahrenheit → Celsius**

```
C = (F − 32) × 5/9
```

**Kelvin → Celsius**

```
C = K − 273.15
```

---

## 💡 Possible Improvements

Future enhancements could include:

* Dropdown-based unit selection
* Automatic conversion while typing
* Dark mode UI
* Support for additional temperature scales

---

## 👨‍💻 Author

**Bhavesh Vadnere**

Information Technology Student

Python Developer | Aspiring AI/ML Engineer

GitHub: https://github.com/BhaveshV23

LinkedIn: https://linkedin.com/in/bhavesh-vadnere

## 📜 License

This project is open-source and available for learning and educational purposes.

---

⭐ If you found this project useful, consider giving it a **star on GitHub**!
