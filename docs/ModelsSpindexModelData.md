# ModelsSpindexModelData

Output from API

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**company** | [**CompanyInfoModel**](CompanyInfoModel.md) |  | 
**spindex** | [**List[ModelsSpindexModelItems]**](ModelsSpindexModelItems.md) | SPINDEX model results | 

## Example

```python
from openapi_client.models.models_spindex_model_data import ModelsSpindexModelData

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsSpindexModelData from a JSON string
models_spindex_model_data_instance = ModelsSpindexModelData.from_json(json)
# print the JSON string representation of the object
print ModelsSpindexModelData.to_json()

# convert the object into a dict
models_spindex_model_data_dict = models_spindex_model_data_instance.to_dict()
# create an instance of ModelsSpindexModelData from a dict
models_spindex_model_data_form_dict = models_spindex_model_data.from_dict(models_spindex_model_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


