#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import pytest

class TestDemo:

    def test_get(self):
        r = requests.get('http://httpbin.testing-studio.com/get')
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert r.status_code == 200