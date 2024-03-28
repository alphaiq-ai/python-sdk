# CompanyInfoModel1

Company identifier information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consilience_id** | **str** | Internal custom company identifier | 
**ticker** | **str** | Ticker of the company/security | 
**cik** | **str** | Central indexing key (CIK) used by SEC&#39;s EDGAR database | 
**lei** | **str** | Legal entity identifier (LEI) | 

## Example

```python
from openapi_client.models.company_info_model1 import CompanyInfoModel1

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyInfoModel1 from a JSON string
company_info_model1_instance = CompanyInfoModel1.from_json(json)
# print the JSON string representation of the object
print CompanyInfoModel1.to_json()

# convert the object into a dict
company_info_model1_dict = company_info_model1_instance.to_dict()
# create an instance of CompanyInfoModel1 from a dict
company_info_model1_form_dict = company_info_model1.from_dict(company_info_model1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


