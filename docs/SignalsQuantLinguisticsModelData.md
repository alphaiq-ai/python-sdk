# SignalsQuantLinguisticsModelData

Output from API

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company** | [**CompanyInfoModel1**](CompanyInfoModel1.md) |  | 
**signals** | [**List[SignalsQuantLinguisticsSignalsModel2]**](SignalsQuantLinguisticsSignalsModel2.md) | Quantitative linguistics signal data | 

## Example

```python
from openapi_client.models.signals_quant_linguistics_model_data import SignalsQuantLinguisticsModelData

# TODO update the JSON string below
json = "{}"
# create an instance of SignalsQuantLinguisticsModelData from a JSON string
signals_quant_linguistics_model_data_instance = SignalsQuantLinguisticsModelData.from_json(json)
# print the JSON string representation of the object
print SignalsQuantLinguisticsModelData.to_json()

# convert the object into a dict
signals_quant_linguistics_model_data_dict = signals_quant_linguistics_model_data_instance.to_dict()
# create an instance of SignalsQuantLinguisticsModelData from a dict
signals_quant_linguistics_model_data_form_dict = signals_quant_linguistics_model_data.from_dict(signals_quant_linguistics_model_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


