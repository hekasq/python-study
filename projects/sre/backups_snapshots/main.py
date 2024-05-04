# Task: write script that snapshots  persistent disks
import api

project = "blz-d-gdp-telemetry"
region = "us-central1"

if __name__ == '__main__':
    # Setup
    disks = []
    count = 0
    zones = api.get_regional_zones(project, region)

    for zone in zones:
        disks_in_zone = api.get_disks(project, zone)
        disks.extend(disks_in_zone)
    print(f"Total disks: {len(disks)}")

    for disk in disks:
        if count == 1:
            exit()
        api.create_snapshot(project, disk)
        count += 1

# Setup
# create GCP client that interacts with persistent storage


# Snapshotting


# use some api to snapshot?
# define SLM (configurable). When? Where to? How often?
# How will this be deployed? Function?
# logging, env vars etc
# monitoring/alerting around Snapshots being taken erroring, logging successes, deletes etc
