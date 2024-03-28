# BulkMappingGet200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**BulkMappingGet200ResponseData**](BulkMappingGet200ResponseData.md) |  | 

## Example

```python
from alphaiq_sdk.models.bulk_mapping_get200_response import BulkMappingGet200Response

# TODO update the JSON string below
json = "{}"
# create an instance of BulkMappingGet200Response from a JSON string
bulk_mapping_get200_response_instance = BulkMappingGet200Response.from_json(json)
# print the JSON string representation of the object
print BulkMappingGet200Response.to_json()

# convert the object into a dict
bulk_mapping_get200_response_dict = bulk_mapping_get200_response_instance.to_dict()
# create an instance of BulkMappingGet200Response from a dict
bulk_mapping_get200_response_form_dict = bulk_mapping_get200_response.from_dict(bulk_mapping_get200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


