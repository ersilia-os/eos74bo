# imports
import os
import pandas as pd
import numpy as np
import csv
import sys
from rdkit import Chem

root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(root, ".."))

from predictors.solubility.solubility_predictor import SolubilityPredictor 
from predictors.utilities.utilities import addMolsKekuleSmilesToFrame 

input_file = sys.argv[1]
output_file = sys.argv[2]
output_file = output_file.strip()


def my_model(smiles_list):
    mols = [Chem.MolFromSmiles(smi) for smi in smiles_list]
    kek_mols = []
    for mol in mols:
        if mol is not None:
            Chem.Kekulize(mol)
        kek_mols += [mol]
    kek_smiles = [Chem.MolToSmiles(mol,kekuleSmiles=True) for mol in kek_mols]
    predictor = SolubilityPredictor(kekule_smiles = np.asarray(kek_smiles), smiles = np.asarray(smiles_list))
    pred_df = predictor.get_predictions()
    
    return pred_df

      
# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]

# run model
output_df = my_model(smiles_list)
output_df.rename(columns={"outcome":"sol_proba"}, inplace=True)
output_df.to_csv(output_file, index=False)
