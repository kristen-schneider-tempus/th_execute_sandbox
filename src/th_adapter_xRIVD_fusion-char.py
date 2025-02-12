"""
Creates input.json files in input_json dir for th_exec
Runs th_exec for each sample
Output is saved in output_json directory

to run:
python th_adapter_xRIVD_fusion-char.py
    --input_csv kristen_th_adapter_input.csv
    --input_dir input_json
    --output_dir output_json

"""

import argparse
import json
import os
import subprocess
import sys
import time

import pandas as pd

# sample input json file
TH_EXEC_JSON_FORMAT = {
        "data_product_manifests": {},
        "data_products": {
            "rnfd-annotated-fusions-collapsed-intermediate": {
                "type": "data-product",
                "dpId": "f1dce23e-0ef9-4168-9591-51502ac94930" # must be included in CSV --> use dps search to get this data type ID
            },
            "rnfd-reportable-fusion-reference-criterion": {
                "type": "data-product",
                "dpId": "63fb4532-27ec-4b31-be07-6393d97a9c42" # must be included in CSV --> reference (same for all samples)
            }
        },
        "environment": {
            "CONFIG": {
                "analysis_id": "af5x6zkvcbhufg73iyrdj5bxra", # this is overwritten
                "assay": "RNA-onco.v1", # must be included in CSV
                "cancer_type": "Tumor of Unknown Origin", # must be included in CSV
                "data_product_storage_bucket": "tsc-bioinf-data-products-staging-usw2",
                "cloud_destination": "gs://tl-bet-bioinf-analysis-complete-us",
                "tumor_fastq_archive": "gs://tl-bet-sequencer-output-fastq-us/20240301-100933-103736-140e4745f111/24-A20352_RSQ1.tar.gz", # must be included in CSV
                "do_upload_data_products": "true",
                "log_formatter": "json",
                "order_id": "ewsr1_test", # must be included in CSV
                "slack_error_channel": "bio_jane_error_staging",
                "slack_info_channel": "bio_jane_staging",
                "token": "bioinformatics",
                "tumor_purity_pathology": "21",
                "workflow": "rna_fusion_char" # must be included in CSV
            }
        },
        "parameters": {},
        "transform_id": "0d33c1f1-6541-49e4-91bd-f4626bc6dd03"
    }

def parse_args():
    '''
    Parse command line arguments
    '''
    parser = argparse.ArgumentParser(description="Run th_exec for each sample")
    parser.add_argument(
        "--input_csv",
        type=str,
        required=True,
        help="Input csv file with sample information",
    )
    parser.add_argument(
        "--input_dir",
        type=str,
        default="input_json",
        help="Input directory for json files",
    )
    parser.add_argument(
        "--output_dir",
        type=str,
        default="output_json",
        help="Output directory for json files",
    )

    return parser.parse_args()


def main():
    args = parse_args()
    input_csv_file = args.input_csv
    input_dir = args.input_dir
    output_dir = args.output_dir

    # check if input csv file exists
    if not os.path.exists(input_csv_file):
        print(f"Input csv file {input_csv_file} does not exist!")
        sys.exit(1)

    # check if input directory exists, if not create it
    if not os.path.exists(input_dir):
        os.mkdir(input_dir)
        
    # read in csv file
    input_csv_df = pd.read_csv(input_csv_file)
    
    # create an empty list to save input json file names
    input_json_name_list = []
    
    # create input json files
    # one for each row of csv
    for i in range(len(input_csv_df)):
        temp_input_json_data = TH_EXEC_JSON_FORMAT
        
        temp_input_json_data["transform_id"] = input_csv_df.loc[i, "transform_id"]
        temp_input_json_data["environment"]["CONFIG"]["order_id"] = input_csv_df.loc[i, "order_id"]
        temp_input_json_data["environment"]["CONFIG"]["tarball"] = input_csv_df.loc[i, "order_id"]
    #    temp_input_json_data["environment"]["CONFIG"]["ref_bucket"] = input_csv.loc[i, "ref_bucket"]
        temp_input_json_data["environment"]["CONFIG"]["tumor_fastq_archive"] = input_csv_df.loc[
            i, "tumor_fastq_archive"
        ]
    #   temp_input_json_data["environment"]["CONFIG"]["normal_fastq_archive"] = input_csv.loc[
    #       i, "normal_fastq_archive"
    #   ]
    #   temp_input_json_data["environment"]["CONFIG"]["docker_image"] = input_csv.loc[
    #       i, "docker_image"
    #   ]
        temp_input_json_data["environment"]["CONFIG"]["workflow"] = input_csv_df.loc[i, "workflow"]
        temp_input_json_data["environment"]["CONFIG"]["cancer_type"] = input_csv_df.loc[i, "cancer_type"]
        temp_input_json_data["environment"]["CONFIG"]["assay"] = input_csv_df.loc[i, "assay"]
        temp_input_json_data["data_products"]["rnfd-reportable-fusion-reference-criterion"]["dpId"] = input_csv_df.loc[i, "rnfd-reportable-fusion-reference-criterion_dpID"]
        temp_input_json_data["data_products"]["rnfd-annotated-fusions-collapsed-intermediate"]["dpId"] = input_csv_df.loc[i, "rnfd-annotated-fusions-collapsed-intermediate_dpID"]  
        temp_input_json_data = [temp_input_json_data]
        json_string = json.dumps(temp_input_json_data)
        name = input_csv_df.loc[i, "order_id"]
        input_json_name_list.append("./input_json/%s.json" % name)
        with open("./input_json/%s.json" % name, "w") as outfile:
            outfile.write(json_string)

    # check if output directory exists, if not create it
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

#############




# create a directory to save output json files
if not os.path.exists("output_json"):
    os.mkdir("output_json")

# launch each sample and save output to output_json
for filename in input_json_name_list:
    subprocess.run(
        [
            "python3",
            "-m",
            "bioinf_analysis_utils.orch.th_execute",
            "--input-path",
            filename,
            "--output-path",
            "output_json/%s" % filename.split("/")[-1], # write to out dir and name output file with similar naming convention as input
        ]
    )
    time.sleep(1)
