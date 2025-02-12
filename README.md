# th_execute_sandbox

- [link to repo](https://github.com/tempuslabs/bioinf-rna-onco/pull/244)
- [link to new docker image build](https://concourse.ops.gcp.tempus.cloud/teams/rp/pipelines/rna-fusion-char/jobs/pr-build-image/builds/722)
- [link to transform id registered in bet](https://concourse.ops.gcp.tempus.cloud/teams/rp/pipelines/rna-fusion-char/jobs/pr-register-in-bet/builds/159)


# resources
- [`rna-onco/rna-fusion-char` th-exec input](https://github.com/tempuslabs/bioinf-rna-onco/blob/develop/rna-fusion-char/transformhub/test_rnaonco_fusion_char.json)
- [`splunk to check execution id of th-exec out json](https://tempus.splunkcloud.com/en-US/app/search/cs_transformhub_transforms_by_execution_id?form.timespan.earliest=-24h%40h&form.timespan.latest=now&form.log_type_token=NOT%20loggerName%3Dopt.tempus.transform.harness.node_modules.%40tempus.transformhub-tools.dist.lib.utils.performance-measures&form.log_type_token=NOT%20loggerName%3Dtransformhub.lib.dps.dps-provider&form.severity_token=&form.execution_id=51078d8c-1538-4d92-94ee-c7ee026f2b05)


# information about ticket --> to be transferred to the pull request
- [x] **JIRA ticket**: [BFXA-5715](https://tempuslabs.atlassian.net/jira/software/c/projects/BFXA/boards/1249?assignee=712020%3Afe369597-023a-4144-a1f8-84df1cca7bd4&selectedIssue=BFXA-5715&useStoredSettings=true)
- [x] **th_exec on February 11, 2025**


| sample | th_exec analysis ID | th_exec execution ID | BIPS execution ID | fastq url |
|----------|----------|----------|----------|----------|
| sample7 | agkpnofdprgyrfrbf2ktrhphoy | 5fd12c8f-6096-4226-9f26-df6c757ae25a | 5af27560-06fc-457b-b9c5-d93da5a56875 | gs://tl-bet-sequencer-output-fastq-us/20241208-042436-652760-ef951c740108/24-D37629_RSQ1.tar.gz |
| sample8 | agkpnoelv5cgrmg4of2ibtifhe | 1bd621ff-259f-459b-83e4-862d3b128892 | b6548283-bf1a-4679-ba4f-9a131d8e7d83 | gs://tl-bet-sequencer-output-fastq-us/20241208-042436-652760-ef951c740108/24-D37630_RSQ1.tar.gz |
| sample9 | agkpnogg5ne37cdceob7pwd7iu | c821c8cc-34e4-459b-91c9-bb9a71844487 | e5467cad-74a7-4c12-8d0e-e50a28f1f1b9 | gs://tl-bet-sequencer-output-fastq-us/20241208-042436-652760-ef951c740108/24-D37631_RSQ1.tar.gz |
| sample10 | agkpnohlpfgbpo4vcxaniey4yq | e176172e-57f6-48cf-ab4b-6dcef7c6d54b | | gs://tl-bet-sequencer-output-fastq-us/20241208-042436-652760-ef951c740108/24-D37632_RSQ1.tar.gz |
| sample11 | agkpnoeygne7tio77ohqmchpiu | 04bddba5-2257-46cb-9f57-39e31c81dd5d | 77653e84-d8f0-49b1-a6c7-831e98fa29f5 | gs://tl-bet-sequencer-output-fastq-us/20241208-042436-652760-ef951c740108/24-D37633_RSQ1.tar.gz |
| sample12 | agkpnogspraaribakstwrvgzxe | c04fad18-17bd-43b5-95d8-2c61a742e1d5 | 1a564eb6-6d5b-41ae-ba98-9445d9c039de | gs://tl-bet-sequencer-output-fastq-us/20241208-042436-652760-ef951c740108/24-D37634_RSQ1.tar.gz |
| sample13 | agkpnofpaba45gvam7zcu2nq7a | 17fbf33a-d07e-4ffe-a9c9-129a6905a312 | 5c7e424f-1d12-43ad-9c39-18ad1a1b1e84 | gs://tl-bet-sequencer-output-fastq-us/20241208-042436-652760-ef951c740108/24-D37635_RSQ1.tar.gz |
| sample14 | agkpnof2ozgb3cigflweufqf6m | 44294b02-6bb9-4061-b63e-ee4936c29550 | 3dabeac9-bab7-4e7b-b142-184de83a0f88 | gs://tl-bet-sequencer-output-fastq-us/20241208-042436-652760-ef951c740108/24-D37636_RSQ1.tar.gz |
| sample15 | agkpnog67bcpnpjp7u7vzozmyq | a690156e-8c07-46ba-9172-dd50dff04c63 | c445c7b0-1d9b-4be5-b6ab-4ade839bac1f | gs://tl-bet-sequencer-output-fastq-us/20241208-042436-652760-ef951c740108/24-D37637_RSQ1.tar.gz |
| sample16 | agkpnod64rd33euds3qzdalmv4 | 4e4bb26c-0479-4e23-bd83-195310930dc3 | 1bfc2959-7399-4149-bc44-f2e5c9205503 | gs://tl-bet-sequencer-output-fastq-us/20241208-042436-652760-ef951c740108/24-D37638_RSQ1.tar.gz |
