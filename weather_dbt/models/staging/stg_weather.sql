select
    cast(time as timestamp) as observed_at,
    temperature_2m as temperature_c,
    relative_humidity_2m as humidity_pct,
    precipitation as precipitation_mm
from raw.weather