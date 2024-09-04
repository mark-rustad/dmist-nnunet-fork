# dmist-nnunet-fork TODO List

- [x] See if I can use a private submodule for custom IRF-specific script files (a forked repo must be kept public).
  
  - All files intended to be saved in `irf_scripts` will now be saved and developed within the private repo [dmist-nnunet](https://github.com/niaid/dmist-nnunet).

- [ ] nnUNet DICOM catcher

  - Use `irf_scripts/inference_ensembling_postprocessing_job_template.job` as a template job file for an inference task.

- [ ] Dataset preprocessing script

  - Ensure IRF datasets are nnUNet-compatible.

- [ ] Clean up existing nnUNet run directories

  - Specifically, clean up `/data/irf/ai/rustadmd/nnUNet/runs` which contain copies of the 048E Liver dataset.
