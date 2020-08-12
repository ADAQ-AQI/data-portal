---
title: MOCCA
...

# Project Overview

Whilst aerosol and gaseous pollutants in the UK are generally well
observed at the surface, and column averaged information is increasingly
available from satellite observations, there remains limited data on the
vertical distribution of key pollutants in the UK boundary layer. This
information is needed to support air quality model development and
evaluation.

The Met Office Clean Air project aims to address this gap by collecting
regular airborne measurements over the Southern UK for a period of 1 to
2 years using the **Met Office Civil Contingencies Aircraft (MOCCA)**.
MOCCA is an instrumented Cessna-421 and is on 24/7 standby to respond to
a volcanic ash related civil contingencies event. The aircraft is
operated by the Met Office Observational Based Research (OBR) group on
behalf of the Civil Aviation Authority (CAA).

As well as an existing suite of aerosol/ash detecting instruments, the
MOCCA has now also been instrumented to allow additional measurements of
aerosol and gaseous pollutants for the Met Office Clean Air Project,
part of the wider Met Office Air Quality programme. Airborne
observations will take place approximately every 3 in 4 weeks, weather
permitting, over the duration of the project, culminating at
approximately 15 hours per month.

The key pollutants for observation are **PM~2.5~**, **PM~10~**,
**NO~2~**, **SO~2~** and **O~3~**, which will be measured using the
following instrumentation:

