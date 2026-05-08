# Energy Data Hackdays 2026 Lausanne: Estimating hourly power production

SFOE Challenge for the Energy Data Hackdays 2026 Lausanne. 

### Challenge Pitch Presentation 
![Slide 2](ChallengeDesign_BFE_LAU26/Folie2.PNG)
![Slide 2](ChallengeDesign_BFE_LAU26/Folie3.PNG)
![Slide 2](ChallengeDesign_BFE_LAU26/Folie4.PNG)

### Additional Data Sources:
- PV Production csv:     [bfe-ogd.ch/backcast_data_export.csv](https://www.uvek-gis.admin.ch/BFE/ogd/temp/backcast_data_export.csv)
- PV Production parquet: [www.bfe-ogdch/backcast_data_export.pq](https://www.uvek-gis.admin.ch/BFE/ogd/temp/backcast_data_export.pq)
- [ENTSOE](https://transparency.entsoe.eu/) & https://github.com/EnergieID/entsoe-py

### Compute & storage on Renku:
- https://renkulab.io/p/lucs/energy-data-hackdays-lausanne-2026

### Methods:

#### Chow-Lin (tempdisagg): 
Disaggregates low-frequency series (daily → hourly) using a high-frequency indicator and AR(1) residual modeling. Ensures hourly estimates sum back to original daily totals.

https://github.com/jaimevera1107/tempdisagg

#### Kalman Filter
State-space approach that recursively estimates hourly production by combining a process model with noisy observations. Updates predictions as new data arrives, naturally handling missing values and measurement uncertainty.

https://arxiv.org/pdf/1710.04055

#### Simple scaling
Distributes daily totals to hourly values proportionally using a known hourly profile. Each hour gets a share of the daily total based on the indicator's relative weight within that day.