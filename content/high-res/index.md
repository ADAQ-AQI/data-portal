---
title: High Resolution Modelling
...

# A kilometre-scale air quality model for the UK

As part of the Clean Air SPF, the Met Office is developing a new
kilometre-scale air quality model. The Met Office provides the UK
national air quality forecast using a numerical model that operates on a
12x12 km^2^ grid. This is much larger than the typical length scales on
which pollutant concentrations vary in the atmosphere and is
significantly coarser than the current UK weather prediction model that
operates on the kilometre-scale. The aim of this project is to develop a
new UK-wide air quality model on a 2.2 km and/or a 1.5 km grid. This
will be in line with existing operational Met Office numerical weather
prediction models.

Increasing the resolution of the air quality model to the
kilometre-scale will:

- better represent atmospheric processes, such as explicitly resolving
  convection, and better resolve surface features (e.g. orography)
  that will improve surface interactions (e.g. deposition of
  pollutants to the surface)

- benefit from emissions datasets that are available at higher
  resolution, such as the National Atmospheric Emissions Inventory
  that provides national emissions data at 1x1 km^2^ resolution

- better resolve pollutant concentration gradients in the rural and
  urban background environment, particularly important for short-lived
  pollutants

- provide boundary and initial conditions required by very
  high-resolution (100-metre scale) urban air quality models.

The emissions of primary pollutants are a primary factor in determining
local air quality. The figures below illustrate the improvement in the
spatial representation of emissions when using a 2.2 km grid compared
with a 12 km grid. The figures show the annual mean emissions of nitric
oxide (NO) over the UK and Ireland. The higher-resolution grid better
resolves the main road networks, a major source of NO.

: NO emissions

+------------------------------------+------------------------------------+
| 2.2 km                             | 12 km                              |
+====================================+====================================+
| ![](high-res/NO_aqeur.png){        | ![](high-res/NO_aquk.png){         |
| width=100%}                        | width=100%}                        |
+------------------------------------+------------------------------------+

# Applications of the new higher-resolution model

A kilometre-scale air quality model has not been routinely used for the
UK and this new capability will be used to answer several open
questions:

- what are the impacts of using a convection-permitting model on
  surface concentrations of pollutants?

- how do we treat emissions (both spatially and temporally) in a
  higher-resolution model and what are the impacts of resolving
  finer-scale emissions?

- how do we deal with verification of the model against observations
  at higher-resolutions?

- what are the costs-benefits of using different spatial resolutions
  (e.g. 12 km vs 2.2 km vs 1.5 km)?

The model developed in this project will be used to tackle a variety of
open scientific questions in air quality as well as inform development
of the next-generation Met Office air quality forecast model.

# Early results from the new model configuration

A preliminary configuration of the new model at 2.2 km resolution was
run for a single day -- 2^nd^ May 2018 -- and compared with the 12 km
model. The figures below compare the surface daily-mean surface mass
fractions of ozone (O~3~) and nitrogen dioxide (NO~2~) and demonstrate
the first-order effects of increasing the spatial resolution of the
model.

For both pollutants, more fine-scale features are apparent in the 2.2 km
model, compared with the lower resolution model. The concentration of
the short-lived pollutant NO~2~ is well correlated with its emission (of
NO). This illustrative the improved representation of the urban-rural
concentration gradient in the higher-resolution model for short-lived
pollutants.

: Ozone

+------------------------------------+------------------------------------+
| ![](high-res/aqum_O3.png){         | ![](high-res/aquk_O3.png){         |
| width=100%}                        | width=100%}                        |
+------------------------------------+------------------------------------+

: Nitrogen dioxide (NO~2~)

+------------------------------------+------------------------------------+
| ![](high-res/aqum_NO2.png){        | ![](high-res/aquk_NO2.png){        |
| width=100%}                        | width=100%}                        |
+------------------------------------+------------------------------------+
