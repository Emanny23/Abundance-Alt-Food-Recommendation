# Abundance-Alt-Food-Recommendation

### Purpose of MVP

# The main function of this project is to create an Alternative Food recommender system that is able to recommend similar products when the originally intended Item of purchase Is out of stock. I have taken the last 2 weeks preparing the data but there are so many empty fields in the ingredients fields, there may be products that are poorly matched compared to others. In the notebook we can observe each process through the lines of code in the beginning as they serve a specific purpose in this process. The main columns that are relevant to our usecase for the alternative product recommender system are the following columns, inv_name, pi1_descritpion, pi2_description, brd_name, dpt_name and than all of the Ingredient columns which were separated in excel for better product matching. 


## Methodology/Explain my approaches and problems ecountered along the way

# In the code we have 2 models that will serve the purpose of retrieving alternative products.
# The first model is the TFIDF vectorizer using Cosine similarity, 2nd model will be the a Bert model utilziing Cosine Similarity 

## Term Frequency- A measure of how many times a given word appears in a document
## Inverse Document Frequency- A measure of how many times the same word occurs in other documents within the corpus

## BERT, which stands for Bidirectional Encoder Representations from Transformers, is based on transformers, a deep learning model in which every output element is connected to every input element, and the weightings between them are dynamically calculated based upon their connection






# you can observe the outputs of the models and it will give you the alternative products recommended based on similariy matching. It's not the best but based on the amounut of empty fields I am working with, its not bad at all! The end Goal is to be able to run the defined funcions in the manner where I am able to retrieve all the different products and there recommended alternatives in an excel sheet that I am able to store. 


## Final Deliverables
## Excel File with Alternative Product Recommendations

## Includes product names, top 4-7 alternatives, similarity scores, dpt_name, brd_name, inv_scancode, inv_pk for easy business reference
## Streamlit App for Interactive Use

## Allows non technical folks to search for products, view alternatives, compare details, adjust recommendations, and export to Excel
## Optimized & Validated Data

## Fine-tune similarity thresholds and test accuracy before final delivery