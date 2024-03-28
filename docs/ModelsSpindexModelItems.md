# ModelsSpindexModelItems


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | 
**overall_risk** | **int** |  | 
**overall_risk_change** | **int** |  | 
**overall_risk_wh** | **int** |  | 
**overall_risk_roc** | **int** |  | 
**overall_risk_mr** | **int** |  | 
**evasive** | **int** |  | 
**uncertain** | **int** |  | 
**speculative** | **int** |  | 
**constrained** | **int** |  | 
**insecure** | **int** |  | 
**economic_risk** | **int** |  | 
**financial_risk** | **int** |  | 
**earnings_risk** | **int** |  | 
**operational_risk** | **int** |  | 

## Example

```python
from openapi_client.models.models_spindex_model_items import ModelsSpindexModelItems

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsSpindexModelItems from a JSON string
models_spindex_model_items_instance = ModelsSpindexModelItems.from_json(json)
# print the JSON string representation of the object
print ModelsSpindexModelItems.to_json()

# convert the object into a dict
models_spindex_model_items_dict = models_spindex_model_items_instance.to_dict()
# create an instance of ModelsSpindexModelItems from a dict
models_spindex_model_items_form_dict = models_spindex_model_items.from_dict(models_spindex_model_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


