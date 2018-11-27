from census import Census
import pandas as pd
from us import states
from read_config_json import read_config


api_key = read_config('census.json')['api_key']


def get_census_tract_acs_data_for_state(
        your_api_key,
        acs_field_name,
        state_abbrev,
        out_csv,
):
    c = Census(your_api_key)
    pd.DataFrame(
        c.acs5.state_county_tract(
            acs_field_name,
            state_abbrev.fips,
            '*',
            '*',
        )
    ).to_csv(out_csv, index=False)


get_census_tract_acs_data_for_state(api_key, 'B01003_001E', states.NY, 'ny_state_acs_pop_est.csv')
