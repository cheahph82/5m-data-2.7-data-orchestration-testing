# definitions.py
from dagster import (
    Definitions,
    ScheduleDefinition,
    define_asset_job,
    load_assets_from_modules,
    PipesSubprocessClient, # 1. Import the client
)
import meltano_orchestration.assets as assets_module

all_assets = load_assets_from_modules([assets_module])

elt_job = define_asset_job(
    name="daily_elt_pipeline",
    selection="*",
    description="Meltano extraction → dbt transformation → data quality tests"
)

daily_schedule = ScheduleDefinition(
    job=elt_job,
    cron_schedule="0 2 * * *",
    name="daily_elt_schedule",
    description="Daily resale data pipeline"
)

defs = Definitions(
    assets=all_assets,
    jobs=[elt_job],
    schedules=[daily_schedule],
    # 2. Add the resource here
    resources={
        "pipes_subprocess_client": PipesSubprocessClient(),
    },
)
