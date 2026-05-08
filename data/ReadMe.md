# Data preprocessing

- Units standardisation to MWh
- Aggregation to hourly frequency
- Restricted to the common time period 2024-2025
- Aggregation at national level

## Correspondence Entsoe and SFOE columns:

- Hydro Pumped Storage + Hydro Water Reservoir = Speicherkraft
- Hydro Run-of-river and poundage = Flusskraft
- Nuclear = Kernkraft
- Wind Onshore = Wind

- Solar = Photovoltaik --> use data from seperate PV production file

- Thermische --> no correspondence (use 1/24 for hourly)
