# Lake Nasser MODIS Image Time Series Project

## Project Overview

This project utilizes Google Earth Engine (GEE) and MODIS satellite data to analyze and visualize changes around Lake Nasser over time. It generates a time series of satellite images, processes them to create a video, and creates a GIF that shows changes in the region over the years. The goal is to visualize environmental changes using satellite imagery data from 2000 to 2023.

## Requirements

Before running the project, ensure that the following dependencies are installed:

- Python 3.x
- Google Earth Engine (GEE) API
- geemap library
- pandas
- numpy
- os
- datetime

You can install the required libraries using the following pip commands:

```bash
pip install pandas numpy geemap earthengine-api

Setup and Authentication
Step 1: Earth Engine Authentication

To authenticate with Google Earth Engine (GEE), use the following command:

import ee
ee.Authenticate()
ee.Initialize(project='#')

This will open a link in your browser, where you need to sign in and paste the authentication token back into the command line.
Step 2: Configure Project Parameters

The project script defines the location of Lake Nasser, the time range from 2000 to 2023, and a list of MODIS satellite image collections.

The location of Lake Nasser is set using the following coordinates:

    Latitude: 22.833
    Longitude: 32.500

Project Description

    Image Collection: The script collects MODIS images from the MODIS/061/MOD09GA dataset, focusing on the RGB bands (sur_refl_b02, sur_refl_b04, sur_refl_b03), over the specified geographical region (Lake Nasser area) and time range.

    Time Series Creation: The script then generates a time series of these images, covering the period from 2000-01-01 to 2023-08-01. The images are processed with predefined visual parameters to enhance the image quality.

    GIF Generation: The script generates a GIF that visualizes the changes over time by showing the images sequentially with date labels.

    Saving Results: All generated images and the final GIF are saved to the specified output directory.

Usage

    Clone or download the project repository.
    Modify the out_dir and other directory paths as per your system.
    Run the Python script to authenticate and process the satellite images.
    Once the script runs successfully, it will create the GIF showing the changes around Lake Nasser over time.

GIF Visualization

The GIF generated in this project shows the environmental changes around Lake Nasser from 2000 to 2023. Here is a preview of the generated GIF:

Conclusion

This project provides a powerful way to visualize and analyze environmental changes over a large area, leveraging satellite imagery and Google Earth Engine's data processing capabilities. The generated GIF offers a visual representation of how the region has changed over the years, providing insights into long-term environmental trends.
