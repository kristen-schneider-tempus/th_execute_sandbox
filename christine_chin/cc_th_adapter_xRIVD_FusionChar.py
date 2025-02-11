"""
Create input.json for th_exec to run samples in batch for xt-onco val run

python3 th_adapter.py input.csv

"""

import json
import os
import subprocess
import sys
import time

import pandas as pd

# Check if the input csv file exists
if len(sys.argv) < 2 or (not sys.argv[1].endswith("csv")):
    print("Please provide the input csv file on the command line!")
    sys.exit(1)

# sample input json file
data = {
        "data_product_manifests": {},
        "data_products": {
            "rnfd-annotated-fusions-collapsed-intermediate": {
                "type": "data-product",
                "dpId": "f1dce23e-0ef9-4168-9591-51502ac94930"
            },
            "rnfd-reportable-fusion-reference-criterion": {
                "type": "data-product",
                "dpId": "63fb4532-27ec-4b31-be07-6393d97a9c42"
            }
        },
        "environment": {
            "CONFIG": {
                "analysis_id": "af5x6zkvcbhufg73iyrdj5bxra",
                "assay": "RNA-onco.v1",
                "cancer_type": "Tumor of Unknown Origin",
                "data_product_storage_bucket": "tsc-bioinf-data-products-staging-usw2",
                "cloud_destination": "gs://tl-bet-bioinf-analysis-complete-us",
                "tumor_fastq_archive": "gs://tl-bet-sequencer-output-fastq-us/20240301-100933-103736-140e4745f111/24-A20352_RSQ1.tar.gz",
                "do_upload_data_products": "true",
                "log_formatter": "json",
                "order_id": "ewsr1_test",
                "slack_error_channel": "bio_jane_error_staging",
                "slack_info_channel": "bio_jane_staging",
                "token": "bioinformatics",
                "tumor_purity_pathology": "21",
                "workflow": "rna_fusion_char"
            }
        },
        "parameters": {},
        "transform_id": "0d33c1f1-6541-49e4-91bd-f4626bc6dd03"
    }

# create a directory to save input json files
if not os.path.exists("input_json"):
    os.mkdir("input_json")

# read in csv files
input_csv = pd.read_csv(sys.argv[1])

# create an empty list to save input json file names
json_name_list = []

# create json files for each row of csv
for i in range(len(input_csv)):
    temp_data = data
    temp_data["transform_id"] = input_csv.loc[i, "transform_id"]
    temp_data["environment"]["CONFIG"]["order_id"] = input_csv.loc[i, "order_id"]
    temp_data["environment"]["CONFIG"]["tarball"] = input_csv.loc[i, "order_id"]
#    temp_data["environment"]["CONFIG"]["ref_bucket"] = input_csv.loc[i, "ref_bucket"]
    temp_data["environment"]["CONFIG"]["tumor_fastq_archive"] = input_csv.loc[
        i, "tumor_fastq_archive"
    ]
 #   temp_data["environment"]["CONFIG"]["normal_fastq_archive"] = input_csv.loc[
 #       i, "normal_fastq_archive"
 #   ]
 #   temp_data["environment"]["CONFIG"]["docker_image"] = input_csv.loc[
 #       i, "docker_image"
 #   ]
    temp_data["environment"]["CONFIG"]["workflow"] = input_csv.loc[i, "workflow"]
    temp_data["environment"]["CONFIG"]["cancer_type"] = input_csv.loc[i, "cancer_type"]
    temp_data["environment"]["CONFIG"]["assay"] = input_csv.loc[i, "assay"]
    temp_data["data_products"]["rnfd-reportable-fusion-reference-criterion"]["dpId"] = input_csv.loc[i, "rnfd-reportable-fusion-reference-criterion_dpID"]
    temp_data["data_products"]["rnfd-annotated-fusions-collapsed-intermediate"]["dpId"] = input_csv.loc[i, "rnfd-annotated-fusions-collapsed-intermediate_dpID"]  
    temp_data = [temp_data]
    json_string = json.dumps(temp_data)
    name = input_csv.loc[i, "order_id"]
    json_name_list.append("./input_json/%s.json" % name)
    with open("./input_json/%s.json" % name, "w") as outfile:
        outfile.write(json_string)

# create a directory to save output json files
if not os.path.exists("output_json"):
    os.mkdir("output_json")

# launch each sample and save output to output_json
for filename in json_name_list:
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
