import pandas as pd
from huggingface_hub import list_datasets

all_data = list(list_datasets())
print(len(all_data))
