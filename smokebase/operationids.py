op_names = [
    'vote',
    'comment',
    'transfer',
    'transfer_to_vesting',
    'withdraw_vesting',
    'account_create',
    'account_update',
    'witness_update',
    'account_witness_vote',
    'account_witness_proxy',
    'custom',
    'delete_comment',
    'custom_json',
    'comment_options',
    'set_withdraw_vesting_route',
    'custom_binary',
    'claim_reward_balance',
    'author_reward',
    'curation_reward',
    'comment_reward',
    'shutdown_witness',
    'hardfork',
    'comment_payout_update',
    'comment_benefactor_reward',
]

#: assign operation ids
operations = dict(zip(op_names, range(len(op_names))))
