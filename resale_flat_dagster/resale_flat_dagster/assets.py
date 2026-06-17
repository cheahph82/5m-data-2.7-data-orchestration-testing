from dagster import AssetExecutionContext
from dagster_dbt import DbtCliResource, dbt_assets

from .project import resale_flat_project


@dbt_assets(manifest=resale_flat_project.manifest_path)
def resale_flat_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()
    