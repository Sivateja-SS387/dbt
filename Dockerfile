FROM quay.io/astronomer/astro-runtime:11.3.0

# Install dbt into a virtual environment
RUN python -m venv dbt_venv && \
    . dbt_venv/bin/activate && \
    pip install --no-cache-dir dbt-snowflake==1.5.4 && \
    deactivate

# Set a connection to the Airflow metadata DB to use for testing
ENV AIRFLOW_CONN_AIRFLOW_METADATA_DB=snowflake://Sivateja2001:Sivateja#2003@uyb42629.us-east-1.aws/AIRFLOW/dev?warehouse=COMPUTE_WH

# sql_alchemy_conn = snowflake://Sivateja2001:Sivateja#2003@pk18845.us-east-2.aws/AIRFLOW/dev?warehouse=COMPUTE_WH
