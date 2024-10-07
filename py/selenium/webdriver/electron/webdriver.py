# Licensed to the Software Freedom Conservancy (SFC) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The SFC licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
from selenium.common.exceptions import WebDriverException

from selenium.webdriver.chromium.webdriver import ChromiumDriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from .options import Options
from .service import Service


class WebDriver(ChromiumDriver):
    """Controls the ElectronDriver and allows you to drive the browser."""

    def __init__(
        self,
        options: Options = None,
        service: Service = None,
    ) -> None:
        """Creates a new instance of the electron driver. Starts the service and
        then creates new instance of electron driver.

        :Args:
         - options - this takes an instance of ElectronOptions
         - service - Service object for handling the browser driver if you need to pass extra details
        """
        service = service if service else Service()
        if options.binary_location is None:
            raise WebDriverException("You must specify a binary location")

        super().__init__(
            browser_name=DesiredCapabilities.ELECTRON["browserName"],
            options=options,
            service=service,
        )
