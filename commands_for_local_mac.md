# Data data_download

python 01-fetch_taxon_keys.py \
--species_filepath uksi-macro-moths.csv \
--column_name taxon \
--output_filepath uksi-macro-moths-keys.csv \
--place london31May2023


python 02-fetch_gbif_moth_data.py \
--write_directory /Users/lbokeria/Documents/projects/gbif-species-trainer-AMI-fork/data_download/output_data/gbif_data_uksi_macro_moths_small_try/  \
--dwca_file /Users/lbokeria/Downloads/0001402-230530130749713.zip \
--species_checklist /Users/lbokeria/Documents/projects/gbif-species-trainer-AMI-fork/data_download/uksi-macro-moths-small-try-keys.csv \
--max_images_per_species 10 \
--resume_session True 

For erebidae: 
python 02-fetch_gbif_moth_data.py \
--write_directory /Users/lbokeria/Documents/projects/gbif-species-trainer-AMI-fork/data_download/output_data/gbif_data_uksi_macro_moths_small_try_Erebidae/  \
--dwca_file /Users/lbokeria/Downloads/erebidae.zip \
--species_checklist /Users/lbokeria/Documents/projects/gbif-species-trainer-AMI-fork/data_download/uksi-macro-moths-small-try-keys-erebidae-amata-phegea.csv \
--max_images_per_species 2 \
--resume_session False 

Serial:
python 02-fetch_gbif_moth_data_serial.py \
--write_directory /Users/lbokeria/Documents/projects/gbif-species-trainer-AMI-fork/data_download/output_data/gbif_data_uksi_macro_moths_small_try_Erebidae/  \
--dwca_file /Users/lbokeria/Downloads/erebidae.zip \
--species_checklist /Users/lbokeria/Documents/projects/gbif-species-trainer-AMI-fork/data_download/uksi-macro-moths-small-try-keys-erebidae-amata-phegea.csv \
--max_images_per_species 2 \
--resume_session False 

Serial with sesiidae:

python 02-fetch_gbif_moth_data_serial.py \
--write_directory /Users/lbokeria/Documents/projects/gbif-species-trainer-data/gbif_images/drepanidae/  \
--dwca_file /Users/lbokeria/Documents/projects/gbif-species-trainer-data/dwca_files/drepanidae.zip \
--species_checklist /Users/lbokeria/Documents/projects/gbif-species-trainer-AMI-fork/data_download/uksi-macro-moths-keys.csv \
--max_images_per_species 2 \
--resume_session False

## Wrapper for downloading data

python 02-fetch_gbif_moth_data_wrapper.py \
--write_directory_lists /Users/lbokeria/Documents/projects/gbif-species-trainer-AMI-fork/data_download/  \
--write_directory_images /Users/lbokeria/Documents/projects/gbif-species-trainer-data/gbif_images/sandbox/  \
--dwca_directory /Users/lbokeria/Documents/projects/gbif-species-trainer-data/dwca_files/ \
--species_checklist /Users/lbokeria/Documents/projects/gbif-species-trainer-AMI-fork/data_download/uksi-macro-moths-keys.csv \
--max_images_per_species 2 \
--resume_session False \
--family_name Sesiidae



## Update the data stats 

python 03-update_data_statistics.py \
--data_directory /Users/lbokeria/Documents/projects/gbif-species-trainer-data/gbif_images/sandbox/ \
--species_checklist /Users/lbokeria/Documents/projects/gbif-species-trainer-AMI-fork/data_download/uksi-macro-moths-keys.csv



# Model training 

python 01-create_dataset_split.py \
--root_dir /Users/lbokeria/Documents/projects/gbif-species-trainer-data/gbif_images/try_wrapper/ \
--write_dir /Users/lbokeria/Documents/projects/gbif-species-trainer-AMI-fork/model_training/data/ \
--species_checklist /Users/lbokeria/Documents/projects/gbif-species-trainer-AMI-fork/data_download/uksi-macro-moths-drepanidae-sesiidae-limacodidae-keys.csv \
--train_ratio 0.75 \
--val_ratio 0.10 \
--test_ratio 0.15 \
--filename 01-uksi

python 02-calculate_taxa_statistics.py \
--species_checklist /Users/lbokeria/Documents/projects/gbif-species-trainer-AMI-fork/data_download/uksi-macro-moths-drepanidae-sesiidae-limacodidae-keys.csv \
--write_dir /Users/lbokeria/Documents/projects/gbif-species-trainer-AMI-fork/model_training/data/ \
--numeric_labels_filename uksi_numeric_labels_07Aug2023 \
--category_map_filename uksi_category_map_07Aug2023 \
--taxon_hierarchy_filename uksi_taxon_hierarchy_07Aug2023 \
--training_points_filename uksi_count_training_points_07Aug2023 \
--train_split_file /Users/lbokeria/Documents/projects/gbif-species-trainer-AMI-fork/model_training/data/01-uksi_train-split.csv

Creating the webdatasets: 

Train set 
python 03-create_webdataset.py \
--dataset_dir /Users/lbokeria/Documents/projects/gbif-species-trainer-data/gbif_images/try_wrapper/ \
--dataset_filepath /Users/lbokeria/Documents/projects/gbif-species-trainer-AMI-fork/model_training/data/01-uksi_train-split.csv \
--label_filepath /Users/lbokeria/Documents/projects/gbif-species-trainer-AMI-fork/model_training/data/uksi_numeric_labels_07Aug2023.json \
--image_resize 300 \
--webdataset_patern "/Users/lbokeria/Documents/projects/gbif-species-trainer-AMI-fork/model_training/train/train-500-%06d.tar" 

Validation set 
python 03-create_webdataset.py \
--dataset_dir /Users/lbokeria/Documents/projects/gbif-species-trainer-data/gbif_images/try_wrapper/ \
--dataset_filepath /Users/lbokeria/Documents/projects/gbif-species-trainer-AMI-fork/model_training/data/01-uksi_val-split.csv \
--label_filepath /Users/lbokeria/Documents/projects/gbif-species-trainer-AMI-fork/model_training/data/uksi_numeric_labels_07Aug2023.json \
--image_resize 300 \
--webdataset_patern "/Users/lbokeria/Documents/projects/gbif-species-trainer-AMI-fork/model_training/val/val-500-%06d.tar" 

Test set 
python 03-create_webdataset.py \
--dataset_dir /Users/lbokeria/Documents/projects/gbif-species-trainer-data/gbif_images/try_wrapper/ \
--dataset_filepath /Users/lbokeria/Documents/projects/gbif-species-trainer-AMI-fork/model_training/data/01-uksi_test-split.csv \
--label_filepath /Users/lbokeria/Documents/projects/gbif-species-trainer-AMI-fork/model_training/data/uksi_numeric_labels_07Aug2023.json \
--image_resize 300 \
--webdataset_patern "/Users/lbokeria/Documents/projects/gbif-species-trainer-AMI-fork/model_training/test/test-500-%06d.tar"



python 04-train_model.py \
--train_webdataset_url "/Users/lbokeria/Documents/projects/gbif-species-trainer-AMI-fork/model_training/train/train-500-{000000..00002}.tar" \
--val_webdataset_url "/Users/lbokeria/Documents/projects/gbif-species-trainer-AMI-fork/model_training/val/val-500-{000000..000000}.tar" \
--test_webdataset_url "/Users/lbokeria/Documents/projects/gbif-species-trainer-AMI-fork/model_training/test/test-500-{000000..000000}.tar" \
--config_file config/01-config_uksi_resnet50.json \
--dataloader_num_workers 6