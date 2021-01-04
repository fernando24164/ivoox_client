Ivoox-client
############

Ivoox client


Quickstart
==========

ivoox-client is available on PyPI and can be installed with `pip <https://pip.pypa.io>`_.

.. code-block:: console

    $ pip install ivoox_client

After installing ivoox-client you can use it like any other Python module.

Here is a simple example:

.. code-block:: python

    import asyncio
    from ivoox_client import client

    if __name__ == "__main__":
        loop = asyncio.get_event_loop()
        response = loop.run_until_complete(client.get_audios())
