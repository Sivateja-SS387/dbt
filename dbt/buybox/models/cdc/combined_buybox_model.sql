{{ config(
    materialized='incremental',  
    unique_key='message_id'  
) }}

WITH new_data AS (
    SELECT *
    FROM {{ ref('base_model') }}  
),

existing_data AS (
    SELECT *
    FROM {{ source('AIRFLOW', 'BB_Raw_data') }}  
)

SELECT *
FROM existing_data

UNION ALL

SELECT *
FROM new_data

{% if is_incremental() %}
WHERE last_modified > (SELECT MAX(last_modified) FROM {{ this }}) 
{% endif %}
