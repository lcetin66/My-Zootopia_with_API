# 🐾 Zootopia with API

![Python](https://img.shields.io/badge/Python-3.11%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Completed-success)
![Masterschool](https://img.shields.io/badge/Masterschool-Bootcamp-orange)
![Platform](https://img.shields.io/badge/Platform-Terminal%20%2B%20HTML-lightgrey)

A dynamic web page generator that fetches detailed animal data from an external API (API Ninjas) and presents it in a beautifully styled card-based repository.

---

## 🌟 Features

- **Real-time Data Fetching**: Retrieves up-to-date animal characteristics using API Ninjas.
- **Dynamic HTML Generation**: Automatically builds a responsive, glassmorphism-inspired animal repository.
- **Robust Error Handling**: Includes validation for API timeouts, missing data, and invalid inputs.
- **Environment Security**: Uses `.env` and `python-dotenv` to keep sensitive API keys secure.
- **Modern UI**: Clean, card-based layout with responsive design and modern font smoothing.

---

## 📂 Project Structure

```text
.
├── animals.html                # Generated final web page
├── animals_template.html       # HTML/CSS template for the generator
├── animals_web_generator.py    # Main orchestration script
├── data_fetcher.py             # API communication module
├── requirements.txt            # Project dependencies
├── animals_data.json           # Local backup/reference data
└── .gitignore                  # Git exclusion rules
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.11 or higher installed on your system.
- An API Key from [API Ninjas](https://api-ninjas.com/api/animals).

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/lcetin66/My-Zootopia_with_API.git
   cd My-Zootopia_with_API
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment:**
   Create a `.env` file in the root directory and add your API key:
   ```text
   API_KEY=your_actual_api_key_here
   ```

---

## 🛠 Usage

Run the generator from your terminal:

```bash
python animals_web_generator.py
```

Follow the prompt to enter an animal name (e.g., *Fox*, *Lemur*, *Tiger*). The script will fetch the data and update `animals.html` instantly. Launch `animals.html` in your browser to see the results!

---

## 📜 License

Distributed under the **MIT License**. See `LICENSE` for more information.

---

### 👨‍💻 Developed by
**lcetin66** (Masterschool Bootcamp Student)
