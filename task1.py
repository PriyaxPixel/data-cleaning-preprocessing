import pandas as pd

print("========== TASK 1 START ==========")

# ===== POINT 1: Dataset Import Aur Structure Dekho =====
print("\n1. Dataset Load Kar Rahe Hain...")
# Tere file ka naam 'country-data.csv' hai with small c
df = pd.read_csv('country-data.csv', header=None)

# Column ke naam de rahe hain kyunki CSV mein header nahi hai
df.columns = ['Country', 'Region', 'Population', 'Area', 'Pop_Density', 'Coastline', 
              'Net_migration', 'Infant_mortality', 'GDP', 'Literacy']

print("\nPehli 5 Rows:")
print(df.head())
print("\nData Ki Jankari:")
df.info()
print("\nShape:", df.shape)

# ===== POINT 2: Ganda Data Dhundo =====
print("\n\n2. Missing Values Aur Duplicate Check...")
print("\nKahan-Kahan Khali Hai:")
print(df.isnull().sum())
duplicate_count = df.duplicated().sum()
print(f"\nTotal Duplicate Rows: {duplicate_count}")

# ===== POINT 3: Data Saaf Karo =====
print("\n\n3. Data Saaf Kar Rahe Hain...")
df_clean = df.drop_duplicates()
print(f"Duplicate hatane ke baad rows: {len(df_clean)}")

# Sabhi numeric columns ko number banao aur khali jagah 0 se bharo
numeric_cols = df_clean.columns[2:] # Country aur Region chod ke sab
for col in numeric_cols:
    df_clean[col] = pd.to_numeric(df_clean[col], errors='coerce').fillna(0)

df_clean['Country'] = df_clean['Country'].fillna('Unknown')
df_clean['Region'] = df_clean['Region'].fillna('Unknown')

print("\nNull check after clean:")
print(df_clean.isnull().sum())

# ===== POINT 4: Data Ready =====
print("\n\n4. CLEANED DATA READY:")
print(df_clean.head())

# ===== BONUS: Save the new file =====
df_clean.to_csv('cleaned_country_data.csv', index=False)
print("\n\n====== TASK 1 COMPLETE ======")
print("New file saved: cleaned_country_data.csv")
print("Submit this file")
