# dmist-nnunet-fork TODO list

1. See if I can use a private submodule for custom IRF-specific script files (a forked repo must be kept public).
   
    - for now, all files intended to be saved in `irf_scripts` will be saved/developed within the private repo [dmist-nnunet](https://github.com/niaid/dmist-nnunet)

2. nnUNet DICOM catcher

   - use `irf_scripts/inference_ensembling_postprocessing_job_template.job` as template job file for an inference task

3. Dataset preprocessing script (ensure IRF datasets are nnUNet-compatible)
4. Clean-up existing nnUNet run directories (in `/data/irf/ai/rustadmd/nnUNet/runs`) which contain copies of the 048E Liver dataset

