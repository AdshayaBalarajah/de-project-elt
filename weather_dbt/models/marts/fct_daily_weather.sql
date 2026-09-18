select
    date_trunc('day', observed_at) as day,
    round(avg(temperature_c), 1) as avg_temp_c,
    round(max(temperature_c), 1) as max_temp_c,
    round(avg(humidity_pct), 1) as avg_humidity_pct,
    round(sum(precipitation_mm), 1) as total_precipitation_mm
from {{ ref('stg_weather') }}
group by 1
order by 1