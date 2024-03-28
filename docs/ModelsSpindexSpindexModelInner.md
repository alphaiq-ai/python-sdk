# ModelsSpindexSpindexModelInner


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
from alphaiq_sdk.models.models_spindex_spindex_model_inner import ModelsSpindexSpindexModelInner

# TODO update the JSON string below
json = "{}"
# create an instance of ModelsSpindexSpindexModelInner from a JSON string
models_spindex_spindex_model_inner_instance = ModelsSpindexSpindexModelInner.from_json(json)
# print the JSON string representation of the object
print ModelsSpindexSpindexModelInner.to_json()

# convert the object into a dict
models_spindex_spindex_model_inner_dict = models_spindex_spindex_model_inner_instance.to_dict()
# create an instance of ModelsSpindexSpindexModelInner from a dict
models_spindex_spindex_model_inner_form_dict = models_spindex_spindex_model_inner.from_dict(models_spindex_spindex_model_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


