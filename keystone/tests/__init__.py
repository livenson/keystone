# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright 2013 OpenStack Foundation
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from keystone.openstack.common import gettextutils

# NOTE(blk-u):
# gettextutils.install() must run to set _ before importing any modules that
# contain static translated strings.
#
# Configure gettextutils for deferred translation of messages
# so that error messages in responses can be translated according to the
# Accept-Language in the request rather than the Keystone server locale.
gettextutils.install('keystone', lazy=True)


from keystone.tests.core import *  # flake8: noqa
