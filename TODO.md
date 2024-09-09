# dmist-nnunet-fork TODO List

- [x] See if I can use a private submodule for custom IRF-specific script files (a forked repo must be kept public).
  
  - All files intended to be saved in `irf_scripts` will now be saved and developed within the private repo [dmist-nnunet](https://github.com/niaid/dmist-nnunet).

- [ ] nnUNet DICOM catcher

  - Steps:

    1. Send DICOM to Skyline
       1. use `/data/irf/ai/DICOM/liver/dcm_48E/RA0212_20180918_DIWB250` as starting point
    2. Convert DICOM to NIfTI
    3. Call `irf_scripts/nnUNet_predict_ensemble_pp.py`
       1. `./nnUNet_predict_ensemble_pp.py --input_folder /data/irf/ai/rustadmd/dmist-nnunet-fork/segmentation_data/input_folder --run_dir /data/irf/ai/rustadmd/dmist-nnunet-fork/segmentation_data/liver/RA0212_20180918_DIWB250 --configs 2d 3d_fullres 3d_lowres 3d_cascade_fullres`
       2. `./nnUNet_predict_ensemble_pp.py --input_folder /data/irf/ai/rustadmd/dmist-nnunet-fork/segmentation_data/input_folder --run_dir /data/irf/ai/rustadmd/dmist-nnunet-fork/segmentation_data/liver/RA0212_20180918_DIWB250_3d_fullres_3d_lowres --configs 3d_fullres 3d_lowres`
    4. Send prediction to MIM
       1. `/data/irf/ai/rustadmd/dmist-nnunet-fork/irf_scripts/AnalyzeToDicom.py --patid_study_date RA0212_20180918 --dicom_in /data/irf/ai/DICOM/liver/dcm_48E/RA0212_20180918_DIWB250 --nifti_in <NIFTI_PATH> --series_description nnUNetpipeline_Liver_Seg_DL --keep-dicom`

- [ ] Fix ensemble_job_id value in `./nnUNet_predict_ensemble_pp.py`

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

- [ ] Dataset preprocessing script

  - Ensure IRF datasets are nnUNet-compatible.

- [ ] Clean up existing nnUNet run directories

  - Specifically, clean up `/data/irf/ai/rustadmd/nnUNet/runs` which contain copies of the 048E Liver dataset.
