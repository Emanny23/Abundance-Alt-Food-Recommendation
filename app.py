

# import streamlit as st
# import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity

# # Page title
# st.image("https://abundance.coop/wp-content/uploads/2020/04/AbundanceLogoWeb.png")

# st.title("Abundance Food Co-op Alternate Product Recommender Generator")

# st.markdown(
#     """This is an alternative product recommender tool for matching product that are similar In Ingridients and overall product type.
#     """
# )

# #Upload CSV
# uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

# #Data Cleaning Function
# def clean_data(df):
#     # Drop completely empty rows
#     df = df.dropna(how='all')
    
#     # Fill missing text columns with empty string
#     text_cols = df.select_dtypes(include='object').columns
#     df[text_cols] = df[text_cols].fillna("")

#     # Remove duplicates based on a column like 'inv_name'
#     if 'inv_name' in df.columns:
#         df = df.drop_duplicates(subset='inv_name')

#     return df

# #Combine text columns
# def prepare_text(df):
#     text_columns = [col for col in df.columns if col not in ['inv_pk', 'inv_scancode', 'inv_dpt', 'inv_brd']]
#     df['Combined_Text'] = df[text_columns].astype(str).agg(' '.join, axis=1)
#     return df

# # Similarity Computation
# def compute_similarity(text_series):
#     tfidf = TfidfVectorizer()
#     tfidf_matrix = tfidf.fit_transform(text_series)
#     return cosine_similarity(tfidf_matrix, tfidf_matrix)

# #Find Alternatives
# def get_top_similar_products(df, sim_matrix, top_n=7, threshold=0.95):
#     results = []

#     for idx, row in df.iterrows():
#         product_name = row['inv_name']
#         similarities = list(enumerate(sim_matrix[idx]))
#         filtered = [(i, score) for i, score in similarities if i != idx and score >= threshold]
#         top_matches = sorted(filtered, key=lambda x: x[1], reverse=True)[:top_n]

#         for match_idx, score in top_matches:
#             matched_row = df.iloc[match_idx]
#             results.append({
#                 "original_product": product_name,
#                 "inv_pk": row["inv_pk"],
#                 "inv_scancode": row["inv_scancode"],
#                 "similar_product": matched_row["inv_name"],
#                 "similarity_score": score,
#                 "similar_inv_pk": matched_row["inv_pk"],
#                 "similar_brd_name": matched_row["dpt_name"],
#                 "similar_dpt_name": matched_row["brd_name"]
#             })

#     return pd.DataFrame(results)

# # Main flow
# if uploaded_file:
#     df_raw = pd.read_csv(uploaded_file)
#     df_clean = clean_data(df_raw)
#     df_ready = prepare_text(df_clean)
    
#     st.subheader("Preview Cleaned Data:")
#     st.dataframe(df_ready.head())

#     if st.button("🔍 Find Similar Products and Export to Excel"):
#         cosine_sim = compute_similarity(df_ready['Combined_Text'])
#         result_df = get_top_similar_products(df_ready, cosine_sim)

#         st.success("✅ Similar products generated!")

#         st.subheader("Sample Results")
#         st.dataframe(result_df.head())

#         result_df.to_excel("similar_products_output.xlsx", index=False)
#         with open("similar_products_output.xlsx", "rb") as f:
#             st.download_button("📥 Download Excel File", f, file_name="similar_products.xlsx")




import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Page title
st.image("https://abundance.coop/wp-content/uploads/2020/04/AbundanceLogoWeb.png")

st.title("Abundance Food Co-op Alternate Product Recommender Generator")

st.markdown(
    """This is an alternative product recommender tool for matching products that are similar In Ingredients and overall product type."""
)

# Upload CSV
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

# Data Cleaning Function
def clean_data(df):
    df = df.dropna(how='all')
    text_cols = df.select_dtypes(include='object').columns
    df[text_cols] = df[text_cols].fillna("")
    if 'inv_name' in df.columns:
        df = df.drop_duplicates(subset='inv_name')
    return df

# Combine text columns
def prepare_text(df):
    text_columns = [col for col in df.columns if col not in ['inv_pk', 'inv_scancode', 'inv_dpt', 'inv_brd', 'inv_name']]
    df['Combined_Text'] = df[text_columns].astype(str).agg(' '.join, axis=1)
    return df

# Similarity Computation
def compute_similarity(text_series):
    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform(text_series)
    return cosine_similarity(tfidf_matrix, tfidf_matrix)

# Find Alternatives
def get_top_similar_products(df, sim_matrix, top_n=7, threshold=0.95):
    results = []

    for idx, row in df.iterrows():
        if idx >= sim_matrix.shape[0]:  # safety check
            continue

        similarities = list(enumerate(sim_matrix[idx]))
        filtered = [(i, score) for i, score in similarities if i != idx and score >= threshold]
        top_matches = sorted(filtered, key=lambda x: x[1], reverse=True)[:top_n]

        for match_idx, score in top_matches:
            matched_row = df.iloc[match_idx]
            results.append({
                "original_product": row["inv_name"],
                "similar_product": matched_row["inv_name"],
                "inv_pk": row["inv_pk"],
                "inv_scancode": row["inv_scancode"],
                "similarity_score": score,
                "similar_inv_pk": matched_row["inv_pk"],
                "similar_brd_name": matched_row["brd_name"],  # corrected
                "similar_dpt_name": matched_row["dpt_name"]   # corrected
            })

    return pd.DataFrame(results)

# Main flow
if uploaded_file:
    df_raw = pd.read_csv(uploaded_file)
    df_clean = clean_data(df_raw)
    df_clean = df_clean.reset_index(drop=True)  # ✅ reset index before computing similarity
    df_ready = prepare_text(df_clean)
    
    st.subheader("Preview Cleaned Data:")
    st.dataframe(df_ready.head())

    if st.button("🔍 Find Similar Products and Export to Excel"):
        cosine_sim = compute_similarity(df_ready['Combined_Text'])

        # double-check shapes match
        if cosine_sim.shape[0] != len(df_ready):
            st.error("❌ Similarity matrix size mismatch. Check data cleaning steps.")
        else:
            result_df = get_top_similar_products(df_ready, cosine_sim)

            st.success("✅ Similar products generated!")

            st.subheader("Sample Results")
            st.dataframe(result_df.head())

            result_df.to_excel("similar_products_output.xlsx", index=False)
            with open("similar_products_output.xlsx", "rb") as f:
                st.download_button("📥 Download Excel File", f, file_name="similar_products.xlsx")
