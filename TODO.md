# dmist-nnunet-fork TODO List

## In progress

### Dataset training script

- [ ] debug `train_models.py`:
  - errors are probably associated with `"overwrite_image_reader_writer": "NibabelIO"` in the created `"f{dataset_dir}/dataset.json"` file

### Summary report implementation

- [ ] When searching for previous results, be able to handle different segmentation models.

## Completed

### Dataset preprocessing script

- [X] Add command line args for `prepare_dataset.py`, `process_entry.py`, and `create_folds.py`:
  - `input_yaml`: describes contents of dataset
  - `dataset_id`: number id
  - `dataset_desc`: text descriptor (`dataset_name` becomes `f"Dataset{dataset_id}_{dataset_desc}"`)

- [X] Call `create_folds.py` within `prepare_dataset.py`:
  - script to create to create the folds

- [X] Create a function `create_slurm_script_make_folds_plan_and_preprocess` in `prepare_dataset.py` script to submit a second slurm job to create the folds and perform the experiment planning and preprocessing:
  - first slurm job: `"process_entries.py"`
  - second slrum job: `"create_folds.py"` and `nnUNetv2_plan_and_preprocess` command

### nnUNet DICOM catcher

- [X] Send DICOM to Skyline

  - use `/data/irf/ai/DICOM/liver/dcm_48E/RA0212_20180918_DIWB250` as starting point
  - will be sent to `/data/irf/ai/rustadmd/segmentation_data/liver/dcm` on Skyline

- [x] Convert DICOM to NIfTI

  - `/data/irf/ai/rustadmd/dmist-nnunet-fork/irf_scripts/dcm2niix_nnunet_wrapper.sh /data/irf/ai/DICOM/liver/dcm_48E/RA0212_20180918_DIWB250 /data/irf/ai/rustadmd/dmist-nnunet-fork/segmentation_data/tmp`

- [X] Call `irf_scripts/nnUNet_predict_ensemble_pp.py` within `dmist-deploy/seg_driver.sh`

  - `seg_driver.sh` args:
     1. required: `in_dir`, `out_dir`,
     2. need to  be made: new `mode` option (*e.g.* `liver_nnunet`)

  - example call:

     1. `./nnUNet_predict_ensemble_pp.py --input_folder_nii /data/irf/ai/rustadmd/dmist-nnunet-fork/segmentation_data/input_folder_2 --run_dir /data/irf/ai/rustadmd/dmist-nnunet-fork/segmentation_data/liver/RA0212_20180918_DIWB250_3d_fullres_3d_lowres_5 --configs 3d_fullres 3d_lowres`
     2. DEBUG: array predict job files do not loop through the configs properly (two 3d_fullres jobs are created)
- [X] Script to call after predict, ensemble, post-process

  - File I/O
  - Slurm stats using `seff`

- [X] Send prediction to MIM

  1. `/data/irf/ai/rustadmd/dmist-nnunet-fork/irf_scripts/AnalyzeToDicom.py --patid_study_date RA0212_20180918 --dicom_in /data/irf/ai/DICOM/liver/dcm_48E/RA0212_20180918_DIWB250 --nifti_in <NIFTI_PATH> --series_description nnUNetpipeline_Liver_Seg_DL --keep-dicom`

### Misc

- [x] See if I can use a private submodule for custom IRF-specific script files (a forked repo must be kept public).
  
  - All files intended to be saved in `irf_scripts` will now be saved and developed within the private repo [dmist-nnunet](https://github.com/niaid/dmist-nnunet).

- [x] Clean up existing nnUNet run directories

  - Specifically, clean up `/data/irf/ai/rustadmd/nnUNet/runs` which contain copies of the 048E Liver dataset.

- [x] Fix ensemble_job_id value in `./nnUNet_predict_ensemble_pp.py`

  ```bash
  $ ./nnUNet_predict_ensemble_pp.py --input_folder /data/irf/ai/rustadmd/dmist-nnunet-fork/segmentation_data/input_folder --run_dir /data/irf/ai/rustadmd/dmist-nnunet-fork/segmentation_data/liver/RA0212_20180918_DIWB250_3d_fullres_3d_lowres --configs 3d_fullres 3d_lowres

  submit_cmd:
  sbatch --parsable /data/irf/ai/rustadmd/dmist-nnunet-fork/segmentation_data/liver/RA0212_20180918_DIWB250_3d_fullres_3d_lowres/nnUNet_array_predict_3d_fullres.slurm


  job_id:
  523027


  submit_cmd:
  sbatch --parsable /data/irf/ai/rustadmd/dmist-nnunet-fork/segmentation_data/liver/RA0212_20180918_DIWB250_3d_fullres_3d_lowres/nnUNet_array_predict_3d_lowres.slurm


  job_id:
  523028


  ensemble_and_pp_cmd:
  sbatch --dependency=afterok:523027:523028 /data/irf/ai/rustadmd/dmist-nnunet-fork/segmentation_data/liver/RA0212_20180918_DIWB250_3d_fullres_3d_lowres/nnUNet_ensemble_and_pp.slurm


  ensemble_job_id:
  Submitted batch job 523029
  ```
