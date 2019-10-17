# NSO to EPNM Optical Service

A python script to create and delete optical services (OCHCC) through REST API calls to NSO.  NSO then communicates to EPNM and launches the service.  

![](nso_epnm_2.png)

## Contacts:
* Jason Mah (jamah@cisco.com)

# Solution Components
* Python3
* NSO
* EPN-M


# Installation

Create a constants.py file and add the following variables:

```bash
# NSO server IP and Username and Password
NSO_URL = "http://x.x.x.x:8080/"
NSO_USER = "nso_username"
NSO_PASSWORD = "nso_password"

# EPNM server IP and port and NSO device name
EPNM_IP = "x.x.x.x"
EPNM_PORT = "443"
EPNM_DEVICE_NAME = "EPNM1"  #EPNM NSO server name
```
# Usage

To launch an optical service create:

```bash
$ python create_service.py
```

To launch an optical service delete:

```bash
$ python delete_service.py
```


## License

Provided under Cisco Sample Code License, for details see [LICENSE](./LICENSE)

## Code of Conduct

Our code of conduct is available [here](./CODE_OF_CONDUCT.md)

## Contributing

See our contributing guidelines [here](./CONTRIBUTING.md)
