# Natural-product-fingerprints

Natural product fingerprints

| Description | Input  | Output  | Training Data | Experimental Validation |
| ------- | --- | --- | --- | --- |
| A structural fingerprint based on natural products | SMILES | Fingerprints as vectors | 605,351 compounds | No |

## Source code
This model is publshed by Janosch Menke, Joana Massa, Oliver Koch. Natural product scores and fingerprints extracted from artificial neural networks. *Computational and Structural Biotechnology Journal*, Volume 19, 2021, Pages 4593-4602, ISSN 2001-0370, DOI: [https://doi.org/10.1016/j.csbj.2021.07.032](https://www.sciencedirect.com/science/article/pii/S2001037021003226)

Code: https://github.com/kochgroup/neural_npfp

## Extended description
A manually curated dataset of natural products and synthetic decoys was used to train this model. 

### Summary
- Trained using natural products and synthetic molecules
- The output is a fingerprint which encodes molecular structure into vectors
- Trained to distinguish between natural products and synthetic ones

### Specifications
- Input: SMILES string
- Output: fingerproints as vectors

## History
- Model was downloaded on September 28, 2021
