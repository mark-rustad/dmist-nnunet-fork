# DMIST-nnUNet Integration

This repository is a fork of the [nnU-Net](https://github.com/MIC-DKFZ/nnUNet) framework. Our goal is to integrate nnU-Net’s powerful automated segmentation capabilities within DMIST (Deep-learning Medical Image Segmentation Toolbox).

- [dmist-train](https://github.com/niaid/dmist-train): toolbox for training
- [dmist-deploy](https://github.com/niaid/dmist-deploy): toolbox for pipeline implementation

### Key Objectives

- **Integrate custom data preprocessing scripts** to create our own nnUNet-compatible IRF imaging datasets.
- **Deploy nnUNet models trained on IRF imaging datasets** for segmentation tasks.

## About nnU-Net

nnU-Net is an automated deep learning-based segmentation framework that adapts itself to the characteristics of any given dataset. Originally developed for the biomedical domain, nnU-Net’s flexibility and out-of-the-box performance make it an ideal starting point for custom applications.

### Key Features of nnU-Net

- **Automated Configuration**: Automatically configures segmentation pipelines tailored to the dataset, with minimal need for expert intervention.
- **Versatility**: Handles 2D and 3D data, with support for various input modalities and voxel spacings.
- **Proven Performance**: Recognized as a top performer in numerous medical imaging challenges, consistently delivering state-of-the-art results.

For more details on the original nnU-Net, please refer to the [official documentation](https://github.com/MIC-DKFZ/nnUNet).

## Custom Modifications

### 1. Custom Scripts

We have developed a series of custom scripts to extend nnU-Net’s functionality for infectious disease research. These include:

- **Preprocessing scripts** tailored to specific imaging modalities and datasets commonly used in our research.
- **SLURM job file creation and management** to perform inference, ensembling, and postprocessing tasks on [Skyline](https://skyline.niaid.nih.gov/) HPC.

### 2. New Pipelines and Configurations

Integrate our custom scripts within the existing dmist-deploy framework.

### 3. Integration with Organizational Infrastructure

Integrate these tools within NIH/NIAID/IRF organizational infrastructure.

## Getting Started

To use our custom version of nnU-Net, follow these steps:

1. **Clone the Repository**:

   ```bash
   git clone git@github.com:mark-rustad/dmist-nnunet-fork.git
   cd nnUNet
   ```

2. **Create a conda environment (using conda/mamba/micromamba) using the environment specification file `nnunet_env_v1.yml`**:

   ```bash
   micromamba create -n <env_name> -f ./nnunet_env_v1.yml
   ```

   Refer to nnUNet's installation instructions in the `documentation/installation_instructions.md` file for additional environment setup information.

3. **Set Up Your Dataset**:
   Convert your dataset into the nnU-Net format as described in the [Dataset Conversion Guide](documentation/dataset_format.md).

4. **Run Custom Pipelines**:
   Use our custom scripts and configurations to train and evaluate models. Refer to our documentation for specific command-line instructions tailored to infectious disease research workflows.

## Documentation

- [Installation Instructions](documentation/installation_instructions.md)
- [Custom Scripts and Pipelines](documentation/custom_pipelines.md) - *TODO:Detailed instructions on using our custom scripts and configurations.*
- [Usage Instructions](documentation/how_to_use_nnunet.md)
- [Extending nnU-Net](documentation/extending_nnunet.md)

## Acknowledgements

This work builds upon the original nnU-Net framework developed by the [Applied Computer Vision Lab (ACVL)](http://helmholtz-imaging.de) and the [Division of Medical Image Computing](https://www.dkfz.de/en/mic/index.php) at the [German Cancer Research Center (DKFZ)](https://www.dkfz.de/en/index.html).

We extend our thanks to the original authors and the broader community for their contributions to this exceptional framework.

## Citation

If you use this fork in your research, please also cite the original nnU-Net paper:

Isensee, F., Jaeger, P. F., Kohl, S. A., Petersen, J., & Maier-Hein, K. H. (2021). nnU-Net: a self-configuring method for deep learning-based biomedical image segmentation. Nature methods, 18(2), 203-211.

---

For questions, contributions, or feedback, please contact Mark Rustad at <mark.rustad@nih.gov>.
