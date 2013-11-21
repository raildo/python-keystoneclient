# vim: tabstop=4 shiftwidth=4 softtabstop=4

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

import uuid

from keystoneclient.tests.v3 import utils
from keystoneclient.v3 import quota



class QuotaDomainTests(utils.TestCase, utils.QuotaCrudTests):
    def setUp(self):
        super(QuotaDomainTests, self).setUp()
        self.key = 'domain'
        self.collection_key = 'domains'
        self.complement = 'quotas'
        self.model = quota.DomainQuota
        self.manager = self.client.domainquota

    def new_ref(self, **kwargs):
        kwargs = super(QuotaDomainTests, self).new_ref(**kwargs)
        kwargs.setdefault('enabled', True)
        kwargs.setdefault('name', uuid.uuid4().hex)
        return kwargs
