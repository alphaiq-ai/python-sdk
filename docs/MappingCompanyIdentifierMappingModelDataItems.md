# MappingCompanyIdentifierMappingModelDataItems


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consilience_id** | **str** | Consilience company identifier | [optional] 
**ticker** | **str** | Ticker of the company/security | [optional] 
**cik** | **str** | Central indexing key (CIK) used by SEC&#39;s EDGAR database | [optional] 
**lei** | **str** | Legal entity identifier (LEI) | [optional] 
**name** | **str** | Company name | [optional] 

## Example

```python
from openapi_client.models.mapping_company_identifier_mapping_model_data_items import MappingCompanyIdentifierMappingModelDataItems

# TODO update the JSON string below
json = "{}"
# create an instance of MappingCompanyIdentifierMappingModelDataItems from a JSON string
mapping_company_identifier_mapping_model_data_items_instance = MappingCompanyIdentifierMappingModelDataItems.from_json(json)
# print the JSON string representation of the object
print MappingCompanyIdentifierMappingModelDataItems.to_json()

# convert the object into a dict
mapping_company_identifier_mapping_model_data_items_dict = mapping_company_identifier_mapping_model_data_items_instance.to_dict()
# create an instance of MappingCompanyIdentifierMappingModelDataItems from a dict
mapping_company_identifier_mapping_model_data_items_form_dict = mapping_company_identifier_mapping_model_data_items.from_dict(mapping_company_identifier_mapping_model_data_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


