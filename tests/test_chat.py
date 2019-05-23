# -*- coding: utf-8 -*-

import pytest
from Python_testing_training.app.app import App


@pytest.fixture
def app(request):
    fixture = App()
    request.addfinalizer(fixture.destroy)
    return fixture


# @py.tests.mark.parametrize
def test_add_blue_text(app):
    app.go_page()
    app.enter_name('Test')
    app.enter_message('One Two Three')
    app.choose_color('blue')
    app.click_ok()
