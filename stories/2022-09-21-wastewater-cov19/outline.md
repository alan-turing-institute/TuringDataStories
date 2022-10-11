# Data sources

-   [Waste Water
    Data](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1049734/Final_EMHP_Wastewater_Data_January_2022.ods)
-   Need to use [Metrics
    documentation](https://coronavirus.data.gov.uk/metrics/name) in
    order to understand!
-   Going to correlate with [data.gov
    link](https://api.coronavirus.data.gov.uk/v2/data?areaType=region&metric=newCasesByPublishDate&metric=newCasesLFDOnlyBySpecimenDate&metric=newOnsDeathsByRegistrationDate&metric=newPeopleVaccinatedFirstDoseByPublishDate&metric=newCasesPCROnlyBySpecimenDate&format=csv)
-   Population states
    [ONS](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/populationestimates/datasets/populationestimatesforukenglandandwalesscotlandandnorthernireland)
    -   This is already included in the waste water data!
-   GeoJson for UK [datalink](https://martinjc.github.io/UK-GeoJSON/)
-   Sooooo the water data links quite nicely to the UK (old) EU election
    mappings for regions:
    [dataset](https://hub.arcgis.com/datasets/ons::european-electoral-regions-december-2017-uk-buc/explore?location=51.637964%2C0.216908%2C6.51)

# Ideas

## Use number of positive tests 
- Consider this with respect to number of tests done

## Could we use plotly to make a nice Choropleth plots?

### Plotly also has other language bindings

### We could hopefully make some nice temporal plots too?

## Decide to do this entire exercise in Julia/R/Python

### Personally, I\'m leaning towards Julia just to have an excuse to learn it

### Though, if time is an issue /and/or for prototyping I may just use python

## To make everything easier I\'d suggest two things

1.  Use England data only (sorry UK, as usual England is obviously the
    ONLY country in the UK)
2.  Use regions as a scope.
    1.  This kinda ignores a lot of the data which is within the water
        data
    2.  But possibly, if there\'s time and space we could do a more in
        depth view for one region
    3.  For example, I\'m *sure* we can find some geo data for London
        districts and show if there\'s much variability between regions
        vs districts
    4.  This could also build a good argument for if we need to have
        more refined data or is region a sweetspot (hypothesis being
        that it\'s prob better to be more specific)
    5.  Can see an issue with this being that if we did this in a high
        density area such as london then it would be more homogeneous
        that somewhere like Yorkshire which is less densely populated.

## Could do like a Voronoi mapping of place locations and build our own geojson files?
## Possibly could also calculate population per area, samples per area, etc.


# Flow

## Explain how we actually started with making these maps
- Where did we get data and how did we organise it 

## Exploring Wastewater data

### What is the data

### How often is it collected, how variable is it and where is it collected

This also serves as a nice way of introducing the spatial-temporal

### These data with respect to populations?

## COVID monitoring [^1]

### Explore and explain the COVID19 data

### Shouldn\'t need too much about this, most people are familiar with the cases curves

### Again, break down by region with map plots

## Questions to explore:

### Can you see a correlation on covid19 gene copies per litre in wastewater with population

-   We\'d need a way to calculate density of the area covered

[^1]: Given that **many** $^{\textrm{citation needed}}$ people are
    likely exhausted with reading and hearing about COVID would it be an
    idea to put a spin on this to \"learning from this pandemic\'s data
    in order to make the next one easier?\" Or is that too much?
