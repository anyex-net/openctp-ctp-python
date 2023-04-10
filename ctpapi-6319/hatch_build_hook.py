import platform
import sys
from typing import Any, Dict

from hatchling.builders.hooks.plugin.interface import BuildHookInterface


class CustomBuildHook(BuildHookInterface):
    def initialize(self, version: str, build_data: Dict[str, Any]) -> None:
        build_data['pure_python'] = False
        build_data['infer_tag'] = True
        if sys.platform.startswith('linux'):
            build_data['artifacts'].extend([
                'ctpapi_6319/linux_x64/*.so',
                'ctpapi_6319/thosttraderapi.py',
            ])
        elif sys.platform.startswith('darwin'):
            if platform.machine() == 'x86_64':
                build_data['artifacts'].append('ctpapi_6319/mac_x64/*.so')
            elif platform.machine() == 'amd64':
                pass
        elif sys.platform.startswith('win'):
            major, minor = sys.version_info[:2]
            assert major == 3
            assert minor in (7, 8, 9, 10, 11)
            build_data['artifacts'].append('ctpapi_6319/thosttraderapi.py')
            build_data['force_include'].update({
                'ctpapi_6319/win_x64/thostmduserapi_se.dll': 'ctpapi_6319/thostmduserapi_se.dll',
                'ctpapi_6319/win_x64/thosttraderapi_se.dll': 'ctpapi_6319/thosttraderapi_se.dll',
                f'ctpapi_6319/win_x64/py3{minor}/_thostmduserapi.pyd': 'ctpapi_6319/_thostmduserapi.pyd',
                f'ctpapi_6319/win_x64/py3{minor}/_thosttraderapi.pyd': 'ctpapi_6319/_thosttraderapi.pyd',
            })
