# Before running th_execute for testing
Likely you are making some changes to the stack and need to run a th_exec or th_adapter to test the changes. Here are some steps to follow to get the data you need to run the tests.

## docker
```
## pull docker image and give it a name
docker pull <us-docker.pkd.dev/transform-v1-artifact-register/docker/...:pr-abcdefghijklmnopqrstuvwxyz> --platform linux/amd64
docker tag <us-docker.pkd.dev/transform-v1-artifact-register/docker/...:pr-abcdefghijklmnopqrstuvwxyz> rna-project-name:date
docker rmi <us-docker.pkd.dev/transform-v1-artifact-register/docker/...:pr-abcdefghijklmnopqrstuvwxyz>

docker run --platform linux/amd64 -it --entrypoint /bin/bash <image-id> 
--> can add -v /path/to/local/data:/opt/tempus/transform/bin/data to mount data
```
- open VSCode and connect to the container with "_Attach to Running Container_"
- develop and test in the container
- go to the PR page and choose "draft PR"
- wait for tests to run. wash, rinse, repeat.

## run unit tests
```
python -m unittest project.submodule.tests.unit.scripts.test_script
```

## install new libraries
```
pip install <library>
pip freeze | grep "library" # to get version that is installed

poetry add <libarary=version.0.0>
```
- do NOT run `poetry update` or `poetry lock` or `poetry install` as it will update all libraries and likely ruin the lock file.
- copy the content of the lock file to the local repo and commit it
- copy the content of the toml file to the local repo and commit it
- push the changes to the repo

# register in beta
- follow the link on the PR to the concourse pipeline
- _login_
- click "pull-request"
- click "pr-register-in-bet"
- check that commits align with the changes you expect to see
- click "trigger a new build"
- wait for the tests to run
- follow put: transform-resource-bet to get the transform id (bottom of page)

# running th_execute
## th_execute: one sample
```
python3,
    -m bioinf_analysis_utils.orch.th_execute,
    --input-path input_json/sampleA.json
    --output-path output_json/sampleA.json
```

## th_adapter: many samples
```
python3,
    --input_csv input_csv.csv
    --input_path input_json/
    --output_path output_json/
```

### input CSV
- **order_id**: orderhub_id --> mostly used for naming purposes and keeping track of files
- **tumor_fastq_archive**: url to fastq file
- **cancer_type**: e.g. _Tumor of Unknown Origin_
- **workflow**: look under _transformhub_ in the repo (e.g. `bioinf-rna-onco/rna-fusion.char/transformhub/tempus_rna_fusion.json`)
- **assay**: RNA-onco.v1 or RS.v2
- **docker_image**(_optional_): Dockerfile --> `JANE_DEFAULT_WORKFLOW=...` OR `pyproject.toml='...'`
- **do_upload_to_cloud**: TRUE
- **transform_id**: new transform id that is being tested (from concourse)
- **rnfd-annotated-fusions-collapsed-intermediate_dpID**: this a dp for each sample, and will be different for each sample. `dps search -m analysis-id=agj3dc4vfbbkviesmpdxdchbrq --type=rnfd-annotated-fusions-collapsed-intermediate` --> look for latest version, knowing the difference between ldt (runs automaticallly) and xr-IVD. then look at the `id` field in the top (not metadata)
- **rnfd-reportable-fusion-reference-criterion_dpID**: this is a dp for the reference, and should be applied to all samples. `dps search --type rnfd-reportable-fusion-reference-criterion` --> "id": xxx-xxx...

