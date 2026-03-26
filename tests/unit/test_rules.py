import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src/main")))

from rules import check_ec2, check_ebs, check_s3


def test_ec2_underutilized():
    instances = [{"id": "i-001", "cpu_usage": 5, "state": "running"}]
    result = check_ec2(instances)
    assert "underutilized" in result[0]


def test_ebs_unattached():
    volumes = [{"id": "vol-001", "attached": False}]
    result = check_ebs(volumes)
    assert "unattached" in result[0]


def test_s3_issue():
    buckets = [{"name": "test", "lifecycle_policy": False, "public": True}]
    result = check_s3(buckets)
    assert len(result) > 0
