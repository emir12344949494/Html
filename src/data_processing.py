import os
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: The file at {file_path} is empty.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def preprocess_data(df, n_components=10):
    # Normalize features for PCA
    X = df.drop(columns=['target'])
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Dimensionality reduction using PCA
    pca = PCA(n_components=n_components)
    X_pca = pca.fit_transform(X_scaled)

    return X_pca

def save_data(data, file_path):
    try:
        # Ensure the directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        pd.DataFrame(data).to_csv(file_path, index=False)
        print(f"Processed data saved to {file_path}")
    except Exception as e:
        print(f"An error occurred while saving the file: {e}")

def main():
    input_file = 'data/raw/datos.csv'
    output_file = 'data/processed/processed_data.csv'
    
    df = load_data(input_file)
    if df is not None:
        processed_data = preprocess_data(df)
        save_data(processed_data, output_file)

if __name__ == "__main__":
    main()

