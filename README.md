# Natural product fingerprint

The model uses a combination of two multilayer perceptron networks (baseline and auxiliar) and an autoencoder-like network to extract natural-product specific fingerprints that outperform traditional methods for molecular representation. The training sets correspond to the coconut database (NP) and the Zinc database (synthetic). 

## Identifiers

* EOS model ID: `eos6tg8`
* Slug: `natural-product-fingerprint`

## Characteristics

* Input: `Compound`
* Input Shape: `Single`
* Task: `Representation`
* Output: `Descriptor`
* Output Type: `String`
* Output Shape: `List`
* Interpretation: Descriptor of a molecule

## References

* [Publication](https://www.sciencedirect.com/science/article/pii/S2001037021003226?via%3Dihub#f0010)
* [Source Code](https://github.com/kochgroup/neural_npfp)
* Ersilia contributor: [miquelduranfrigola](https://github.com/miquelduranfrigola)

## Citation

If you use this model, please cite the [original authors](https://www.sciencedirect.com/science/article/pii/S2001037021003226?via%3Dihub#f0010) of the model and the [Ersilia Model Hub](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff).

## License

This package is licensed under a GPL-3.0 license. The model contained within this package is licensed under a None license.

Notice: Ersilia grants access to these models 'as is' provided by the original authors, please refer to the original code repository and/or publication if you use the model in your research.

## About Us

The [Ersilia Open Source Initiative](https://ersilia.io) is a Non Profit Organization ([1192266](https://register-of-charities.charitycommission.gov.uk/charity-search/-/charity-details/5170657/full-print)) with the mission is to equip labs, universities and clinics in LMIC with AI/ML tools for infectious disease research.

[Help us](https://www.ersilia.io/donate) achieve our mission!