#!/usr/bin/env python3
"""Import modules for client module tests"""

import unittest
from typing import Dict

from unittest.mock import (
    MagicMock,
    Mock,
    PropertyMock,
    patch,
)

from parameterized import parameterized, parameterized_class


class TestGithubOrgClient(unittest.TestCase):
    """test the GithubOrgClient class"""
    @parameterized.expand([
        ("google", {'login': "google"}),
        ("abc", {'login': "abc"}),
    ])
    @patch("client.get_json")
    def test_org(self, org: str, resp: Dict, mocked_func: MagicMock) -> None:
        """Tests for the org method"""
        mocked_func.return_value = MagicMock(return_value=resp)
        gh_org_client = GithubOrgClient(org)
        self.assertEqual(gh_org_client.org(), resp)
        mocked_func.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org)
        )
