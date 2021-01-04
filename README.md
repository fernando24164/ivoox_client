# Ivoox Client

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Contributing](./CONTRIBUTING.rst)
- [Credit](#credit)

## About <a name = "about"></a>

Client to get audios, podcasts and search on Ivoox

## Getting Started <a name = "getting_started"></a>

Take a look to examples or tests folder

### Installing

```
pip install ivoox_client
```

## Usage <a name = "usage"></a>

```
import asyncio
from ivoox_client import client

loop = asyncio.get_event_loop()
response = loop.run_until_complete(client.get_audios())
```

## Credit

Inspired by [node-ivoox](https://github.com/EdgarVaguencia/node-ivoox)
