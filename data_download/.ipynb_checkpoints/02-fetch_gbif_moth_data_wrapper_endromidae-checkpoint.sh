#!/bin/bash
#SBATCH --account vjgo8416-amber
#SBATCH --qos turing
#SBATCH --time 02:00:00
#SBATCH --nodes 1
#SBATCH --cpus-per-task 36
#SBATCH --mem=10G

# Module loading
module purge # unloads and loaded modules and resets the environment
module load baskerville # loads the default Baskerville environment 
module load bask-apps/live # load the stable, default application stack
module load Miniconda3/4.10.3 # load the Conda package manager

set -e # exit immediately if there is an error
eval "$(${EBROOTMINICONDA3}/bin/conda shell.bash hook)" # initialise Conda

# export CONDA_ENV_NAME="/bask/homes/r/rybf4168/.conda/envs/gbif_species_trainer"

export CONDA_ENV_PATH="/bask/projects/v/vjgo8416-amber/conda_envs/gbif-species-trainer-AMI-fork"

# Activate the environment
conda activate "${CONDA_ENV_PATH}"

# Execute your python programme
python 02-fetch_gbif_moth_data_wrapper.py \
--write_directory_lists /bask/projects/v/vjgo8416-amber/projects/gbif-species-trainer-AMI-fork/data_download/  \
--write_directory_images /bask/projects/v/vjgo8416-amber/data/gbif-species-trainer-AMI-fork/gbif_images/try_wrapper/  \
--dwca_directory /bask/projects/v/vjgo8416-amber/data/gbif-species-trainer-AMI-fork/dwca_files/ \
--species_checklist /bask/projects/v/vjgo8416-amber/projects/gbif-species-trainer-AMI-fork/data_download/uksi-macro-moths-keys.csv \
--max_images_per_species 1000 \
--resume_session False \
--family_name Endromidae