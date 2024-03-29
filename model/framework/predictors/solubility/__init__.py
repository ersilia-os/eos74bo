import os
import sys

root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(root, ".."))

from predictors.utilities.utilities import load_gcnn_model_with_versioninfo

solubility_model_file_url = os.path.abspath(os.path.join(root, '../../../checkpoints/gcnn_model.pt'))
solubility_model_file_path = os.path.abspath(os.path.join(root, '../../../checkpoints/gcnn_model.pt'))

print(f'Loading Solubility graph convolutional neural network model', file=sys.stdout)
solubility_gcnn_scaler, solubility_gcnn_model, solubility_gcnn_model_version = load_gcnn_model_with_versioninfo(
    solubility_model_file_path, 
    solubility_model_file_url
    )

del solubility_model_file_url
del solubility_model_file_path

print(f'Finished loading Solubility models', file=sys.stdout)