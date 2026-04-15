# Cardamom spice price analysis & prediction

> End-to-end web scraping, data mining, and visualization of cardamom market data
> to help agricultural analysts track price trends and predict future yields.

---

## 🧩 Problem it solves

Cardamom prices fluctuate heavily based on season, geography, and demand — but
this data is scattered across dozens of web pages with no central dashboard.
This project automates the collection of 100+ pages of real market data and
turns it into actionable insights: price trends, quantity patterns, and
future price predictions — all in one place.

---

## 🛠️ Technologies used

| Tool | Purpose |
|---|---|
| Python | Core language |
| Selenium | Automated web scraping across 100+ pages |
| Pandas | Data cleaning and transformation |
| Matplotlib / NumPy | Trend charts and statistical analysis |
| File handling | Exporting reports as CSV/Excel |

---

## ⚙️ Installation & setup

**1. Clone the repo**
```bash
git clone https://github.com/I-am-keerthana/Cardomom-analysis-python.git
cd Cardomom-analysis-python
```

**2. Install dependencies**
```bash
pip install selenium pandas matplotlib numpy
```

**3. Set up ChromeDriver**
Download [ChromeDriver](https://chromedriver.chromium.org/downloads) matching
your Chrome version and add it to your PATH.

**4. Run the script**
```bash
python cardamom_code_git.py
```

---

## 📊 Key findings

- Cardamom prices show a strong **seasonal peak** between October–December
- Price and quantity have an **inverse relationship** — high supply months
  consistently show lower unit prices
- The data reveals a **year-on-year upward price trend**, suggesting growing
  export demand
- Interactive charts allow analysts to filter by date range and market region

---

## 📁 Output

- Exportable CSV reports with price, quantity, and date
- Interactive dashboards with trend lines
- Price prediction chart for upcoming seasons

---

## 📌 Notes

> This scraper targets publicly available agricultural market data.
> Run responsibly — add delays between requests to avoid overloading the server.
