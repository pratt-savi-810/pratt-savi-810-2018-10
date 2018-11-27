import Bikeshare_Functions as Bf

# Run Bikeshare Route Finder with various config.json files
# Load different travel points and save destinations through config.json files

# Note: Only run individually on each config.json file
# - geodatabase lock issue prevents functions from running sequentially

Bf.run_bikeshare_route('config1.json')

# Bf.run_bikeshare_route('config2.json')

# Bf.run_bikeshare_route('config3.json')

# Bf.run_bikeshare_route('config4.json')
