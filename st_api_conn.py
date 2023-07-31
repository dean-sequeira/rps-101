from streamlit.connections import ExperimentalBaseConnection
import streamlit as st
import requests


class APIConnection(ExperimentalBaseConnection[requests]):

    def _connect(self, route=None, method='get', payload=None) -> requests.get:
        """Connect to the API and return the response
        :param route: The API endpoint
        :param method: The HTTP method
        :param payload: The payload to send
        :return: The response
        """
        if 'headers' in self._secrets:
            headers = self._secrets['headers']
        else:
            headers = None
        if method == 'post':
            return requests.post(f"{self._secrets['url']}{route}", headers=headers, data=payload)
        else:
            return requests.get(f"{self._secrets['url']}{route}", headers=headers, data=payload)

    def get(self, route=None, method='get', payload=None) -> requests.get:
        """Connect to the API and return the response using the _connect method
        :param route: The API endpoint
        :param method: The HTTP method
        :param payload: The payload to send
        :return: The response
        """
        try:
            self._connect(route, method, payload).raise_for_status()
        except requests.exceptions.HTTPError as e:
            st.error(f"Error: {e}")
        return self._connect(route, method, payload).json()
