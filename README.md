# Movie Recommendation System [📌](https://movie-recommender-system-efkk.onrender.com)
A content based movie recommendation system that recommends movies based on content similarity.

## Workflow :
1. Data cleaning and preprocessing
2. Feature engineering using text tags
3. Text vectorization
4. Similarity calculation
5. Recommendation list

### Dataset source:
TMDB Movie Dataset from Kaggle
### Data preprocessing
Cleaned the data and by extracting metadata, merged multiple columns into a single tags column
### Feature extraction
Performed stemming on the 'tags' column that reduces derived words to base or root form using nltk library
### Text vectorization
Used Bag of Words approach which calculates frequency of a word. Applied CountVectorizer to convert text into vectors.
### Similarity calculation
Calculated Cosine similarity between movies vectors to find ten nearest movies.
### Poster
Integrated TMDB API to fetch movie posters. Posters are visible with the name of the movies.
### UI
Streamlit was used to build simple interactive interface.

## Libraries
* Numpy
* Pandas
* NLTK
* Scikit-learn
* Streamlit

## Deployment
Hosted on Render.
[Link](https://movie-recommender-system-efkk.onrender.com)
