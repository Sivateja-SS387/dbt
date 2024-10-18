from datetime import datetime

from cosmos import DbtDag, ProjectConfig, RenderConfig

from include.profiles import buy_box
from include.constants import buybox_path, venv_execution_config

only_seeds = DbtDag(
    project_config=ProjectConfig(buybox_path),
    profile_config=buy_box,
    execution_config=venv_execution_config,
    # new render config
    render_config=RenderConfig(
        select=["path:seeds"],
    ),
    # normal dag parameters
    schedule_interval=None,
    start_date=datetime(2023, 1, 1),
    catchup=False,
    dag_id="only_seeds",
    task_id="sivatejaa",
    tags=["filtering"],
)














# from datetime import datetime
# from cosmos import DbtDag, ProjectConfig, RenderConfig, BashOperator

# from include.profiles import buy_box
# from include.constants import buybox_path, venv_execution_config

# only_seeds = DbtDag(
#     project_config=ProjectConfig(buybox_path),
#     profile_config=buy_box,
#     execution_config=venv_execution_config,
#     render_config=RenderConfig(
#         select=["path:seeds"],
#         select=["path:models"],
#     ),
#     schedule_interval=None,
#     start_date=datetime(2023, 1, 1),
#     catchup=False,
#     dag_id="only_seeds",
#     tags=["filtering"],
# )

# run_base_model = BashOperator(
#     task_id='run_base_model',
#     bash_command='cd /path/to/your/dbt/project && dbt run --models base_model',
#     dag=only_seeds,
# )

# run_combined_model = BashOperator(
#     task_id='run_combined_model',
#     bash_command='cd /path/to/your/dbt/project && dbt run --models combined_buybox_model',
#     dag=only_seeds,
# )

# run_base_model >> run_combined_model
