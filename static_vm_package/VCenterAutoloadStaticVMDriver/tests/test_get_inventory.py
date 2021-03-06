import uuid
from unittest import TestCase

import jsonpickle
from pyVmomi import vim
from mock import Mock, create_autospec, patch
from pyVmomi.VmomiSupport import vmodlNames

from static_vm_package.VCenterAutoloadStaticVMDriver.app_discovery.vm_autoload_driver import \
    DeployAppOrchestrationDriver


class TestGetInventory(TestCase):
    def setUp(self):
        self.deploy_app_orchestration_driver = DeployAppOrchestrationDriver()
        self.context = Mock()
        self.context.resource.attributes = Mock()
        self.VMLoader = Mock()

    def test_get_inventory(self):
        vcenter_data_model = Mock()
        vcenter_data_model.default_datacenter = 'name'
        self.deploy_app_orchestration_driver.cs_helper.get_session = Mock(return_value=Mock())
        self.deploy_app_orchestration_driver.model_parser.convert_to_vcenter_model = Mock(
            return_value=vcenter_data_model)
        self.deploy_app_orchestration_driver._get_connection_to_vcenter = Mock(return_value=Mock())
        self.deploy_app_orchestration_driver._try_get_ip = Mock(return_value=Mock())
        self.deploy_app_orchestration_driver._get_vm_details = Mock(return_value=Mock())
        self.deploy_app_orchestration_driver.pv_service.find_vm_by_name = Mock(
            return_value=vim.VirtualMachine(Mock(), Mock()))

        # deployer.deploy_from_image = Mock(return_value=res)
        self.context.resource.attributes = {'vCenter VM': 'dd', 'vCenter Name': 'd2'}

        self.logger = Mock()
        # Act

        self.deploy_app_orchestration_driver.get_inventory(self.context)
        # Assert

        self.assertTrue(self.deploy_app_orchestration_driver.model_parser.convert_to_vcenter_model.called)
        self.assertTrue(self.deploy_app_orchestration_driver.cs_helper.get_session.called)
        self.assertTrue(self.deploy_app_orchestration_driver.model_parser.convert_to_vcenter_model.valled)
        self.assertTrue(self.deploy_app_orchestration_driver._get_connection_to_vcenter.called)
        self.assertTrue(self.deploy_app_orchestration_driver._try_get_ip.called)
        self.assertTrue(self.deploy_app_orchestration_driver._get_vm_details.called)
        self.assertTrue(self.deploy_app_orchestration_driver.pv_service.find_vm_by_name.called)
        


    def test_get_vm_details(self):
        vm_details = self.deploy_app_orchestration_driver._get_vm_details(uuid="Piplup",
                                                                          vcenter_name="Prinplup",
                                                                          resource="Empoleon")
        str_vm_details = jsonpickle.decode(vm_details)
        self.assertTrue(str_vm_details['CloudProviderName']=="Prinplup")
        self.assertTrue(str_vm_details['UID']=='Piplup')




