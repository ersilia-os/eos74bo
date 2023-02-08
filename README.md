# **Kinetic Aqueous Solubility**

## **Model identifiers**
- Slug: solubility
- Ersilia ID: eos74bo
- Tags: solubility
#
## **Model description**
<p align="justify">
Aqueous Solubility refers to the solubility of a pure substance or solute in a solvent. It measures the maximum concentration of a substance that can be completely dissolved in an aqueous medium at a certain temperature and pressure level. 
</p>
<p align="justify">
A drug needs to dissolve and achieve the desired concentration to produce a desirable pharmacological response. Drugs that have poor aqueous solubility have a slower drug absorption rate, which can lead to inadequate and variable bioavailability, and render the drug ineffective. Poor solubility of drugs also leads to other issues, such as challenges with metabolism or permeability, interactions with other drugs or the need to extend drug release. 
</p>
<p align="justify">
This data was provided by the National Center for Advancing Translational Sciences (NCATS). A probability of below 0.5 is considered high soluility. Probability of 0.5 or greater is considered low solubility. 
</p>

- Input: SMILES
- Output: SMILES

#
## **Source code**

Cite the source publication
[Predictive models of aqueous solubility of organic compounds built on A large dataset of high integrity](https://pubmed.ncbi.nlm.nih.gov/31176566/)

- Code: [NCATS-ADME](https://github.com/ncats/ncats-adme.git)
- Checkpoints: include the link to the checkpoints used if model is a pretrained model
#
## **License**
GNU General Public License v3.0.

## **History**
- The model was incorporated into Ersilia on the 22th of January, 2023.
- Modifications to the original code.
    1. Removal of Flask functionalities and dependencies.
    2. Striping unused functions from the original code.

- To run the model, follow these [steps](model/README.md).

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission or [volunteer](https://www.ersilia.io/volunteer) with us!
