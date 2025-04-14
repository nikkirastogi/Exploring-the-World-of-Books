
# 📚 Exploring the World of Books

**Author:**  
- **Nikki Rastogi** – [LinkedIn](https://www.linkedin.com/in/nikkirastogi/)

---

## 🧠 Abstract

This project explores the nuanced relationship between an author’s **prolificacy** (number of books written) and the **average ratings** of their works. Our findings reveal that a high book count does not guarantee high ratings — while some authors maintain consistent quality, others show varied patterns. The study underscores the idea that **quality, not quantity**, shapes literary impact.

Through data analysis, visualizations, and web scraping, we provide actionable insights for readers, publishers, and authors about trends in the literary world.

---

## 📌 Introduction

This is a data-driven exploration into the **book ecosystem**, combining structured data and scraped reviews to:

- Analyze trends in book ratings
- Compare author productivity to perceived quality
- Visualize publisher dominance and rating distributions
- Scrape Amazon for live book data

---

## 📦 Dataset Overview

The project uses two main CSV datasets:

- `BX-Books.csv` – Book details (title, author, year, publisher)
- `BX-Book-Ratings.csv` – User ratings

```python
import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/nikkirastogi/Exploring-the-World-of-Books/main/src/data/BX-Books.csv", 
                 delimiter=";", encoding="latin1", on_bad_lines='skip')

ratings_df = pd.read_csv("https://raw.githubusercontent.com/nikkirastogi/Exploring-the-World-of-Books/main/src/data/BX-Book-Ratings.csv", 
                         delimiter=";", encoding="latin1", on_bad_lines='skip')
```

---

## 🔧 Modules Overview

| Module | Purpose |
|--------|---------|
| `cleaning.books_cleaning.py` | Preprocessing and merging book & rating data |
| `summary.books_summary.py`   | Dataset summary, shape, nulls, and statistics |
| `eda.books_eda.py`           | Visualizations: top authors, publishers, rating distributions |
| `inference.books_inference.py` | Analysis of correlations between authorship and ratings |
| `scraping.books_scraper.py` | Web scraping Amazon for book review metadata |
| `surprise.book_surprise.py` | Generating recommendation-based insight |

---

## 📊 Features

- 📈 **Top Publishers/Authors**: Bar plots for most prolific contributors
- 🧩 **Ratings Distribution**: Histograms of user ratings
- ☁️ **Word Clouds**: Visual summary of frequent titles
- 🔬 **Author-Rating Correlation**: Explore trends across prolific authors
- 🌐 **Amazon Scraper**: Pull book title, rating, and review count live
- 📈 **Publication Year Analysis**: Study reader preferences over time

---

## 🔎 Web Scraping Example

```python
from src.scraping.books_scraper import BooksScraper

book_list = ["The Big Book of American Trivia", "Hamlet (Wordsworth Classics)"]
scraper = BooksScraper("https://www.amazon.com")
book_data = scraper.scrape_books(book_list)
```

---

## 📌 Inference Highlights

**Main Question:**  
> Is there a correlation between how many books an author writes and how well they’re rated?

🧠 Observations:
- No strong correlation between prolificacy and rating.
- Some prolific authors maintain high standards.
- Ratings fluctuate independently of volume for many.

---

## 📁 Project Structure

```
Exploring-the-World-of-Books/
├── src/
│   ├── cleaning/
│   ├── summary/
│   ├── eda/
│   ├── inference/
│   ├── scraping/
│   ├── surprise/
│   └── data/
├── BusinessProblem/
├── books_and_reviews.ipynb
├── LICENSE
├── README.md
├── pyproject.toml
└── updated_dataset.csv
```

---

## 🚀 How to Run Locally

```bash
git clone https://github.com/nikkirastogi/Exploring-the-World-of-Books.git
cd Exploring-the-World-of-Books
pip install -e .
```

---

## 📚 Conclusion

This project emphasizes that **prolific writing doesn't guarantee critical success**, and offers tools to help readers, publishers, and authors analyze literary trends with data.

---
