def allocate(Q, wishes):
    """ Resources allocation in case of penury: When a list of consumers want
    some resources, and that resource exists in insufficient quantity to
    satisfy the total demand, a way must be found to allocate existing resources
    while minimizing unsatisfaction.

    This heuristic finds a ceiling, a maximal authorized quantity of
    resources allowed per consumer. Those who asked less than the
    ceiling will receive what they asked for, others will receive the
    ceiling quantity. resources are attributed by integral values, so
    there might be some resources left, although less than 1unit per
    unsatisfied consumer. The couple of remaining resource units beyond
    the ceiling are attributed to the consumers who asked for the most
    resources, i.e. presumably the most unsatisfied ones.

    :param Q: total quantity allocated.
    :param wishes: quantities wished by each consumer (dictionary, arbitrary key types).
    :return:  quantities allocated to each consumer (dictionary, same keys as above).
    """
    wish_values = wishes.values()
    if sum(wish_values) <= Q:
        # print "There's enough for everyone!"
        return wishes
    unallocated = Q  # resources left to attribute
    granted = {k: 0 for k in wishes.keys()}  # what consumers have been granted so far
    n_unsatisfied = len(wishes) - wish_values.count(0)  # nb of consumers still unsatisfied
    ceiling = 0  # current limit (increases until everything is allocated)

    # first stage: find a ceiling that leaves less than one unit per unsatisfied buyer
    while unallocated >= n_unsatisfied:
        lot = unallocated/n_unsatisfied  # We can safely distribute at least this much
        ceiling += lot
        # print ("%i units left; allocating %i units to %i unsatisfied people" % (unallocated, lot, n_unsatisfied))
        for k, wish_k in wishes.items():
            wish_more_k = wish_k-granted[k]
            if wish_more_k > 0:  # this consumer isn't satisfied yet, give him some more
                lot_k = min(wish_more_k, lot)  # don't give more than what he asked for, though.
                # print ("person %i wishes %i more unit, receives %i"%(i, wish_i, lot_i))
                granted[k] += lot_k
                unallocated -= lot_k
                if granted[k] == wishes[k]:
                    n_unsatisfied -= 1  # He's satisfied now!

    # 2nd stage: give the remaining units, one by one, to biggest unsatisfied buyers
    got_leftover = sorted(wishes.keys(), key=lambda k: granted[k]-wishes[k])[0:unallocated]
    # print ("%i more units to distribute, they will go to %s" % (unallocated, got_leftover))
    for k in got_leftover:
        granted[k] += 1
        unallocated -= 1

    # Some invariant checks
    if True:
        assert unallocated == 0
        assert sum(granted.values()) == Q
        for k in wishes.keys():
            assert granted[k] <= wishes[k]
            assert granted[k] <= ceiling+1

    return granted
