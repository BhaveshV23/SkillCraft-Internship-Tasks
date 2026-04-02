# 📚 Multi-Page E-Commerce Book Data Scraper (Python)

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Web Scraping](https://img.shields.io/badge/Web%20Scraping-BeautifulSoup-green.svg)
![Data Export](https://img.shields.io/badge/Data-CSV-orange.svg)
![Status](https://img.shields.io/badge/Project-Completed-success.svg)

## 📌 Project Overview

This project is a **Python-based web scraping application** that extracts structured product information from an e-commerce website and stores it in a CSV file.

The scraper collects:

* 📖 Book Title
* 💰 Price
* ⭐ Rating

from multiple pages of an online bookstore and exports the dataset in a clean structured format suitable for **data analysis, machine learning preprocessing, or reporting tasks**.

---

## 🚀 Features

✔ Multi-page web scraping support

✔ Extracts structured product information

✔ Converts rating text → numeric values

✔ Error handling implemented

✔ Clean CSV dataset generation

✔ Beginner-friendly and extensible architecture

---

## 🛠 Technologies Used

* Python
* requests
* BeautifulSoup
* pandas

---

## 📂 Project Structure

```
ecommerce-book-scraper/
│
├── main.py
├── books.csv
├── requirements.txt
└── README.md
```

---

## ⚙ Installation & Setup

### Step 1: Clone Repository

```
git clone https://github.com/BhaveshV23/SkillCraft-Internship-Tasks.git
cd SkillCraft-Internship-Tasks/SCT-SD-4
```

### Step 2: Install Dependencies

```
pip install -r requirements.txt
```

---

## ▶ How to Run the Script

Execute:

```
python main.py
```

After execution:

```
books.csv
```

will be generated automatically containing extracted product data.

---

## 📊 Sample Output

| Title                | Price  | Rating |
| -------------------- | ------ | ------ |
| A Light in the Attic | £51.77 | 3      |
| Tipping the Velvet   | £53.74 | 1      |
| Soumission           | £50.10 | 1      |

---

## 🧠 How It Works

The script follows these steps:

1. Sends HTTP request to the website
2. Parses HTML using BeautifulSoup
3. Extracts product information
4. Converts rating text into numeric format
5. Iterates across multiple catalogue pages
6. Stores extracted data into a CSV file

---

## 🌐 Data Source

Scraped from:

https://books.toscrape.com

This website is designed specifically for practicing web scraping safely and ethically.

---

## 📈 Future Improvements

Possible enhancements:

* Scrape all available pages automatically
* Export dataset as Excel file
* Add command-line arguments for page selection
* Store data inside a database (SQLite / MySQL)
* Build visualization dashboard using matplotlib or Power BI

---

## 🎯 Learning Outcomes

Through this project:

* Learned HTML parsing using BeautifulSoup
* Practiced multi-page web scraping
* Converted unstructured data → structured dataset
* Exported results into CSV format
* Implemented error handling in scraping workflow

---

## 👨‍💻 Author

**Bhavesh Vadnere**

Information Technology Student
Python Developer | Aspiring AI/ML Engineer

GitHub: https://github.com/BhaveshV23

LinkedIn: https://linkedin.com/in/bhavesh-vadnere

---

## ⭐ Support

If you found this project useful:

Give it a ⭐ on GitHub!
