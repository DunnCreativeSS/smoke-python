import math

from .amount import Amount
from .instance import shared_steemd_instance


class Converter(object):
    """ Converter simplifies the handling of different metrics of
        the blockchain

        :param Steemd steemd_instance: Steemd() instance to
        use when accessing a RPC

    """

    def __init__(self, steemd_instance=None):
        self.steemd = steemd_instance or shared_steemd_instance()

        self.CONTENT_CONSTANT = 2000000000000

    def steem_per_mvests(self):
        """ Obtain SMOKE/MVESTS ratio
        """
        info = self.steemd.get_dynamic_global_properties()
        return (Amount(info["total_vesting_fund_steem"]).amount /
                (Amount(info["total_vesting_shares"]).amount / 1e6))

    def vests_to_sp(self, vests):
        """ Obtain SP from VESTS (not MVESTS!)

            :param number vests: Vests to convert to SP
        """
        return vests / 1e6 * self.steem_per_mvests()

    def sp_to_vests(self, sp):
        """ Obtain VESTS (not MVESTS!) from SP

            :param number sp: SP to convert
        """
        return sp * 1e6 / self.steem_per_mvests()

    def sp_to_rshares(self, sp, voting_power=10000, vote_pct=10000):
        """ Obtain the r-shares

            :param number sp: Steem Power
            :param int voting_power: voting power (100% = 10000)
            :param int vote_pct: voting participation (100% = 10000)
        """
        # calculate our account voting shares (from vests), mine is 6.08b
        vesting_shares = int(self.sp_to_vests(sp) * 1e6)

        # get props
        props = self.steemd.get_dynamic_global_properties()

        # determine voting power used
        used_power = int((voting_power * vote_pct) / 10000);
        max_vote_denom = props['vote_power_reserve_rate'] * (5 * 60 * 60 * 24) / (60 * 60 * 24);
        used_power = int((used_power + max_vote_denom - 1) / max_vote_denom)

        # calculate vote rshares
        rshares = ((vesting_shares * used_power) / 10000)

        return rshares


    def rshares_2_weight(self, rshares):
        """ Obtain weight from rshares

            :param number rshares: R-Shares
        """
        _max = 2 ** 64 - 1
        return (_max * rshares) / (2 * self.CONTENT_CONSTANT + rshares)
