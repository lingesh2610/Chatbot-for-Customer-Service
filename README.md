# 🤖 Customer Service NLP Chatbot – "Nova"

## 🚀 Project Overview

This project was developed as part of a 1-month online internship to demonstrate the real-world application of **Natural Language Processing (NLP)**.

The **"Nova" Chatbot** is designed to assist customers of a fictional electronics store, **TechNova**, by answering Frequently Asked Questions (FAQs) about:

- Store hours  
- Shipping policies  
- Returns  
- Product availability  

The chatbot processes natural language input and retrieves the most relevant response from a predefined knowledge base.

---

## ✨ Key Features

### 1️⃣ Intent Recognition
- Detects greetings and farewells using keyword matching.

### 2️⃣ Contextual Response Retrieval
- Uses a structured knowledge base to provide accurate answers.

### 3️⃣ NLP Processing Pipeline
- Tokenization  
- Lemmatization  
- Stop-word removal  

### 4️⃣ Similarity-Based Matching
- Uses **TF-IDF Vectorization**
- Applies **Cosine Similarity**
- Returns the most relevant response even if phrasing differs.

### 5️⃣ Graceful Error Handling
- Provides fallback response when no match is found.
- Suggests contact information for unresolved queries.

---

## 🛠 Technologies Used

| Category | Technology |
|----------|------------|
| Language | Python 3.x |
| NLP Library | NLTK (Natural Language Toolkit) |
| ML Library | Scikit-learn |
| Text Processing | Regex & String Manipulation |

---

## 🧠 How It Works

The chatbot follows a structured NLP pipeline:

### 1️⃣ Preprocessing
- Converts text to lowercase
- Cleans unwanted characters

### 2️⃣ Tokenization
- Splits text into sentences and words

### 3️⃣ Lemmatization
- Converts words to root form  
  Example: `"shipping"` → `"ship"`

### 4️⃣ TF-IDF Vectorization
- Converts text into numerical feature vectors
- Highlights important keywords

### 5️⃣ Cosine Similarity
- Measures similarity between:
  - User input
  - Knowledge base responses
- Returns the response with the highest similarity score

---

## ⚙️ Installation & Setup

### Step 1: Clone the Repository

```bash
git clone <your-repository-link>
cd <project-folder>
```

### Step 2: Install Dependencies

Ensure Python 3.x is installed, then run:

```bash
py -m pip install nltk scikit-learn
```

You may also need to download NLTK resources:

```python
import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
```

### Step 3: Run the Application

```bash
python chatbot.py
```

---

## 💬 Usage Example

```
User: Hello!
Nova: Hi there!

User: What are your shipping options?
Nova: For shipping, we offer standard delivery (3-5 business days) and express delivery (1-2 business days).

User: bye
Nova: Goodbye! Have a great day.
```

---

## 🔮 Future Enhancements

- 🌐 GUI Integration using Flask or Streamlit  
- 🗄 Database Integration for real-time order tracking  
- 🧠 Deep Learning Upgrade (BERT / GPT-based conversational AI)  
- 📱 Web or Mobile Deployment  

---

## 👨‍💻 Author

Developed as part of an **Artificial Intelligence Internship Project**.

---

## ⚠️ Disclaimer

This chatbot is built for educational and demonstration purposes only.
