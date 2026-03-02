import nltk
import string
import warnings
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Suppress warnings for a cleaner output
warnings.filterwarnings('ignore')

# Download necessary NLTK data packages
def setup_nltk():
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        nltk.download('punkt')
        nltk.download('wordnet')
        nltk.download('omw-1.4')
        nltk.download('punkt_tab')

setup_nltk()

# --- KNOWLEDGE BASE ---
# In a real-world scenario, this could be loaded from a JSON or TXT file.
# For this project, we define a robust set of FAQs about a fictional tech store.
knowledge_base = """
Hello! Welcome to TechNova Support. 
How can I help you today?
We offer a wide range of products including laptops, smartphones, and accessories.
Our store hours are Monday to Friday, 9 AM to 6 PM.
We are located at 123 Innovation Drive, Silicon Valley.
For shipping, we offer standard delivery (3-5 business days) and express delivery (1-2 business days).
Returns are accepted within 30 days of purchase with a valid receipt.
To track your order, please visit the 'My Orders' section on our website.
You can contact our human agents at support@technova.com or call 1-800-TECH-NOV.
We accept all major credit cards, PayPal, and Apple Pay.
The warranty on most electronic items is 1 year from the date of purchase.
If you received a damaged item, please contact us immediately for a replacement.
Our laptops come pre-installed with the latest operating systems.
We do offer international shipping to over 50 countries.
Discounts are available for students and seasonal sales happen every quarter.
"""

# Preprocessing: Tokenization
# Convert text to lowercase and split into sentences
sent_tokens = nltk.sent_tokenize(knowledge_base.lower())

# Word Lemmatization
lemmer = nltk.stem.WordNetLemmatizer()

def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

# --- GREETING LOGIC ---
GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "whats up", "hey",)
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]

def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)

# --- RESPONSE GENERATION ---
def response(user_response):
    robo_response = ''
    sent_tokens.append(user_response)
    
    # TF-IDF Vectorization: Term Frequency - Inverse Document Frequency
    # This identifies the importance of words in the query relative to the knowledge base
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    
    # Cosine Similarity: Calculate how close the user query is to our knowledge base sentences
    vals = cosine_similarity(tfidf[-1], tfidf)
    
    # Find the most similar sentence (excluding the user query itself at index -1)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    
    if(req_tfidf == 0):
        robo_response = robo_response + "I am sorry, I don't quite understand that. Could you try rephrasing or contact support@technova.com?"
        return robo_response
    else:
        robo_response = robo_response + sent_tokens[idx]
        return robo_response

# --- MAIN CHAT LOOP ---
def main():
    flag = True
    print("\n" + "="*50)
    print("TECHNOVA CUSTOMER SUPPORT CHATBOT")
    print("="*50)
    print("Bot: My name is Nova. I can answer questions about store hours, shipping, and returns.")
    print("     Type 'bye' to exit the conversation.\n")

    while(flag == True):
        user_response = input("You: ")
        user_response = user_response.lower()
        
        if(user_response != 'bye'):
            if(user_response == 'thanks' or user_response == 'thank you'):
                flag = False
                print("Nova: You are welcome!")
            else:
                if(greeting(user_response) != None):
                    print("Nova: " + greeting(user_response))
                else:
                    print("Nova: ", end="")
                    print(response(user_response))
                    sent_tokens.remove(user_response)
        else:
            flag = False
            print("Nova: Goodbye! Have a great day.")

if __name__ == "__main__":
    main()