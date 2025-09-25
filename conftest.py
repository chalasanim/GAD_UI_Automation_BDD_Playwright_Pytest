import pytest
import os
import logging
import shutil

@pytest.fixure(scope = 'session')
def context(browswer: Browser):
  context = browser.new_context(ignore_http_errors = True)
  yield context
  context.close()

