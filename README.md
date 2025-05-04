# 🛒 Abundance Alternative Food Recommendation System

## 📌 Project Overview

##### The purpose of this project is to build an **Alternative Product Recommender System** for a grocery store. It suggests similar items when a customer's intended product is **out of stock**, helping the business:

##### - ✅ Retain sales that would otherwise be lost
##### - ✅ Enhance customer experience by reducing frustration
##### - ✅ Provide scalable, automated product substitutions using NLP

---

## 🧹 Data Preparation

#### Over two weeks, I cleaned and structured the dataset for effective similarity matching.

### Key Steps:
##### - **Removed discontinued inventory** to ensure relevance
##### - **Standardized missing values** by replacing blanks with `NaN`, then with `None` for processing
##### - **Dropped unrelated columns** to streamline the dataset
##### - **Separated ingredient data in Excel** to improve matching quality

### Core Features Used:
##### - `inv_name`  
##### - `pi1_description`, `pi2_description`  
##### - `brd_name` (Brand), `dpt_name` (Department)  
##### - All ingredient-related columns

---

## 🧠 Modeling Approach

### Two NLP-based models were developed to recommend alternative products:

### 1. TF-IDF + Cosine Similarity
##### - Converts product text into frequency-based vectors
##### - Measures similarity based on word usage
##### - Lightweight and interpretable baseline

### 2. BERT + Cosine Similarity
##### - Uses **Bidirectional Encoder Representations from Transformers**
##### - Understands context and meaning in product descriptions
##### - More powerful for nuanced matches

---

## 🔎 Results

##### - Both models return a ranked list of similar items
##### - Due to missing ingredient data, some matches are imperfect — but performance is strong for well-labeled items
##### - Final goal: Automate the recommendation process and export results to Excel

---

## ✅ Final Deliverables

### 📄 Excel Sheet
Includes:
##### - Product name
##### - Top 4–7 alternatives
##### - Similarity scores
##### - Brand, department, `inv_scancode`, `inv_pk` for business reference

### 🌐 Streamlit App
##### - Non-technical interface to:

  ##### - View recommended alternatives
  ##### - Export results to Excel

### 🧪 Optimized & Validated Data
##### - Cleaned, tested, and fine-tuned dataset
##### - Model outputs validated for business use

---

## 🚀 Future Improvements
##### - Integrate real-time inventory updates
##### - Use customer purchase history for personalization
##### - Improve ingredient data quality through NLP parsing

---

## 💡 Summary

### This MVP shows how **data science can solve real business problems** — by minimizing lost sales and improving customer satisfaction, even in everyday use cases like grocery shopping.