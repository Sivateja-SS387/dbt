{{ config(
    materialized='table' 
) }}

SELECT *
FROM {{ source('AIRFLOW', 'BB_Raw_data') }}  
