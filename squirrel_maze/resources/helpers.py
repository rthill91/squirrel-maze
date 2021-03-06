import random


def get_rand_val(min_val, max_val):
    return random.randint(min_val, max_val)


def is_critical_hit(value, crit_hit_chance):
    if value >= crit_hit_chance:
        return True
    else:
        return False


def is_critical_fail(value, crit_fail_chance):
    if value <= crit_fail_chance:
        return True
    else:
        return False


def get_crit_hit_bonus():
    # TODO: add recursive addition on 10s
    # should that be a passive advantage?
    return int(get_rand_val(1, 10) / 2)


def get_crit_fail_bonus():
    value = int(get_rand_val(1, 10) / 2) * -1
    return value


def get_stat_list():
    stats = ["hp", "str", "dex", "sta", "wil",
             "crit_hit_chance", "crit_fail_chance"]
    return stats


def calc_magic_defense(source, target):
    return source.cur_wil - target.cur_wil


def any_members_active(actors, pc_type):
    # TODO: rename from active to something else, alive?
    # to remove confusion from 'active actor'
    for actor in actors:
        if actor.pc_type == pc_type and actor.cur_hp > 0:
            return True
    return False


def get_actor_list_by_stat(actors, stat_primary, stat_secondary):
    sorted_actors = sorted(actors, key=lambda actor: (getattr(actor, stat_primary), getattr(actor, stat_secondary)),
                           reverse=True)
    # TODO: Break ties using level, then random number
    # sorted_actors = break_tie_between(sorted_actors)
    return sorted_actors


def get_max_stat_from_actor_list(actors, stat):
    # max_val = max(actor.cur_dex for actor in actors)
    max_val = max(getattr(actor, stat) for actor in actors)
    # TODO: add condition on level, to not call break tie, to prevent a loop
    return max_val
