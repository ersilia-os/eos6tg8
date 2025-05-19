# Natural product fingerprint

The model uses a combination of two multilayer perceptron networks (baseline and auxiliar) and an autoencoder-like network to extract natural-product specific fingerprints that outperform traditional methods for molecular representation. The training sets correspond to the coconut database (NP) and the Zinc database (synthetic). 

This model was incorporated on 2021-11-03.

## Information
### Identifiers
- **Ersilia Identifier:** `eos6tg8`
- **Slug:** `natural-product-fingerprint`

### Domain
- **Task:** `Representation`
- **Subtask:** `Featurization`
- **Biomedical Area:** `Any`
- **Target Organism:** `Not Applicable`
- **Tags:** `Natural product`, `Fingerprint`, `Descriptor`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `65`
- **Output Consistency:** `Fixed`
- **Interpretation:** Descriptor of a molecule

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| feature_00 | float |  | Feature 0 of the natural product fingerprint |
| feature_01 | float |  | Feature 1 of the natural product fingerprint |
| feature_02 | float |  | Feature 2 of the natural product fingerprint |
| feature_03 | float |  | Feature 3 of the natural product fingerprint |
| feature_04 | float |  | Feature 4 of the natural product fingerprint |
| feature_05 | float |  | Feature 5 of the natural product fingerprint |
| feature_06 | float |  | Feature 6 of the natural product fingerprint |
| feature_07 | float |  | Feature 7 of the natural product fingerprint |
| feature_08 | float |  | Feature 8 of the natural product fingerprint |
| feature_09 | float |  | Feature 9 of the natural product fingerprint |

_10 of 65 columns are shown_
### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos6tg8](https://hub.docker.com/r/ersiliaos/eos6tg8)
- **Docker Architecture:** `AMD64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos6tg8.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos6tg8.zip)

### Resource Consumption
- **Model Size (Mb):** `120`
- **Environment Size (Mb):** `2112`


### References
- **Source Code**: [https://github.com/kochgroup/neural_npfp](https://github.com/kochgroup/neural_npfp)
- **Publication**: [https://www.sciencedirect.com/science/article/pii/S2001037021003226?via%3Dihub#f0010](https://www.sciencedirect.com/science/article/pii/S2001037021003226?via%3Dihub#f0010)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2021`
- **Ersilia Contributor:** [miquelduranfrigola](https://github.com/miquelduranfrigola)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [None](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos6tg8
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos6tg8
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
