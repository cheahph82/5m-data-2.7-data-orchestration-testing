from pathlib import Path

from dagster_dbt import DbtProject

resale_flat_project = DbtProject(
    project_dir=Path(__file__).joinpath("..", "..", "..", "..", "5m-data-2.6-data-pipelines-orchestration", "resale_flat").resolve(),
    packaged_project_dir=Path(__file__).joinpath("..", "..", "dbt-project").resolve(),
)
resale_flat_project.prepare_if_dev()