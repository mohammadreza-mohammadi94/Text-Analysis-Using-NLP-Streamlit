# Text Analysis Using NLP with Streamlit

Welcome to the Text Analysis Using NLP with Streamlit repository. This project demonstrates how to leverage Natural Language Processing (NLP) techniques to perform various text analysis tasks, integrated into an interactive web application using Streamlit.

## Overview

This repository provides a comprehensive text analysis tool that includes functionalities such as text preprocessing, sentiment analysis, named entity recognition, and more. The web application is built with Streamlit, making it easy to deploy and interact with various NLP models and techniques.

## Features

- **Text Preprocessing:** Clean and preprocess text data by removing stopwords, punctuation, and applying tokenization.
- **Sentiment Analysis:** Analyze the sentiment of the input text (positive, negative, neutral) using pre-trained models.
- **Named Entity Recognition (NER):** Identify and classify named entities (e.g., persons, organizations, locations) in the text.
- **Word Cloud Generation:** Visualize the most frequent words in the text data using word clouds.
- **Part-of-Speech Tagging:** Tag each word in the text with its respective part-of-speech.
- **Customizable Parameters:** Easily adjust parameters for different NLP tasks through the Streamlit interface.

## Getting Started

### Prerequisites

Ensure you have the following installed on your machine:

- Python 3.6 or higher
- pip (Python package installer)

### Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/mohammadreza-mohammadi94/Text_Analysis_Using_NLP_Streamlit.git
    cd Text_Analysis_Using_NLP_Streamlit
    ```

2. **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

To run the Streamlit application, use the following command:
```bash
streamlit run app.py
```

This will start a local web server and open the application in your default web browser.

## Project Structure

- `app.py`: Main application file containing the Streamlit interface and NLP functionalities.
- `requirements.txt`: List of required Python packages.
- `utils.py`: Utility functions for text preprocessing and NLP tasks.
- `README.md`: Project documentation.

## Usage

Once the application is running, you can perform various NLP tasks by entering text into the input field and selecting the desired analysis options. The results will be displayed interactively on the web page.

## Example

Here's a brief example of how to use the application:

1. Open the application by running `streamlit run app.py`.
2. Enter the text you want to analyze in the input field.
3. Select the desired NLP tasks such as Sentiment Analysis, Named Entity Recognition, etc.
4. View the results displayed interactively on the web page.

## Contributing

Contributions are welcome! If you have any ideas for improvements or new features, feel free to open an issue or submit a pull request.

### Steps to Contribute

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- [Streamlit](https://www.streamlit.io/) for providing an easy-to-use framework for building web applications.
- [spaCy](https://spacy.io/) for providing powerful NLP tools and models.

## Contact

For any questions or feedback, please feel free to reach out via GitHub issues.
