# dmist-nnunet-fork TODO List

## In progress

### Training variations

- [ ] [Scale ResEnc nnUNet beyond the presets](https://github.com/MIC-DKFZ/nnUNet/blob/master/documentation/resenc_presets.md#scaling-resenc-nnu-net-beyond-the-presets)
  - set `gpu_memory_target_in_gb = 80`:

      ```bash
      nnUNetv2_plan_experiment -d DATASETID -pl nnUNetPlannerResEncXL -gpu_memory_target 80 -overwrite_plans_name nnUNetResEncUNetPlans_80G
      ```

- [ ] [Scale to multiple GPUs](https://github.com/MIC-DKFZ/nnUNet/blob/master/documentation/resenc_presets.md#scaling-to-multiple-gpus)
  - Run `nnUNetv2_plan_experient` normally (targeting to run on one GPU), and then manually edit the plans file to increase the batch size. You can use [configuration inheritance](https://github.com/MIC-DKFZ/nnUNet/blob/master/documentation/explanation_plans_files.md). In the configurations dictionary of the genereated plans JSON file, add the following entry:

      ```json
      "3d_fullres_bsXX": {
          "inherits_from": "3d_fullres",
          "batch_size": XX
      },
      ```

    Where XX is the new batch size. If 3d_fullres has a batch size of 2 for one GPU and you are planning to scale to 8 GPUs, make the new batch size 2x8=16! You can then train the new configuration using nnU-Net's multi-GPU settings:

      ```bash
      nnUNetv2_train DATASETID 3d_fullres_bsXX FOLD -p nnUNetResEncUNetPlans_80G -num_gpus 8
      ```

### Summary report implementation

- [ ] When searching for previous results, be able to handle different segmentation models.

## Completed

### Dataset preprocessing script

- [X] Make details within generated `./nnUNet_preprocessed/<Dataset>/dataset.json` variable, not hardcoded

- [X] debug `train_models.py`:
  - ~~errors are probably associated with `"overwrite_image_reader_writer": "NibabelIO"` in the created `"f{dataset_dir}/dataset.json"` file~~
  - erros caused by corrupted file/lack of space in `"/data/scratch/rustadmd/ai-hpcgpu19/torchinductor_rustadmd/"`

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
