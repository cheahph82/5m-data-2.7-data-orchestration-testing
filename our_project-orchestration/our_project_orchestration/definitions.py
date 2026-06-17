from dagster import (
    Definitions,
    ScheduleDefinition,
    define_asset_job,
    load_assets_from_modules,
)

import our_project_orchestration.assets as assets_module

all_assets = load_assets_from_modules([assets_module])

elt_job = define_asset_job(
    name="daily_elt_pipeline",
    selection="*",
    description="dbt profiling → staging cleaning → validation → star schema"
)

daily_schedule = ScheduleDefinition(
    job=elt_job,
    cron_schedule="*/5 * * * *",
    name="daily_elt_pipeline_schedule",
    description="Run ELT pipeline every 5 minutes"
)

defs = Definitions(
    assets=all_assets,
    jobs=[elt_job],
    schedules=[daily_schedule],
)