Low Level
~~~~~~~~~

HttpClient
----------

A fast ``urllib3`` based HTTP client that features:

* Connection Pooling
* Concurrent Processing
* Automatic Node Failover

The functionality of ``HttpClient`` is encapsulated by ``Steem`` class. You shouldn't be using ``HttpClient`` directly,
unless you know exactly what you're doing.

.. autoclass:: smokebase.http_client.HttpClient
   :members:

-------------

smokebase
---------

smokeBase contains various primitives for building higher level abstractions.
This module should only be used by library developers or people with deep domain knowledge.

**Warning:**
Not all methods are documented. Please see source.

.. image:: https://i.imgur.com/A9urMG9.png

Account
=======

.. automodule:: smokebase.account
   :members:

--------

Base58
======

.. automodule:: smokebase.base58
   :members:

--------

Bip38
=====

.. automodule:: smokebase.bip38
   :members:


--------

Memo
====

.. automodule:: smokebase.memo
   :members:


--------

Operations
==========

.. automodule:: smokebase.operations
   :members:


--------

Transactions
============

.. automodule:: smokebase.transactions
   :members:



--------

Types
=====

.. automodule:: smokebase.types
   :members:

--------

Exceptions
==========

.. automodule:: smokebase.exceptions
   :members:
