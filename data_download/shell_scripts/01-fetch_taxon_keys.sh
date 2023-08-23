#!/bin/bash
#SBATCH --account vjgo8416-amber
#SBATCH --qos turing
#SBATCH --time 01:00:00
#SBATCH --nodes 1
#SBATCH --gpus 1
#SBATCH --cpus-per-gpu 36

# Module loading
module purge # unloads and loaded modules and resets the environment
module load baskerville # loads the default Baskerville environment 
module load bask-apps/live # load the stable, default application stack
module load Miniconda3/4.10.3 # load the Conda package manager

set -e # exit immediately if there is an error
eval "$(${EBROOTMINICONDA3}/bin/conda shell.bash hook)" # initialise Conda

export CONDA_ENV_NAME="gbif_species_trainer"

# Activate the environment
conda activate gbif_species_trainer

# Execute your python programme

python 01-fetch_taxon_keys.py \
--species_filepath uksi-macro-moths.csv \
--column_name taxon \
--output_filepath uksi-macro-moths-keys2.csv \
--place london07June2023

# python 02-fetch_gbif_moth_data.py \
# --write_directory /bask/projects/v/vjgo8416-amber/projects/gbif-species-trainer-AMI-fork/data_download/output_data/gbif_data_uksi_macro_moths_small_try/  \
# --dwca_file /bask/projects/v/vjgo8416-amber/data/gbif-species-trainer-AMI-fork/0001402-230530130749713.zip \
# --species_checklist bask/projects/v/vjgo8416-amber/projects/gbif-species-trainer-AMI-fork/uksi-macro-moths-small-try-keys.csv \
# --max_images_per_species 2 \
# --resume_session True 