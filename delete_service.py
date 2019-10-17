"""
Copyright (c) 2019 Cisco and/or its affiliates.
This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.0 (the "License"). You may obtain a copy of the
License at
               https://developer.cisco.com/docs/licenses
All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.


NSO EPNM Optical

"""

from controllers.nso import NsoController

if __name__ == "__main__":

    nso = NsoController()

    nso.syncFromDevices()

    nso.deleteOCCHCcircuit(serviceName="OCHCC_site1_2")

    nso.deleteInternalPatch(siteName="Site1",
                            aEndTp="VFAC-5-4-12-1",
                            zEndTp="PSLINE-1-1-10-RX")
    nso.deleteInternalPatch(siteName="Site1",
                            aEndTp="PSLINE-1-1-10-TX",
                            zEndTp="VFAC-5-4-12-1")
    nso.deleteInternalPatch(siteName="Site2",
                            aEndTp="VFAC-1-5-12-1",
                            zEndTp="PSLINE-1-1-10-RX")
    nso.deleteInternalPatch(siteName="Site2",
                            aEndTp="PSLINE-1-1-10-TX",
                            zEndTp="VFAC-1-5-12-1")


    #nso.deleteOCCHCcircuit(serviceName="OCHCC_site1_2_circuit2")