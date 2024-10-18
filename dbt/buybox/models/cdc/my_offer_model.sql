
WITH source_data AS (
    SELECT parse_json(message_body) AS raw_data
    FROM {{ ref('raw_buybox') }}
),flatten_payload as (
    select 
        raw_data:"NotificationMetadata"::Object:"NotificationId"::STRING as NotificationId
    from source_data
)
SELECT * FROM flatten_payload