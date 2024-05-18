import pandas as pd
import psycopg2
from datetime import datetime

# Define the connection parameters
host = 'localhost'
port = 5432
database = 'parch'
username = 'postgres'
password = '12345'

# Define the file path of the CSV
csv_file = r"C:\\Users\\DELL\\Desktop\\UI\\Future_train.csv"

# Function to upload data to the database
def upload_to_database():
    print("Reading the CSV file...")
    # Read the CSV file
    df = pd.read_csv(csv_file)

    print("Establishing connection to the database...")
    # Establish a connection to the database
    conn = psycopg2.connect(host=host, port=port, database=database, user=username, password=password)
    print("Connection successful.")

    # Create a cursor
    cursor = conn.cursor()

    print("Inserting data into the database...")
    # Iterate over each row in the DataFrame and insert it into the database
    for index, row in df.iterrows():
        cursor.execute('''INSERT INTO retrain_model (
                            chroma_stft, chroma_cqt, chroma_cens, melspectrogram, mfccs, rms,
                            spectral_centroid, spectral_bandwidth, spectral_contrast, spectral_flatness,
                            spectral_rolloff, poly_features, zero_crossing_rate, harmonic_centroid,
                            harmonic_tonnetz, harmonic_rms, harmonic_spectral_flatness,
                            harmonic_spectral_contrast, harmonic_spectral_rolloff, harmonic_zero_crossing_rate,
                            command_executed, _record_source, _load_timestamp)
                            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)''',
                       (row['chroma_stft'], row['chroma_cqt'], row['chroma_cens'], row['melspectrogram'],
                        row['mfccs'], row['rms'], row['spectral_centroid'], row['spectral_bandwidth'],
                        row['spectral_contrast'], row['spectral_flatness'], row['spectral_rolloff'],
                        row['poly_features'], row['zero_crossing_rate'], row['harmonic_centroid'],
                        row['harmonic_tonnetz'], row['harmonic_rms'], row['harmonic_spectral_flatness'],
                        row['harmonic_spectral_contrast'], row['harmonic_spectral_rolloff'],
                        row['harmonic_zero_crossing_rate'], row['command_executed'], row['_record_source'],
                        datetime.now()))

    print("Data insertion complete.")
    # Commit the transaction and close the connection
    conn.commit()
    conn.close()
    print("Connection closed.")

# Call the function to upload data to the database
upload_to_database()