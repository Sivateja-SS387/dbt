"Contains constants used in the DAGs"

from pathlib import Path
from cosmos import ExecutionConfig

buybox_path = Path("/usr/local/airflow/dbt/buybox")
dbt_executable = Path("/usr/local/airflow/dbt_venv/bin/dbt")

venv_execution_config = ExecutionConfig(
    dbt_executable_path=str(dbt_executable),
)
