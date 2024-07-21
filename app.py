import streamlit as st
import streamlit.components.v1 as stc
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")
import seaborn as sns
import spacy
nlp = spacy.load('en_core_web_sm')
from textblob import TextBlob
import neattext as nt
import neattext.functions as nfx
from collections import Counter
from wordcloud import WordCloud

#! Functions
# This method will be used for text analysis
def text_analyzer(my_textt):
    docx = nlp(my_textt)
    all_data = [(token.text, token.shape_,
                 token.pos_, token.tag_, 
                 token.lemma_, token.is_alpha,
                 token.is_stop) for token in docx]

    # Create dataframe
    df = pd.DataFrame(all_data,
                     columns=['Token', 'Shape', 'PoS', 'Tag', 'Lemma', 'Is_Alpha', 'Is_Stopword'])
    return df


# Funct to extract entities from raw data
def get_entities(my_text):
    docx = nlp(my_text)
    entities = [(entity.text, entity.label_) for entity in docx.ents]
    return entities


# Func to get most common tokens
def get_most_common_tokens(my_text, num=5):
    word_tokens = Counter(my_text.split(' '))
    most_common_tokens = dict(word_tokens.most_common(num))
    return most_common_tokens


# Func to get sentiment 
def get_sentiment(my_text):
    blob = TextBlob(my_text)
    sentiment = blob.sentiment
    return sentiment


# Get words for WordCloud
def plot_wordcloud(my_text):
    wc = WordCloud().generate(my_text)
    fig = plt.figure()
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(fig)



def main():
    st.title("NLP Application With Streamlit")

    # Desing Menu
    menu = ['Home', 'NLP(Files)', "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    # Condition to manage Menu
    if choice == "Home":
        st.subheader("Home: Analyse Text")

        # Text Area to receive text from user
        raw_text = st.text_area("Enter Text Here...", height=250)
        # To Chose number of tokens to be processed by NLP Model
        num_most_common = st.sidebar.number_input("Most Common Tokesn", 1, 10)

        if st.button("Analyze"):
            with st.expander("Original Text"):
                st.write(raw_text)

            with st.expander("Text Analysis"):
                token_res_df = text_analyzer(raw_text)
                st.dataframe(token_res_df)

            with st.expander("Entities"):
                entity_res = get_entities(raw_text)
                st.write(entity_res, height=500, scrolling=True)


            # Desing Layout
            col1, col2 = st.columns(2) # Number of columns

            with col1:
                with st.expander("Word Stats"):
                    st.info("Word Statistics")
                    docx = nt.TextFrame(raw_text)
                    st.write(docx.word_stats())

                with st.expander("Top Keywords"):
                    st.info("Top Keywords/Tokens")
                    processed_text = nfx.remove_stopwords(raw_text)
                    key_words = get_most_common_tokens(processed_text, num_most_common)
                    st.write(key_words)

                with st.expander("Sentiment"):
                    sent_res = get_sentiment(raw_text)
                    st.write(sent_res)

            with col2:
                with st.expander("Plot Word's Frequency"):
                    fig = plt.figure()
                    top_key_words = get_most_common_tokens(processed_text, num_most_common)
                    plt.bar(key_words.keys(),
                            top_key_words.values() )
                    st.pyplot(fig)

                with st.expander("Plot Part Of Speech"):
                    fig = plt.figure()
                    sns.countplot(x=token_res_df['PoS'], palette='viridis')
                    plt.xticks(rotation=45)
                    st.pyplot(fig)

                with st.expander("Plot WordCloud"):
                    plot_wordcloud(raw_text)

            with st.expander("Download Text Analysis Result"):
                pass


    # Manage (NLP Files)
    elif choice == "NLP(Files)":
        st.subheader("NLP Task")
    
    # About Page
    else:
        st.subheader("About")


if __name__ == '__main__':
    main()