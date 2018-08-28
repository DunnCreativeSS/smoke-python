from smoke.amount import Amount


def test_amount_init():
    a = Amount('1 SMOKE')
    assert dict(a) == {'amount': 1.0, 'asset': 'SMOKE'}
