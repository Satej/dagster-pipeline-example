from dagster import define_asset_job, AssetSelection, AssetKey
from ..partitions import monthly_partition, weekly_partition

trips_by_week = AssetSelection.assets("trips_by_week")
adhoc_request = AssetSelection.assets(["adhoc_request"])

adhoc_request_job = define_asset_job(
    name="adhoc_request_job",
    selection=adhoc_request,
)

trip_update_job = define_asset_job(
    name="trip_update_job",
    partitions_def=monthly_partition, # partitions added here
    selection=AssetSelection.all() - trips_by_week - adhoc_request
)

weekly_update_job = define_asset_job(
    name="weekly_update_job",
    selection=trips_by_week,
)

weekly_update_job = define_asset_job(
    name="weekly_update_job",
    partitions_def=weekly_partition,
    selection=trips_by_week,
)
