from dagster import asset
import subprocess

DBT_PROJECT_DIR = "/home/cheahph/DS5-Team-5---Module-2-Assignment-Project/our_project"


@asset
def dbt_profiling():
    subprocess.run(
        ["dbt", "run", "--select", "data_profiling"],
        cwd=DBT_PROJECT_DIR,
        check=True
    )


@asset(deps=[dbt_profiling])
def dbt_staging_cleaning():
    subprocess.run(
        ["dbt", "run", "--select", "staging_cleaning"],
        cwd=DBT_PROJECT_DIR,
        check=True
    )


@asset(deps=[dbt_staging_cleaning])
def dbt_validation():
    subprocess.run(
        ["dbt", "build", "--select", "data_validation"],
        cwd=DBT_PROJECT_DIR,
        check=True
    )


@asset(deps=[dbt_validation])
def dbt_star_schema():
    subprocess.run(
        ["dbt", "build", "--select", "star_schema"],
        cwd=DBT_PROJECT_DIR,
        check=True
    )

# # assets.py
# from dagster import asset, AssetExecutionContext, PipesSubprocessClient

# @asset
# def pipeline_meltano(context: AssetExecutionContext, pipes_subprocess_client: PipesSubprocessClient):
#     """
#     Runs meltano using Dagster Pipes for better logging and observability.
#     """
#     return pipes_subprocess_client.run(
#         command=["meltano", "run", "tap-postgres", "target-bigquery"],
#         context=context,
#         cwd = '/home/cheahph/5m-data-2.6-data-pipelines-orchestration/meltano-resale'
#     ).get_results()

# @asset(deps=[pipeline_meltano])
# def pipeline_dbt_run(context: AssetExecutionContext, pipes_subprocess_client: PipesSubprocessClient):
#     """
#     Runs dbt build using Dagster Pipes.
#     """
#     return pipes_subprocess_client.run(
#         command=["dbt", "build"],
#         context=context,
#         cwd = '/home/cheahph/5m-data-2.6-data-pipelines-orchestration/resale_flat'
#     ).get_results()