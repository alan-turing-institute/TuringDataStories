# Data 

- Wastewater data is available from [UK Government](https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1049734/Final_EMHP_Wastewater_Data_January_2022.ods)
- Geodata uses the ArcGIS hub UK [GEOJSON region map](https://hub.arcgis.com/datasets/ons::european-electoral-regions-december-2017-uk-buc/explore?location=51.637964%2C0.216908%2C6.51)
- SARS2-COVID19 data is made available by the [UK government](https://api.coronavirus.data.gov.uk/v2/data?areaType=region&metric=newCasesByPublishDate&metric=newCasesLFDOnlyBySpecimenDate&metric=newOnsDeathsByRegistrationDate&metric=newPeopleVaccinatedFirstDoseByPublishDate&metric=newCasesPCROnlyBySpecimenDate&format=csv)
  - Also available per NHS region - TODO: is this more useful?
  - Data was combined using pandas and made into single csv's to reduce number
    of files on ghub 
- Rainfall data, the MET data for this is a bit of a pain. They conflate data
  between Wales and England for some regions, for example. Directly comparing to
  current setup may be tricky...
  - [map here](https://www.metoffice.gov.uk/research/climate/maps-and-data/about/districts-map)
  - Data also needs a little cleaned. It says TSV but the formatting is terrible
  - I converted the data from metoffice, which comes in txt files using this regex:
    - `([\s]{2,})`


## Cleaning the Met office rainfall data
The met provides data in a strange txt format and uses multiple spaces between
data to indicate columns, this is inconsistent and annoying to read. Thus, we
provide a small script to initially clean this data. It can be found and run
from the 'rainfall' data folder. It is placed below also for completeness. 

```python
import re 
from glob import glob 
regex = r"([\s]{2,})" # match anything with more than 2 spaces
subst = ","
files = glob("./*.txt")

for file in files:
    with open(file) as f:
        data = f.readlines()
    # some data has extra lines of information before data
    # so we need to find it... 
    crop = 0
    for l in data:
        if 'year' not in l:
            crop=crop+1
        else:
            break
    for idx, ln in enumerate(data[crop:]):
        data[crop+idx] =  re.sub(regex, subst, ln, 0)       
    nn = f"{file.replace('txt','cleaned_.csv')}"
    with open(nn, 'w') as nf:
        nf.writelines(data[crop:])

```

## Main libraries and softwares used

- python 3.X
- numpy
- pandas
- plotly
- json