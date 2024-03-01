select
    level,
    year,
    topic,
    summary,
    learning_outcomes

from {{ source('cfa_prod', 'web_scraped_data') }}