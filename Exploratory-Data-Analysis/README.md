# Exploratory Data Analysis (EDA) on Spotify Tracks Dataset

## 1. Dataset Overview

The Spotify dataset contains 114,000 tracks with 21 features describing song characteristics such as popularity, danceability, energy, loudness, acousticness, tempo, and genre.

### Observation

The dataset includes both numerical and categorical variables, making it suitable for comprehensive exploratory analysis.

### Insight

The variety of audio features enables investigation into factors that may influence song popularity and listener preferences.

---

## 2. Data Cleaning

### Observation

Three columns (`artists`, `album_name`, and `track_name`) contained only one missing value each. No duplicate records were found.

### Insight

The dataset was largely clean and required minimal preprocessing. Missing records were removed without affecting the overall analysis due to the large dataset size.

---

## 3. Distribution of Song Popularity

### Observation

The popularity distribution is heavily concentrated at lower popularity scores, with a noticeable peak near zero. The frequency of songs decreases as popularity increases.

### Insight

Most songs in the Spotify catalog receive relatively low listener engagement, while highly popular tracks represent only a small fraction of the dataset. This indicates that achieving widespread popularity is uncommon among songs.

---

## 4. Explicit vs Non-Explicit Songs

### Observation

Non-explicit songs significantly outnumber explicit songs in the dataset.

### Insight

The Spotify catalog represented in this dataset is dominated by non-explicit content, suggesting that clean tracks are more prevalent than explicit ones.

---

## 5. Correlation Analysis

### Observation

Most audio features show very weak correlations with popularity. However, some audio characteristics exhibit strong relationships with each other.

### Key Findings

#### Energy and Loudness

* Correlation: 0.76

**Insight:**
Songs with higher energy levels tend to be louder. This strong positive relationship suggests that energetic tracks are generally produced with higher perceived volume.

#### Energy and Acousticness

* Correlation: -0.73

**Insight:**
Highly acoustic tracks tend to have lower energy levels, while energetic songs are typically less acoustic in nature.

#### Danceability and Valence

* Correlation: 0.48

**Insight:**
More danceable songs often exhibit higher valence scores, indicating that upbeat and positive tracks are generally easier to dance to.

#### Popularity and Audio Features

* Correlations close to zero

**Insight:**
Popularity does not appear to be strongly influenced by any single audio feature. External factors such as artist reputation, marketing, playlist exposure, and social media trends likely play a greater role in determining a song's success.

---

## 6. Energy vs Popularity Analysis

### Observation

The scatter plot shows a wide spread of popularity values across all energy levels, with no clear upward or downward trend.

### Insight

Energy alone is not a reliable predictor of song popularity. Both low-energy and high-energy songs can achieve similar popularity levels, reinforcing the findings from the correlation analysis.

---

## Overall Conclusion

The analysis reveals that Spotify songs exhibit diverse audio characteristics, but these characteristics alone are insufficient to explain popularity. Strong relationships exist between certain audio features such as energy, loudness, and acousticness, while popularity appears to be influenced by a broader set of factors beyond the musical attributes captured in the dataset.
# Exploratory Data Analysis (EDA) on Spotify Tracks Dataset

## 1. Dataset Overview

The Spotify dataset contains 114,000 tracks with 21 features describing song characteristics such as popularity, danceability, energy, loudness, acousticness, tempo, and genre.

### Observation

The dataset includes both numerical and categorical variables, making it suitable for comprehensive exploratory analysis.

### Insight

The variety of audio features enables investigation into factors that may influence song popularity and listener preferences.

---

## 2. Data Cleaning

### Observation

Three columns (`artists`, `album_name`, and `track_name`) contained only one missing value each. No duplicate records were found.

### Insight

The dataset was largely clean and required minimal preprocessing. Missing records were removed without affecting the overall analysis due to the large dataset size.

---

## 3. Distribution of Song Popularity

### Observation

The popularity distribution is heavily concentrated at lower popularity scores, with a noticeable peak near zero. The frequency of songs decreases as popularity increases.

### Insight

Most songs in the Spotify catalog receive relatively low listener engagement, while highly popular tracks represent only a small fraction of the dataset. This indicates that achieving widespread popularity is uncommon among songs.

---

## 4. Explicit vs Non-Explicit Songs

### Observation

Non-explicit songs significantly outnumber explicit songs in the dataset.

### Insight

The Spotify catalog represented in this dataset is dominated by non-explicit content, suggesting that clean tracks are more prevalent than explicit ones.

---

## 5. Correlation Analysis

### Observation

Most audio features show very weak correlations with popularity. However, some audio characteristics exhibit strong relationships with each other.

### Key Findings

#### Energy and Loudness

* Correlation: 0.76

**Insight:**
Songs with higher energy levels tend to be louder. This strong positive relationship suggests that energetic tracks are generally produced with higher perceived volume.

#### Energy and Acousticness

* Correlation: -0.73

**Insight:**
Highly acoustic tracks tend to have lower energy levels, while energetic songs are typically less acoustic in nature.

#### Danceability and Valence

* Correlation: 0.48

**Insight:**
More danceable songs often exhibit higher valence scores, indicating that upbeat and positive tracks are generally easier to dance to.

#### Popularity and Audio Features

* Correlations close to zero

**Insight:**
Popularity does not appear to be strongly influenced by any single audio feature. External factors such as artist reputation, marketing, playlist exposure, and social media trends likely play a greater role in determining a song's success.

---

## 6. Energy vs Popularity Analysis

### Observation

The scatter plot shows a wide spread of popularity values across all energy levels, with no clear upward or downward trend.

### Insight

Energy alone is not a reliable predictor of song popularity. Both low-energy and high-energy songs can achieve similar popularity levels, reinforcing the findings from the correlation analysis.

---

## Overall Conclusion

The analysis reveals that Spotify songs exhibit diverse audio characteristics, but these characteristics alone are insufficient to explain popularity. Strong relationships exist between certain audio features such as energy, loudness, and acousticness, while popularity appears to be influenced by a broader set of factors beyond the musical attributes captured in the dataset.
