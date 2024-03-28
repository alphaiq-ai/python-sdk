# CompanyInfoModel

Company identifier information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consilience_id** | **str** | Consilience company identifier | 
**ticker** | **str** | Ticker of the company/security | 
**cik** | **str** | Central indexing key (CIK) used by SEC&#39;s EDGAR database | 
**lei** | **str** | Legal entity identifier (LEI) | 

## Example

```python
from openapi_client.models.company_info_model import CompanyInfoModel

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyInfoModel from a JSON string
company_info_model_instance = CompanyInfoModel.from_json(json)
# print the JSON string representation of the object
print CompanyInfoModel.to_json()

# convert the object into a dict
company_info_model_dict = company_info_model_instance.to_dict()
# create an instance of CompanyInfoModel from a dict
company_info_model_form_dict = company_info_model.from_dict(company_info_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


