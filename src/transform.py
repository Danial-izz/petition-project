import pandas as pd
from collections import Counter
from src.preprocessing import preprocess_text

def transform(input_file):
    # Create a dataframe from the JSON data
    data = pd.read_json(input_file)
    df = pd.DataFrame(data)

    # Create a unique ID column
    df['unique_id'] = range(1, len(df) + 1)

    # Apply preprocessing to the 'abstract' column
    df['processed_abstract'] = df['abstract'].apply(lambda x: x['_value']).apply(preprocess_text)

    # Tokenize and count the words in the abstracts
    word_counts = Counter(' '.join(df['processed_abstract']).split())

    # Get the top 20 words with more than 5 letters
    common_words = [word for word, count in word_counts.most_common() if len(word) > 5][:20]

    # Create a blank output dataframe with common words and unique ID
    output_df = pd.DataFrame(columns=['unique_id'] + common_words)

    # Populate the unique ID column
    output_df['unique_id'] = df['unique_id']

    # Populate the columns for each common word
    for word in common_words:
        output_df[word] = df['processed_abstract'].apply(lambda x: x.count(word))

    return output_df
