from enigmatoolbox.datasets import fetch_ahba

# fetch gene expression data (gx is a dataframe)
df = fetch_ahba()

# If numpy is preferred:
# Get array of data
genex = df.iloc[:, 1:].to_numpy()

# Get region labels
reglabels = df.iloc[:,0].to_list()

# Get gene labels
glabels = df.columns.values[1:].tolist()