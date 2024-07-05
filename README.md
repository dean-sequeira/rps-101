# RPS-101
*Demo of `st.connections.ExperimentalBaseConnection` for API requests*

Remake of Rock, Paper, Scissors if it had 101 objects instead of 3. RPS101 public API used to demonstrate a custom
Streamlit's `st.connections.ExperimentalBaseConnection`.


The APIConnection class is a used to facilitate API interactions using the popular Python library, requests.
This class inherits from ExperimentalBaseConnection provided by Streamlit and provides methods to make API calls and
return the response in a json format.


## Class Overview

### `_connect(self, route=None, method='get', payload=None)`

This private method internally handles the API connection based on the provided parameters:

- `route` (str): The API endpoint to be called (default is `None`).
- `method` (str): The HTTP method to use (default is `get`).
- `payload` (dict): The payload to send along with the request (default is `None`).

The method will use Streamlit secrets to retrieve the API URL and headers (optional). Depending on the HTTP method, the method will call the `requests.get()` or `requests.post()` method.

The method returns a `requests.Response` object representing the API response.

### `get(self, route=None, method='get', payload=None)`

This public method allows you to connect to the API and retrieve the JSON response using the `_connect` method internally. It takes the same parameters as `_connect`:

- `route` (str): The API endpoint to be called (default is `None`).
- `method` (str): The HTTP method to use (default is `get`).
- `payload` (dict): The payload to send along with the request (default is `None`).

The method returns the JSON data of the API response.

If the API call encounters an HTTP error (status code other than 2xx), it will raise a `requests.exceptions.HTTPError` and display an error message using Streamlit's `st.error()` method.

## Example Usage

Here's an example of how to use the `APIConnection` class in your Streamlit app:

```python
import streamlit as st
from st_api_conn import APIConnection

# create connection
conn = st.experimental_connection(name="rps101", type=APIConnection)
# set endpoint
endpoint = "objects/all"
# make API call
response = conn.get(endpoint)
# display response
st.write(response)
```

.streamlit/secrets.toml
```toml

[connections.rps101] # name of connection used in st.experimental_connection()
url = "https://rps101.pythonanywhere.com/api/v1/" # base url of API which will prefix all endpoints
headers = { 'access_api_key' = 'my-secret-api-key-here' } # optional headers if required by API

```

## Credits
Original RPS-101 idea, and all hand symbol artwork is from [UMOP.COM](https://www.umop.com/rps101.htm).
The API used for the object list and battle outcomes are from [RPS101 API](https://rps101.pythonanywhere.com/api). 👏 
