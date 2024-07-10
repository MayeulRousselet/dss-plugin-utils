import dataiku
from dataiku.customrecipe import get_input_names_for_role
from dataiku.customrecipe import get_output_names_for_role
from dataiku.customrecipe import get_recipe_config
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

input_datasets = [dataiku.Dataset(name) for name in get_input_names_for_role('input_role')]
output_datasets = [dataiku.Dataset(name) for name in get_output_names_for_role('main_output')]

input_dataset = input_datasets[0]
schema = input_dataset.read_schema()

columns_df = pd.DataFrame.from_dict(schema)

output_dataset = output_datasets[0]
output_dataset.write_with_schema(columns_df)
