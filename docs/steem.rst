Your Starting Point
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Quick Start
-----------
You can start using the library with just a few lines of code, as seen in this quick example:

.. code-block:: python

   # first, we initialize Steem class
   from smoke import Steem
   s = Steem()

.. code-block:: python

   # check @ned's balance
   >>> s.get_account('stoner')['balance']
   '420.011 SMOKE'

   # lets send 1.0 SMOKE to @baabeetaa
   >>> s.commit.transfer(to='baabeetaa', amount=1, asset='SMOKE', account='stoner')
   {'expiration': '2017-03-12T17:54:43',
    'extensions': [],
    'operations': [['transfer',
      {'amount': '1.000 SMOKE', 'from': 'stoner', 'memo': '', 'to': 'baabeetaa'}]],
    'ref_block_num': 23008,
    'ref_block_prefix': 961695589,
    'signatures': ['1f1322be9ca0c22b27c0385c929c9863901ac78cdaedea2162024ea040e22c4f8b542c02d96cbc761cbe4a188a932bc715bb7bcaf823b6739a44bb29fa85f96d2f']}

   # yup, its there
   >>> s.get_account('stoner')['balance']
   '421.011 SMOKE'

Importing your Account
============================
`smoke-python` comes with a BIP38 encrypted wallet, which holds your private keys.



Alternatively, you can also pass required WIF's to ``Steem()`` initializer.

::

    from smoke import Steem
    s = Steem(keys=['<private_posting_key>', '<private_active_key>'])

Using the encrypted wallet is however a recommended way.

Please check :doc:`cli` to learn how to set up the wallet.

Interfacing with steemd
=======================
``Steem()`` inherits API methods from ``Steemd``, which can be called like so:

.. code-block:: python

   s = Steem()

   s.get_account('ned')
   s.get_block(8888888)
   s.get_content('author', 'permlink')
   s.broadcast_transaction(...)
   # and many more

You can see the list of available methods by calling ``help(Steem)``.
If a method is not available trough the Python API, we can call it manually using ``s.exec()``:

.. code-block:: python

   s = Steem()

   # this call
   s.get_followers('furion', 'abit', 'blog', 10)

   # is same as
   s.exec('get_followers',
          'furion', 'abit', 'blog', 10,
           api='follow_api')

Commit and Wallet
=================
``Steem()`` comes equipped with ``Commit`` and ``Wallet``, accessible via dot-notation.

.. code-block:: python

   s = Steem()

   # accessing Commit methods
   s.commit.transfer(...)

   # accessing Wallet methods
   s.wallet.get_active_key_for_account(...)

Please check :doc:`core` documentation to learn more.


Steem
-----

As displayed in the `Quick Start` above, ``Steem`` is the main class of this library. It acts as a gateway to other components, such as
``Steemd``, ``Commit``, ``Wallet`` and ``HttpClient``.

Any arguments passed to ``Steem`` as ``kwargs`` will naturally flow to sub-components. For example, if we initialize
Steem with ``steem = Steem(no_broadcast=True)``, the ``Commit`` instance is configured to not broadcast any transactions.
This is very useful for testing.

.. autoclass:: steem.steem.Steem
   :members:


Steemd API
----------

Steemd contains API generating utilities. ``Steemd``'s methods will be automatically available to ``Steem()`` classes.
See :doc:`steem`.

.. _steemd-reference:

.. automodule:: steem.steemd
   :members:


Setting Custom Nodes
--------------------

There are 3 ways in which you can set custom ``steemd`` nodes to use with ``steem-python``.

**1. Global, permanent override:**
You can use ``steempy set nodes`` command to set one or more node URLs. The nodes need to be separated with comma (,)
and shall contain no whitespaces.

    ::

        ~ % steempy config
        +---------------------+--------+
        | Key                 | Value  |
        +---------------------+--------+
        | default_vote_weight | 100    |
        | default_account     | furion |
        +---------------------+--------+
        ~ % steempy set nodes https://gtg.steem.house:8090/
        ~ % steempy config
        +---------------------+-------------------------------+
        | Key                 | Value                         |
        +---------------------+-------------------------------+
        | default_account     | furion                        |
        | default_vote_weight | 100                           |
        | nodes               | https://gtg.steem.house:8090/ |
        +---------------------+-------------------------------+
        ~ % steempy set nodes https://gtg.steem.house:8090/,https://api.steemit.com
        ~ % steempy config
        +---------------------+----------------------------------------------------------+
        | Key                 | Value                                                    |
        +---------------------+----------------------------------------------------------+
        | nodes               | https://gtg.steem.house:8090/,https://api.steemit.com    |
        | default_vote_weight | 100                                                      |
        | default_account     | furion                                                   |
        +---------------------+----------------------------------------------------------+
        ~ %


To reset this config run ``steempy set nodes ''``.

**2. For Current Python Process:**
You can override default `Steemd` instance for current Python process, by overriding the `instance` singleton.
You should execute the following code when your program starts, and from there on out, all classes (Blockchain, Account,
Post, etc) will use this as their default instance.

    ::

        from smoke.steemd import Steemd
        from smoke.instance import set_shared_steemd_instance

        steemd_nodes = [
            'https://gtg.steem.house:8090',
            'https://api.steemit.com',
        ]
        set_shared_steemd_instance(Steemd(nodes=steemd_nodes))


**3. For Specific Class Instance:**
Every class that depends on steemd comes with a ``steemd_instance`` argument.
You can override said steemd instance, for any class you're initializing (and its children).

This is useful when you want to contain a modified ``steemd`` instance to an explicit piece of code (ie. for testing).

    ::

        from smoke.steemd import Steemd
        from smoke.account import Account
        from smoke.Blockchain import Blockchain

        steemd_nodes = [
            'https://gtg.steem.house:8090',
            'https://api.steemit.com',
        ]
        custom_instance = Steemd(nodes=steemd_nodes)

        account = Account('furion', steemd_instance=custom_instance)
        blockchain = Blockchain('head', steemd_instance=custom_instance)
