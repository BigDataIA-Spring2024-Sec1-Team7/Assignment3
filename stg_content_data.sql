select
    title,
    topic
from {{ source('cfa_prod', 'content_data') }}