# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class InlineResponse200(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, forecast: List[float]=None):  # noqa: E501
        """InlineResponse200 - a model defined in Swagger

        :param forecast: The forecast of this InlineResponse200.  # noqa: E501
        :type forecast: List[float]
        """
        self.swagger_types = {
            'forecast': List[float]
        }

        self.attribute_map = {
            'forecast': 'forecast'
        }
        self._forecast = forecast

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse200':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_200 of this InlineResponse200.  # noqa: E501
        :rtype: InlineResponse200
        """
        return util.deserialize_model(dikt, cls)

    @property
    def forecast(self) -> List[float]:
        """Gets the forecast of this InlineResponse200.


        :return: The forecast of this InlineResponse200.
        :rtype: List[float]
        """
        return self._forecast

    @forecast.setter
    def forecast(self, forecast: List[float]):
        """Sets the forecast of this InlineResponse200.


        :param forecast: The forecast of this InlineResponse200.
        :type forecast: List[float]
        """

        self._forecast = forecast
