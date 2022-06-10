# Natural product fingertips

A structural fingerprint based on natural products

| Description | Input  | Output  | Training Data | Experimental Validation |
| ------- | --- | --- | --- | --- |
| Generation of fingerprints for natural products | SMILES | Fingerprints as vectors | 605351 compounds | No |

## Source code
This model is publshed by Janosch Menkea, Joana Massaa & Oliver Koch, Natural product scores and fingerprints extracted from artificial neural networks Received 31 March 2021, Revised 26 July 2021, Accepted 26 July 2021, Available online 30 July 2021, Version of Record 13 September 2021. https://doi.org/10.1016/j.csbj.2021.07.032

Code: https://github.com/kochgroup/neural_npfp

## Extended description
A manually curated dataset of natural products and synthetic decoys was used to train a multi-layer perceptron network and an autoencoder-like network. In-depth analysis showed that the extracted natural product-specific neural fingerprint outperforms traditional as well as natural product-specific fingerprints on three datasets.

### Summary
- Trained using natural products and synthetic molecules
- The output is a fingerprint which encodes the molecular structure into a vector that is readable by the computer
- Trained to distinguish between natural products and synthetic ones

### Specifications
- Input: SMILES string

## History
- Model was downloaded on September 28, 2021
