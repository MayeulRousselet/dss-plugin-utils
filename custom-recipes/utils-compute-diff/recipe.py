import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu
from dataiku.customrecipe import get_input_names_for_role
from dataiku.customrecipe import get_output_names_for_role
from dataiku.customrecipe import get_recipe_config

input_A_dataset = [dataiku.Dataset(name) for name in get_input_names_for_role('input_A_role')][0]
input_B_dataset = [dataiku.Dataset(name) for name in get_input_names_for_role('input_B_role')][0]
input_A_df = input_A_dataset.get_dataframe()
input_B_df = input_B_dataset.get_dataframe()

diff_columns = set(input_A_df.columns).symmetric_difference(input_B_df.columns)
if len(diff_columns) > 0:
    raise Exception("Not the same columns, diff is: {}".format(diff_columns))

#cf https://stackoverflow.com/questions/48647534/find-difference-between-two-data-frames
outer_join = input_A_df.merge(input_B_df, how = 'outer', indicator = True)
anti_join = outer_join[~(outer_join._merge == 'both')].drop('_merge', axis = 1)

main_output_dataset = [dataiku.Dataset(name) for name in get_output_names_for_role('main_output')][0]
main_output_dataset.write_with_schema(anti_join)
