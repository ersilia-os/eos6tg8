# Natural product fingerprint

Produces a 64-value fingerprint tuned to natural product character, read from the last hidden layer of a feed-forward network trained to tell natural products from synthetic molecules, and returns the natural product score itself as the first column. Menke and colleagues trained it on 394,939 COCONUT natural products against 210,412 ZINC decoys, and report that the extracted representation beats ECFP4 and the natural-product-specific NC_MFP on their screening benchmarks. Dimensions are learned, so none maps onto a defined chemical group.

This model was incorporated on 2021-11-03.Last packaged on 2026-09-01.

## Information
### Identifiers
- **Ersilia Identifier:** `eos6tg8`
- **Slug:** `natural-product-fingerprint`

### Domain
- **Task:** `Representation`
- **Subtask:** `Featurization`
- **Biomedical Area:** `Any`
- **Target Organism:** `Any`
- **Tags:** `Natural product`, `Fingerprint`, `Descriptor`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `65`
- **Output Consistency:** `Fixed`
- **Interpretation:** Natural product score followed by the 64 learned fingerprint features from the same network.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| feat_00 | float |  | Feature 0 of the natural product fingerprint |
| feat_01 | float |  | Feature 1 of the natural product fingerprint |
| feat_02 | float |  | Feature 2 of the natural product fingerprint |
| feat_03 | float |  | Feature 3 of the natural product fingerprint |
| feat_04 | float |  | Feature 4 of the natural product fingerprint |
| feat_05 | float |  | Feature 5 of the natural product fingerprint |
| feat_06 | float |  | Feature 6 of the natural product fingerprint |
| feat_07 | float |  | Feature 7 of the natural product fingerprint |
| feat_08 | float |  | Feature 8 of the natural product fingerprint |
| feat_09 | float |  | Feature 9 of the natural product fingerprint |

_10 of 65 columns are shown_
### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`
- **DockerHub**: [https://hub.docker.com/r/ersiliaos/eos6tg8](https://hub.docker.com/r/ersiliaos/eos6tg8)
- **Docker Architecture:** `AMD64`, `ARM64`
- **S3 Storage**: [https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos6tg8.zip](https://ersilia-models-zipped.s3.eu-central-1.amazonaws.com/eos6tg8.zip)

### Resource Consumption
- **Model Size (Mb):** `120`
- **Environment Size (Mb):** `1144`
- **Image Size (Mb):** `1310.39`

**Computational Performance (seconds):**
- 10 inputs: `25.39`
- 100 inputs: `15.33`
- 10000 inputs: `70.99`

### References
- **Source Code**: [https://github.com/kochgroup/neural_npfp](https://github.com/kochgroup/neural_npfp)
- **Publication**: [https://doi.org/10.1016/j.csbj.2021.07.032](https://doi.org/10.1016/j.csbj.2021.07.032)
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
