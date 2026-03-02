Customer Service NLP Chatbot

Project Overview

This project was developed as part of a 1-month online internship to demonstrate the application of Natural Language Processing (NLP) in a real-world scenario. The "Nova" Chatbot is designed to assist customers of a fictional electronics store, TechNova, by answering frequently asked questions (FAQs) regarding store hours, shipping policies, returns, and product availability.

Key Features

Intent Recognition: Uses keyword matching for greetings and farewells.

Contextual Retrieval: Utilizes a knowledge base to answer specific customer queries.

NLP Pipeline: Implements tokenization, lemmatization, and stop-word removal.

Similarity Scoring: Employs TF-IDF Vectorization and Cosine Similarity to find the most relevant answer even if the user's phrasing varies.

Graceful Error Handling: Provides a fallback response and contact information when a query cannot be resolved.

Technologies Used

Language: Python 3.x

NLP Library: NLTK (Natural Language Toolkit)

Machine Learning Library: Scikit-learn (for Vectorization and Similarity)

Data Handling: String manipulation and Regular Expressions (Regex)

How It Works

The chatbot follows a standard NLP pipeline to process user input:

Preprocessing: The knowledge base and user input are converted to lowercase.

Tokenization: Text is broken down into sentences and individual words.

Lemmatization: Words are reduced to their root dictionary form (e.g., "shipping" becomes "ship") to improve matching accuracy.

TF-IDF Vectorization: Transforms text into numerical vectors, emphasizing unique "keyword" terms over common filler words.

Cosine Similarity: Calculates the "angle" between the user query vector and knowledge base vectors. The sentence with the highest similarity score is returned as the answer.

Installation & Setup

To run this project locally, follow these steps:

Clone the repository:

git clone <your-repository-link>


Install dependencies:
Ensure you have pip installed, then run:

pip install nltk scikit-learn


Run the application:

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
