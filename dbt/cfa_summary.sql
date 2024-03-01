with content as (
        select * from {{ ref('stg_content_data') }}
),

web_scraped as(
        select * from {{ ref('stg_web_scraped_data') }}   
),

source_data as (
        select web_scraped.level,
            web_scraped.year,
            content.title,
            count(web_scraped.topic) as no_of_articles,
            min(length(web_scraped.summary)) as min_length_summary,
            max(length(web_scraped.summary)) as max_length_summary,
            max(length(web_scraped.learning_outcomes)) as min_lenth_learnoutcome,
            min(length(web_scraped.learning_outcomes)) as max_lenth_learnoutcome

        from web_scraped

        join content using (topic)

        group by web_scraped.level,web_scraped.year,content.title

        ORDER BY web_scraped.level, web_scraped.year

    )

select *
from source_data