- [Cavity Attenuated Phase Shift (CAPS) NO~2~ Monitor](<https://metoffice.sharepoint.com/sites/moobrcleanairprojext/SitePages/Cavity-Attenuated-Phase-Shift-NO2-Monitor-(CAPS-NO2).aspx>)

- [Portable Optical Particle Spectrometer (POPS)](<https://metoffice.sharepoint.com/sites/moobrcleanairprojext/SitePages/Portable-Optical-Particle-Counter.aspx>)

- [Tricolour Absorption Photometer (TAP)](<https://metoffice.sharepoint.com/sites/moobrcleanairprojext/SitePages/Tricolor-Absorption-Photometer.aspx>)

- [Nephelometer](<https://metoffice.sharepoint.com/sites/moobrcleanairprojext/SitePages/Nephelometer.aspx>)

- [Droplet Measurement Technologies Cloud and Aerosol Particle Spectrometer (DMT CAPS)](<https://metoffice.sharepoint.com/sites/moobrcleanairprojext/SitePages/Cloud,-Aerosol-and-Precipitation-Spectrometer.aspx>)

- [2B Technologies Ozone Monitor](<https://metoffice.sharepoint.com/sites/moobrcleanairprojext/SitePages/2B-Tech-Ozone.aspx>)

- [SO~2~ analyser](<https://metoffice.sharepoint.com/sites/moobrcleanairprojext/SitePages/SO2.aspx>)

- [Position data and basic meteorology](<https://metoffice.sharepoint.com/sites/moobrcleanairprojext/SitePages/AIMMS.aspx>)

# Flight Planning

The flight planning process involves considering a number of different
[sortie options](mocca#flight-sorties) as well as a number of [flight pattern
techniques](mocca#flight-techniques).

## Flight Sorties

### Ground Network Survey

::: flexrow
![](mocca/sortie-1.png)

- **What**: Survey flight in coordination with ground based monitoring
sites which could also include missed approaches to sample the full
boundary layer.

- **Why**: Coordination with ground based sites provides both surface
measurements and higher altitude measurements for evaluating the model.

- **When**: Under any conditions.
:::

### South Coast Survey

::: flexrow
![](mocca/sortie-2.png)

- **What**: Route along the south coast between Exeter and Eastbourne,
coordinated with overpassing ground based monitoring sites.

- **Why**: Enables the contribution of continental pollution to UK air
quality to be assessed.

- **When**: Under background conditions and when southerly winds bring
polluted air from the continent.
:::

### City Scale Flux

::: flexrow
![](mocca/sortie-3.png)

- **What**: Circular flights around large cities or urban areas.

- **Why**: To measure the conditions upwind and downwind of a city to
identify the flux of emissions from the city.

- **When**: Under background conditions and under settled conditions
when dispersion of pollution is minimised, and concentrations are
allowed to accumulate.
:::

### High Density Special Mapping

::: flexrow
![](mocca/sortie-4.png)

- **What**: Intensive grid box scale sampling over urban areas.

- **Why**: To assess the spatial variability of concentrations in high
pollution conditions.

- **When**: Under background conditions and under settled conditions
when dispersion of pollution is minimised, and concentrations are
allowed to accumulate.
:::

### Targeted Events

::: flexrow
![](mocca/sortie-5.png)

- **What**: Route targeting areas experiencing specific air quality
episodes, coordinated with overpassing ground based monitoring sites.

- **Why**: Enables measurements of concentrations during specific
episodes to be recorded.

- **When**: Under episode conditions such as continental plumes or dust
events.
:::

## Flight Techniques

### Level Flying

::: flexrow
![](mocca/pattern-1.png)

- **Benefits**: Provides information about the spatial changes in
concentrations across large areas at a given altitude, unlike ground
based monitoring which only provides surface level information.

- **Challenges**: Airspace limitations may prevent a constant altitude
being maintained and may limit the altitude range in which the aircraft
may fly.
:::

### Stacked Profiles

::: flexrow
![](mocca/pattern-2.png)

- **Benefits**: Enables vertical changes in concentrations to be
measured across a given sector, such as the downwind sector of a
plume from a city.

- **Challenges**: Airspace limitations may restrict the range of
altitudes which the profiling legs can be flown at.
:::

### Saw Tooth

::: flexrow
![](mocca/pattern-3.png)

- **Benefits**: Enables vertical changes in concentrations to be
measured.

- **Challenges**: The rate of ascent and descent may be too fast for
enough measurements to be made at each altitude in order to get a
sufficient signal to noise ratio.
:::

### Missed Approach

::: flexrow
![](mocca/pattern-4.png)

- **Benefits**: Enables the aircraft to descend below the Civil
Aviation Authority standard minimum altitude of 1000ft and obtain
vertical profile information about concentrations below this altitude.

- **Challenges**: Emissions from the airfield or from other aircraft
taking off or landing could interfere with the concentrations recorded,
making the measurements unrepresentative of typical background
concentrations at these altitudes.
:::

### Grid Box

::: flexrow
![](mocca/pattern-5.png)

- **Benefits**: Provides information on how concentrations change
spatially across a relatively small area (a city) with many different
sources of emissions.

- **Challenges**: Airspace restrictions prevent low level grid flying
over some of the large urban areas, such as London.
:::

# Data Files

*M###* refers to the flight number. We currently only have data for
M251 (although it must be noted that this data is not yet in its final
format as full quality control of the data has not taken place and the
reformatting of the file into NetCDF has not taken place.

## MOCCA Data

The MOCCA data is currently created by combining the raw instrument data
into a single CSV file.

- **Aircraft_Data_M###.csv**

  This is a CSV file containing the aircraft observations. The data is
  available on a 1 second time step. Data includes position of the
  aircraft (latitude, longitude, altitude, pressure), aircraft
  parameters (pitch, roll, TAS), meteorological parameters (wind speed
  and direction, temperature, relative humidity) and pollutant
  concentrations (NO2, O3 and SO2).

## AQUM Data

This is data currently extracted from the archived 3-hourly
operational data files. Data has been extracted for the time step
closest to the flight time, although the method of selecting time
slices and converting data from a rotated pole grid and then
extracting flight coordinates is in need of checking and updating –
the model data should only be treated as an example and no conclusions
should be made based upon this data.

- **AQUM\_Flight\_Track\_Data\_M\#\#\#.csv**

  This is a CSV file containing model data extracted along the
  latitude-longitude-altitude coordinates of the flight track.

- **AQUM\_Flight\_Track\_Column\_Data\_M\#\#\#.nc**

  This is a NetCDF file containing model data for the whole column along
  the latitude-longitude coordinates of the flight track

## AURN Data

This is AURN ground based measurement data for the day and time of the
flight. This includes all sites which were reporting data on the
flight day. For each of these sites, the data is extracted and
averaged between the take-off and landing times.

The following files are currently available for the AURN sites:

- **CO_AURN_Data_M###.csv**

- **NO_AURN_Data_M###.csv**

- **NO2_AURN_Data_M###.csv**

- **SO2_AURN_Data_M###.csv**

- **O3_AURN_Data_M###.csv**

- **PM2p5_AURN_Data_M###.csv**

- **PM10_AURN_Data_M###.csv**

- **C5H8_AURN_Data_M###.csv**
