def check_ec2(instances):
    recommendations = []
    for instance in instances:
        if instance["cpu_usage"] < 10 and instance["state"] == "running":
            recommendations.append(
                f"EC2 {instance['id']} is underutilized. Consider downsizing."
            )
        if instance["state"] == "stopped":
            recommendations.append(
                f"EC2 {instance['id']} is stopped. Consider termination."
            )
    return recommendations


def check_ebs(volumes):
    recommendations = []
    for volume in volumes:
        if not volume["attached"]:
            recommendations.append(
                f"EBS {volume['id']} is unattached. Consider deletion."
            )
    return recommendations


def check_s3(buckets):
    recommendations = []
    for bucket in buckets:
        if not bucket["lifecycle_policy"]:
            recommendations.append(
                f"S3 bucket {bucket['name']} has no lifecycle policy."
            )
        if bucket["public"]:
            recommendations.append(
                f"S3 bucket {bucket['name']} is public. Review access settings."
            )
    return recommendations
