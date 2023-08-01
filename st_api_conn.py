from streamlit.connections import ExperimentalBaseConnection
import streamlit as st
import requests


class APIConnection(ExperimentalBaseConnection[requests]):

    def _connect(self, route=None, method='get', payload=None):
        """Connect to the API and return the response.

        :param route: The API endpoint.
        :param method: The HTTP method.
        :param payload: The payload to send.
        :return: The response object.
        """
        headers = self._secrets.get('headers', None)
        url = f"{self._secrets['url']}{route}"

        if method.lower() == 'post':
            response = requests.post(url, headers=headers, data=payload)
        else:
            response = requests.get(url, headers=headers, data=payload)

        return response

    def get(self, route=None, method='get', payload=None):
        """Connect to the API and return the JSON response using the _connect method.

        :param route: The API endpoint.
        :param method: The HTTP method.
        :param payload: The payload to send.
        :return: The JSON response data.
        """
        try:
            response = self._connect(route, method, payload)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            st.error(f"Error: {e}")
            return None
