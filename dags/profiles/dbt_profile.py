from datetime import datetime

from cosmos import DbtDag, ProjectConfig, ProfileConfig

from include.constants import buybox_path, venv_execution_config

dbt_profile_example = DbtDag(
    # dbt/cosmos-specific parameters
    project_config=ProjectConfig(buybox_path),
    profile_config=ProfileConfig(
        # these map to dbt/buybox_path/profiles.yml
        profile_name="buy_box",
        target_name="dev",
        profiles_yml_filepath=buybox_path / "profiles.yml",
    ),
    execution_config=venv_execution_config,
    # normal dag parameters
    schedule_interval="@daily",
    start_date=datetime(2023, 1, 1),
    catchup=False,
    dag_id="dbt_profile_example",
    task_id="sivatejab",
    tags=["profiles"],
)
