"""
Sentiment Analyzer is a Python script that defines a sentiment analysis bot
that uses the TextBlob library to assess the sentiment of user-provided text
and respond with a corresponding emoji and sentiment score.
"""

# Import the TextBlob class from the TextBlob library for text sentiment analysis
from textblob import TextBlob
# Import the dataclass decorator from the dataclasses module
from dataclasses import dataclass

# The Mood class is used to represent the result of the sentiment analysis. 
@dataclass
class Mood:
    """
    @dataclass: Decorator used to create a data class. In this case, it defines the Mood class, which has two attributes:
    emoji (a string representing an emoji) and
    sentiment (a float representing the sentiment score).
    """
    emoji: str
    sentiment: float

# Define a function to determine the mood based on sentiment
def get_mood(input_text: str, *, sensitivity: float) -> Mood:

    polarity: float = TextBlob(input_text).sentiment.polarity
    """
    This line calculates the sentiment polarity of the input_text using TextBlob's sentiment analysis.
    The polarity is a float value that represents the sentiment score of the input text.
    A positive value indicates positive sentiment,
    a negative value indicates negative sentiment,
    and a value around 0 indicates neutral sentiment.
    """

    # Calculate the thresholds for classifying sentiment
    friendly_threshold: float = sensitivity
    hostile_threshold: float = -sensitivity

    # Determine the mood and return a Mood object
    if polarity >= friendly_threshold:
        # Return a happy emoji if the sentiment is positive
        return Mood('😊', polarity)
    
    elif polarity <= hostile_threshold:
        # Return an angry emoji if the sentiment is negative
        return Mood('😠', polarity)
    
    else:
        # Return a neutral emoji if the sentiment is neither positive nor negative
        return Mood('😐', polarity)
    
def run_bot():
    print("Enter some text for your sentiment analysis or 'exit' to exit :")
    while True:
        user_input: str = input('You: ')
        if user_input.strip().lower() == 'exit':
            print('Exited Succesfully!')
            break

        # Get the mood for the user's input using the get_mood function
        mood: Mood = get_mood(user_input, sensitivity=0.25)

        print(f'Bot: {mood.emoji} ({mood.sentiment})')

# Driver Code
if __name__ == '__main__':
    run_bot()