from squirrel_maze.resources.actor import Actor


def get_goblin(actor_id=0, name='Goblin', pc_type='npc', affiliation='unfriendly'):
    return Actor(actor_id=actor_id, pc_type=pc_type, affiliation=affiliation, name=name, level=1, max_hp=5, max_str=3,
                 max_dex=2, max_sta=2)


def get_big_goblin(actor_id=0, name='Big Goblin', pc_type='npc', affiliation='unfriendly'):
    return Actor(actor_id=actor_id, pc_type=pc_type, affiliation=affiliation, name=name, level=2, max_hp=10, max_str=9,
                 max_dex=9, max_sta=9)
