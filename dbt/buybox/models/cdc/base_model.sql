WITH source_data AS (
  SELECT *, current_timestamp() AS last_modified
  FROM {{ source('AIRFLOW', 'BB_Raw_data') }}
)
SELECT *
FROM source_data
