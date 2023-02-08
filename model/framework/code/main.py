# imports
import os
from os import path
import pandas as pd
import csv
import sys

# current file directory
root = os.path.dirname(os.path.abspath(__file__))
print(root)
sys.path.append('..')

from predictors.solubility.solubility_predictor import SolubilityPredictor
from predictors.utilities.utilities import addMolsKekuleSmilesToFrame 

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

def predict_df(
    smiles_list, 
    smi_column_name='smiles', 
    models=['solubility']
    ):
    
    df = pd.DataFrame({smi_column_name: smiles_list})    
    response = {} 
    working_df = df.copy() 
    addMolsKekuleSmilesToFrame(working_df, smi_column_name) 
    working_df = working_df[~working_df['mols'].isnull() & ~working_df['kekule_smiles'].isnull()] 

    for model in models:
        response[model] = {}
        error_messages = []
        
        if model.lower() == 'solubility': 
            predictor = SolubilityPredictor(
                kekule_smiles = working_df['kekule_smiles'].values, 
                smiles=working_df[smi_column_name].values
                )
        else:
            break

        pred_df = predictor.get_predictions()
        pred_df = working_df.join(pred_df)
        pred_df.drop(
            ['mols', 'kekule_smiles'], 
            axis=1, 
            inplace = True
            )

        # columns not present in original df
        diff_cols = pred_df.columns.difference(df.columns)
        df_res = pred_df[diff_cols]

        # making sure the response df is of the exact same length (rows) as original df
        response_df = pd.merge(
            df, 
            df_res, 
            left_index=True, 
            right_index=True, 
            how='inner'
            )
        return response_df
      
# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]

# run model
output_df = predict_df(smiles_list)

OUTPUT_COLUMN_NAME = "Predicted Class (Probability)"

outputs = []
for x in list(output_df[OUTPUT_COLUMN_NAME]):
    c = int(x.split(" ")[0])
    p = float(x.split("(")[1].split(")")[0])
    if c == 1:
        outputs += [p]
    else:
        outputs += [1-p]
print(outputs)

# write output in a .csv file
with open(output_file, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["value"])  # header
    for o in outputs:
        writer.writerow([o])
 