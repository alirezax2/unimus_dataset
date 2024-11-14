import pandas as pd

df = pd.read_parquet('MUSIT_arkeologi.parquet')
df.shape

df.head(5)

df.Artefact.unique().shape

df.iloc[0:1000].Artefact.unique().shape
df = df.iloc[0:1000][['Artefact']]

import pandas as pd
import torch
from transformers import AutoTokenizer, AutoModel
from sklearn.cluster import KMeans



# Load the model and tokenizer for DistilBERT
model_name = "distilbert-base-uncased"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModel.from_pretrained(model_name)

# Function to get sentence embeddings by mean pooling
def get_sentence_embeddings(texts):
    inputs = tokenizer(texts, padding=True, truncation=True, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
        embeddings = outputs.last_hidden_state
    # Mean Pooling
    embeddings = embeddings.mean(dim=1)
    return embeddings

# Step 1: Generate embeddings for each description
embeddings = get_sentence_embeddings(df["Artefact"].tolist())

# Step 2: Apply KMeans clustering to group into 5 clusters
num_clusters = 10
kmeans = KMeans(n_clusters=num_clusters, random_state=0)
df['cluster'] = kmeans.fit_predict(embeddings.numpy())

# Print the resulting clusters
for cluster_num in range(num_clusters):
    print(f"\nCluster {cluster_num}:")
    print(df[df['cluster'] == cluster_num]['Artefact'].tolist())


cluster=1
mylst= df[df['cluster'] == cluster_num]['Artefact'].tolist()
list(set(mylst))