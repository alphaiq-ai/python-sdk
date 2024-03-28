# FileDownloadModelData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | Pre-signed download link for AWS S3 object | 

## Example

```python
from openapi_client.models.file_download_model_data import FileDownloadModelData

# TODO update the JSON string below
json = "{}"
# create an instance of FileDownloadModelData from a JSON string
file_download_model_data_instance = FileDownloadModelData.from_json(json)
# print the JSON string representation of the object
print FileDownloadModelData.to_json()

# convert the object into a dict
file_download_model_data_dict = file_download_model_data_instance.to_dict()
# create an instance of FileDownloadModelData from a dict
file_download_model_data_form_dict = file_download_model_data.from_dict(file_download_model_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


