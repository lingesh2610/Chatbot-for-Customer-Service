Customer Service NLP Chatbot

Project Overview

This project was developed as part of a 1-month online internship to demonstrate the application of Natural Language Processing (NLP) in a real-world scenario. The "Nova" Chatbot is designed to assist customers of a fictional electronics store, TechNova, by answering frequently asked questions (FAQs) regarding store hours, shipping policies, returns, and product availability.

Key Features

1) Intent Recognition: Uses keyword matching for greetings and farewells.

2) Contextual Retrieval: Utilizes a knowledge base to answer specific customer queries.

3) NLP Pipeline: Implements tokenization, lemmatization, and stop-word removal.

4) Similarity Scoring: Employs TF-IDF Vectorization and Cosine Similarity to find the most relevant answer even if the user's phrasing varies.

5) Graceful Error Handling: Provides a fallback response and contact information when a query cannot be resolved.

Technologies Used

1. Language: Python 3.x

2. NLP Library: NLTK (Natural Language Toolkit)

3. Machine Learning Library: Scikit-learn (for Vectorization and Similarity)

4. Data Handling: String manipulation and Regular Expressions (Regex)


How It Works

The chatbot follows a standard NLP pipeline to process user input:

1) Preprocessing: The knowledge base and user input are converted to lowercase.

2) Tokenization: Text is broken down into sentences and individual words.

3) Lemmatization: Words are reduced to their root dictionary form (e.g., "shipping" becomes "ship") to improve matching accuracy.

4) TF-IDF Vectorization: Transforms text into numerical vectors, emphasizing unique "keyword" terms over common filler words.

5) Cosine Similarity: Calculates the "angle" between the user query vector and knowledge base vectors. The sentence with the highest similarity score is returned as the answer.

Installation & Setup

To run this project locally, follow these steps:

1. Clone the repository:

git clone <your-repository-link>


2. Install dependencies:
Ensure you have pip installed, then run:

pip install nltk scikit-learn


3. Run the application:

python chatbot.py


Usage Example

User: "Hello!"

Nova: "Hi there!"

User: "What are your shipping options?"

Nova: "For shipping, we offer standard delivery (3-5 business days) and express delivery (1-2 business days)."

User: "bye"

Nova: "Goodbye! Have a great day."

Future Enhancements

GUI Integration: Implementing a web interface using Flask or Streamlit.

Database Integration: Connecting to a SQL database to track real-time order status.

Deep Learning: Upgrading from rule-based/statistical NLP to a Transformer-based model (like BERT or GPT) for more conversational flow.

Author

Developed as part of an Artificial Intelligence Internship project.
