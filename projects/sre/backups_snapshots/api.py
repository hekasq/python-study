from google.cloud import compute_v1
from datetime import datetime

diskClient = compute_v1.DisksClient()
snapClient = compute_v1.SnapshotsClient()
zonesClient = compute_v1.ZonesClient()
regionClient = compute_v1.RegionsClient()


def get_zones(project):
    try:
        zone_names = []
        zones = zonesClient.list(project=project)
        for zone in zones:
            zone_names.append(zone.name)
        return zone_names
    except Exception as e:
        print(e)


# is this a possible requirement? If so may have to generalize the client api call
def get_regional_zones(project, region):
    try:
        zone_names = []

        request = compute_v1.GetRegionRequest(
            project=project,
            region=region)

        regions = regionClient.get(request)

        for zone in regions.zones:
            zone_names.append(zone.split("/")[-1])
        return zone_names
    except Exception as e:
        print(e)


def get_disks(project, zone):
    try:
        result = diskClient.list(project=project, zone=zone)
        print(f"Fetched {len(result._response.items.pb)} disks from {zone} ")
        return result
    except Exception as e:
        print(e)


def get_disk(project, zone, name):
    try:
        # diskClient.get(project="blz-d-gdp-telemetry", zone="us-central1-a", disk="dev-usc1-es-ccs-blue-data-001")
        diskClient.get(project=project, zone=zone, disk=name)
    except Exception as e:
        print(e)


# does this have bulk api of sorts?
def create_snapshot(project, disk):
    try:
        snapshot = compute_v1.Snapshot()
        snapshot.name = f"evk-{disk.name}-{datetime.now().date()}"
        snapshot.source_disk = disk.self_link
        snapClient.insert(project=project, snapshot_resource=snapshot)
    except Exception as e:
        print(e)


def get_snapshot(project, name):
    result = snapClient.get(project=project, snapshot=name)
