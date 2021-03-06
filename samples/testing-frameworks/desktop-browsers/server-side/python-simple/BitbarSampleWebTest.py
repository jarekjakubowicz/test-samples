# -*- coding: UTF-8 -*-

#
# Copyright(C) 2019 Bitbar Technologies Oy
#

import os
import sys
import time
import unittest
import xmlrunner
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By

def log(msg):
    print ("%s: %s" % (time.strftime("%H:%M:%S"), msg))
    sys.stdout.flush()

class BitbarSampleWebTest(unittest.TestCase):

    screenshot_dir = None

    def setUp(self):
        self.screenshot_dir = '%s/screenshots/' % os.getcwd()
        if not os.path.exists(self.screenshot_dir):
            os.mkdir(self.screenshot_dir)


    def testSample(self):
        driver = webdriver.Remote('http://localhost:4723/wd/hub')
        log("Start!")

        try:
            driver.get("https://bitbar.com/")
            print driver.title

            driver.get_screenshot_as_file(self.screenshot_dir + 'frontpage.png')
            log("Finish!")
        except WebDriverException:
            log("Failed!")

if __name__ == '__main__':
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))
