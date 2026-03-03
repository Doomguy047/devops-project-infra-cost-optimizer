import json
from rules import check_ec2, check_ebs, check_s3


def analyze_costs():
    with open("sample_data.json") as f:
        data = json.load(f)

    results = []

    results.extend(check_ec2(data["ec2_instances"]))
    results.extend(check_ebs(data["ebs_volumes"]))
    results.extend(check_s3(data["s3_buckets"]))

    return results
