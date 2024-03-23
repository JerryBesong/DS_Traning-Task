# Import necessary libraries
import spacy
import re
import pandas as pd
from textblob import TextBlob

# Load the English model
nlp = spacy.load('en_core_web_sm')

# load dataframe
dataframe = pd.read_csv('amazon_product_reviews.csv', low_memory =False)

# display dataframe
print(dataframe["reviews.text"].head())
print(dataframe["reviews.text"].shape)
dataframe["reviews.text"].isnull().sum()

# drop rows with missing reviews amd print
clean_data = dataframe.dropna(subset =["reviews.text"])
reviews_data = clean_data["reviews.text"]
print(reviews_data.shape)
print(reviews_data.head())

# Creating a function to preprocess "reviews.text"
def preprocessing(text):
    """
    This function performs several preprocessing steps on the input text:
    1. Removes the use of special case or characters using a regular expression, keeping only words and spaces.
    2. performs tokenization with the Use of spaCy NLP library to process the cleaned text,.
    3. Generates a list of lemmatized tokens from the processed text, excluding stopwords and punctuation.
    4. Concatenates the lemmatized tokens back into a single string.
    Function to perform sentiment analysis on a product review.
    
    Parameters:
        text (str): The input product review text.
    
    Returns:
        str: cleaned and processed text.
    """
    special_case = r'[^\w\s]'
    processed_text = re.sub(special_case, " ", text )
    
    # using spacy to process the text
    doc = nlp(processed_text)
    
    processed_token = []
    
    for token in doc:
        if not token.is_stop and not token.is_punct and token.text.strip():
            # lammatize the token, convert it to lowercase
            clean_token = token.lemma_.lower()
            processed_token.append(clean_token)
        # join the clean token to a string
    clean_text = " ".join(processed_token)
    
    return clean_text
print("Done")

processed_reviews = reviews_data.apply(preprocessing)
print(processed_reviews.head())

# Define a function for sentiment analysis using TextBlob    
def sentiment_analysis(reviews):
    """
    Function to perform sentiment analysis on a product review.
    
    This function utilizes TextBlob to compute the sentiment polarity of the input review text. 
    The polarity score is connoted with a negative, neutral, positive sentiment
    
    Parameters:
        review (str): The input product review text.
    
    Returns:
        str: Sentiment of the review ('positive', 'negative', or 'neutral').
    """
    # Perform sentiment analysis using TextBlob
    analysis = TextBlob(reviews)
    
    # Determine sentiment polarity
    polarity = analysis.sentiment.polarity
    
    # Classify sentiment
    if polarity > 0:
        return 'positive'
    elif polarity == 0:
        return 'neutral'
    else:
        return 'negative'

# Apply sentiment analysis to preprocessed reviews and store results in a new 'polarity' column
clean_data["polarity"] = processed_reviews.apply(sentiment_analysis)

# Display the original reviews with their corresponding polarity scores
print(clean_data[["reviews.text", "polarity"]].head())

# load larger spacy model
nlp = spacy.load("en_core_web_md")

# Prompt user for indices of reviews to compare for similarity
index_num1 = input('Please enter the index number of the first review you want to compare: ')
if index_num1.strip().isdigit():
    index_num1 = int(index_num1)
else:
    print("Please enter a valid integer.")

index_num2 = input('Please enter the index number of the first review you want to compare: ')
if index_num2.strip().isdigit():
    index_num2 = int(index_num2)
else:
    print("Please enter a valid integer.")

# Ensure user-selected indices are valid
num_reviews = len(reviews_data)
if index_num1 < 0 or index_num1 >= num_reviews or index_num1 < 0 or index_num2 >= num_reviews:
    print('\n',"Error: Invalid index. Please enter indices within the range 0 to", num_reviews - 1)
else:
    # Retrieve and display the selected reviews
    review_a = reviews_data.iloc[index_num1]
    review_b = reviews_data.iloc[index_num2]
    
    print("Review A:", review_a, '\n')
    print("Review B:", review_b, '\n')

    # Calculate and display the similarity score between the two reviews
    doc_a = nlp(review_a)
    doc_b = nlp(review_b)    
    similarity_score = doc_a.similarity(doc_b)
    print(f'Similarity score of the two reviews: {round(similarity_score,3)}')
    
# Additional interactive component for testing sentiment analysis on a set number of reviews
selection_num = int(input("Enter the number of reviews you want to test: "))
# Select and display sentiment scores for the first 'n' reviews specified by the user
sample_reviews = processed_reviews.head(selection_num)  
for review in sample_reviews:
    sentiment_score = sentiment_analysis(review)
    print("Review:", review)
    print("Sentiment Score:", sentiment_score)
    print()