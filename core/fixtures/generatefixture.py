def generatefixtureweapontrait():
    weaponstraitslist = [
       {
            'name': 'Agile',
            'description': 'multiple attack penalty on the 2nd attack each turn with this weapon is –4 instead of –5, and –8 instead of –10 on the 3rd and subsequent attacks in the turn.'
        },
        {
            'name': 'Attached',
            'description': 'must be combined with another piece of gear to be used.'
        },
        {
            'name': 'Backstabber',
            'description': 'When you hit a flat-footed creature, this weapon deals 1 precision damage'
        },
        {
            'name': 'Backswing',
            'description': 'You can use this weapon’s momentum from a miss to lead into your next attack'
        },
        {
            'name': 'Charge',
            'description': 'If you moved on the action before your attack, add a circumstance bonus to damage'
        },
        {
            'name': 'Deadly',
            'description': 'On a critical hit, the weapon adds a weapon damage die of the listed size. '
        },
        {
            'name': 'Disarm',
            'description': 'You can use this weapon to Disarm with the Athletics skill even if you don’t have a free hand. '
        },
        {
            'name': 'Dwarf',
            'description': 'People of the dwarf ancestry craft and use these weapons.'
        },
        {
            'name': 'Elf',
            'description': 'People of the elf ancestry craft and use these weapons.'
        },
        {
            'name': 'Fatal',
            'description': 'On a critical hit, all theweapon’s damage dice increase to that die size instead of the normal dice, plus the weapon adds another die of damage of the listed size'
        },
        {
            'name': 'Finesse',
            'description': ' You can use your Dexterity modifier instead of your Strength modifier when making attack rolls with this melee weapon.'
        },
        {
            'name': 'Forceful',
            'description': ' When you attack with it more than once on your turn, the second attack adds a circumstance bonus to damage equal to the number of weapon damage dice, and each subsequent attack adds a circumstance bonus to damage equal to double the number of weapon damage dice'
        },
        {
            'name': 'Free-Hand',
            'description': 'This weapon doesn’t take up your hand, usually because it is built into your armor. A free-hand weapon can’t be Disarmed. '
        },
        {
            'name': 'Gnome',
            'description': 'People of the gnome ancestry craft and use these weapons.'
        },
        {
            'name': 'Goblin',
            'description': 'People of the goblin ancestry craft and use these weapons.'
        },
        {
            'name': 'Halfling',
            'description': 'People of the halfling ancestry craft and use these weapons.'
        },
        {
            'name': 'Monk',
            'description': 'Monks can use these weapons with their abilities that normally require unarmed attacks.'
        },
        {
            'name': 'Nonlethal',
            'description': 'All attacks with this weapon are nonlethal.'
        },
        {
            'name': 'Orc',
            'description': 'People of the orc ancestry craft and use these weapons.'
        },
        {
            'name': 'Parry',
            'description': 'This weapon can be used defensively to block attacks.'
        },
        {
            'name': 'Propulsive',
            'description': ' You add half your Strength modifier to damage rolls with a propulsive ranged weapon so long as your Strength modifier is not negative. If you have a negative Strength modifier, you add your full Strength modifier instead'
        },
        {
            'name': 'Reach',
            'description': 'h This weapon is long and can be used to attack creatures up to 10 feet away instead of only adjacent creatures. '
        },
        {
            'name': 'Shove',
            'description': 'You can use this weapon to Shove with the Athletics skill even if you don’t have a free hand.'
        },
        {
            'name': 'Sweep',
            'description': 'This weapon makes wide sweeping or spinning attacks, making it easier to attack multiple enemies. '
        },
        {
            'name': 'Thrown',
            'description': ' You can throw this weapon as a ranged attack.'
        },
        {
            'name': 'Trip',
            'description': ' You can use this weapon to Trip with the Athletics skill even if you don’t have a free hand.'
        },
        {
            'name': 'Twin',
            'description': 'These weapons are used as a pair, each complementing the other. '
        },
        {
            'name': 'Two-Hand',
            'description': 'This weapon can be wielded with two hands.'
        },
        {
            'name': 'Unarmed',
            'description': 'An unarmed attack uses your body rather than a manufactured weapon. '
        },
        {
            'name': 'Versatile',
            'description': 'Can be used to deal a different type of damage than the type listed in the damage entry.'
        },
        {
            'name': 'Volley',
            'description': 'This ranged weapon is less effective at close distances. '
        },
    ]

    stringweapontraits = ''
    i = 1
    for weapontraitdict in weaponstraitslist:
        stringweapontrait = '{"model": "core.weapontrait","pk": '+str(i)+',"fields": {"name": "'+weapontraitdict['name']+'","description": "'+weapontraitdict['description']+'"} },\n'
        i += 1
        stringweapontraits += stringweapontrait

    fixtureweapontraits = '[\n'+stringweapontraits[:len(stringweapontraits)-2]+'\n]'

    return fixtureweapontraits

def generatefixturearmors():
    armorslist = [
        {
            'name': 'Padded armor ',
            'bulk': 'L',
            'type': 'L',
            'trait': 'F',
            'ac_bonus': 1,
            'tac_bonus': 0,
            'check_penalty': 0,
            'speed_penalty': 0,
            'price': {'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 2, 'copperPiece': 0}
        },
        {
            'name': 'Leather',
            'bulk': '1',
            'type': 'L',
            'trait': '',
            'ac_bonus': 1,
            'tac_bonus': 0,
            'check_penalty': 0,
            'speed_penalty': 0,
            'price': {'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 15, 'copperPiece': 0}
        },
        {
            'name': 'Studded Leather',
            'bulk': '1',
            'type': 'L',
            'trait': '',
            'ac_bonus': 2,
            'tac_bonus': 0,
            'check_penalty': -1,
            'speed_penalty': 0,
            'price': {'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 30, 'copperPiece': 0}
        },
        {
            'name': 'Chain shirt',
            'bulk': '2',
            'type': 'L',
            'trait': 'N',
            'ac_bonus': 2,
            'tac_bonus': 1,
            'check_penalty': -1,
            'speed_penalty': 0,
            'price': {'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 45, 'copperPiece': 0}
        },
        {
            'name': 'Hide',
            'bulk': '2',
            'type': 'M',
            'trait': '',
            'ac_bonus': 3,
            'tac_bonus': 0,
            'check_penalty': -3,
            'speed_penalty': 0,
            'price': {'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 20, 'copperPiece': 0}
        },
        {
            'name': 'Scale mail',
            'bulk': '2',
            'type': 'M',
            'trait': '',
            'ac_bonus': 3,
            'tac_bonus': 1,
            'check_penalty': -2,
            'speed_penalty': -5,
            'price': {'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 35, 'copperPiece': 0}
        },
        {
            'name': 'Chain mail',
            'bulk': '2',
            'type': 'M',
            'trait': 'N',
            'ac_bonus': 4,
            'tac_bonus': 1,
            'check_penalty': -3,
            'speed_penalty': -5,
            'price': {'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 60, 'copperPiece': 0}
        },
        {
            'name': 'Breastplate',
            'bulk': '2',
            'type': 'M',
            'trait': 'C',
            'ac_bonus': 4,
            'tac_bonus': 2,
            'check_penalty': -4,
            'speed_penalty': -5,
            'price': {'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 80, 'copperPiece': 0}
        },
        {
            'name': 'Splint mail',
            'bulk': '3',
            'type': 'H',
            'trait': 'C',
            'ac_bonus': 5,
            'tac_bonus': 2,
            'check_penalty': -3,
            'speed_penalty': -10,
            'price': {'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 125, 'copperPiece': 0}
        },
        {
            'name': 'Half plate',
            'bulk': '3',
            'type': 'H',
            'trait': '',
            'ac_bonus': 5,
            'tac_bonus': 2,
            'check_penalty': -4,
            'speed_penalty': -10,
            'price': {'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 175, 'copperPiece': 0}
        },
        {
            'name': 'Full plate (level 2)',
            'bulk': '4',
            'type': 'H',
            'trait': 'C',
            'ac_bonus': 6,
            'tac_bonus': 2,
            'check_penalty': -5,
            'speed_penalty': -10,
            'price': {'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 300, 'copperPiece': 0}
        },
        {
            'name': 'Light wooden shield',
            'bulk': 'L',
            'type': 'S',
            'trait': '',
            'ac_bonus': 1,
            'tac_bonus': 1,
            'check_penalty': -1,
            'speed_penalty': 0,
            'price': {'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 5, 'copperPiece': 0}
        },
        {
            'name': 'Light steel shield',
            'bulk': 'L',
            'type': 'S',
            'trait': '',
            'ac_bonus': 1,
            'tac_bonus': 1,
            'check_penalty': -1,
            'speed_penalty': 0,
            'price': {'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 10, 'copperPiece': 0}
        },
        {
            'name': 'Heavy wooden shield',
            'bulk': '1',
            'type': 'S',
            'trait': '',
            'ac_bonus': 2,
            'tac_bonus': 2,
            'check_penalty': -1,
            'speed_penalty': 0,
            'price': {'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 10, 'copperPiece': 0}
        },
        {
            'name': 'Heavy steel shield',
            'bulk': '1',
            'type': 'S',
            'trait': '',
            'ac_bonus': 2,
            'tac_bonus': 2,
            'check_penalty': -1,
            'speed_penalty': 0,
            'price': {'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 20, 'copperPiece': 0}
        },
    ]

    stringarmors = ''
    i = 1
    j = 1
    for armorsdict in armorslist:
        stringprice = '{"model": "core.price", "pk": ' + str(j) + ', "fields": {"platinumPiece": ' + str(armorsdict['price']['platinumPiece']) + ', "goldPiece": ' + str(armorsdict['price']['goldPiece']) + ', "silverPiece": ' + str(armorsdict['price']['silverPiece']) + ', "copperPiece": ' + str(armorsdict['price']['copperPiece']) + '}},\n'

        stringarmor = '{"model": "core.armor", "pk": ' + str(i) + ', "fields": {"name": "' + armorsdict[
            'name'] + '", "price": ' + str(j) + ', "bulk": "' + armorsdict['bulk'] + '", "type": "' + armorsdict[
                          'type'] + '", "trait": "' + armorsdict['trait'] + '", "ac_bonus": "' + str(armorsdict['ac_bonus']) + '", "tac_bonus": "' + str(armorsdict['tac_bonus']) + '", "check_penalty": "' + str(armorsdict['check_penalty']) + '", "speed_penalty": "' + str(armorsdict['speed_penalty']) + '"}},\n'

        i += 1
        j += 1
        stringarmors += stringprice + stringarmor

    fixturearmors = '[\n' + stringarmors[:len(stringarmors) - 2] + '\n]'

    return fixturearmors

def getWeaponDict(name, bulk, type, damage, hands, group, price, traits, uncommon, reload = 0, range = 0):
    weapondict = {
        'name': name,
        'bulk': bulk,
        'type': type,
        'damage': damage,
        'hands': hands,
        'group': group,
        'price': price,
        'traits': traits,
        'uncommon': uncommon,
        'reload': reload,
        'range': range,
    }

    return weapondict

def getAmmoDict(name, bulk, price, ammoForWeapons):
    weapondict = {
        'name': name,
        'bulk': bulk,
        'price': price,
        'ammoForWeapons': ammoForWeapons,
    }

    return weapondict




def generatefixtureweapons():

    weaponslist = []
    weaponslist.append(
        getWeaponDict(name='Club', bulk='1', type='SM', damage='1d6 B', hands='1', group='CLUB',
                      price={'platinumPiece': 0,'goldPiece': 0,'silverPiece': 0,'copperPiece': 0},
                      traits=[], uncommon=False)
    )
    weaponslist.append(
        getWeaponDict(name='Dagger', bulk='L', type='SM', damage='1d4 P', hands='1', group='KNIFE',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 2, 'copperPiece': 0},
                      traits=[], uncommon=False)
    )
    weaponslist.append(
        getWeaponDict(name='Fist', bulk='', type='SM', damage='1d4 B', hands='1', group='BRAWLING',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 0, 'copperPiece': 0},
                      traits=[], uncommon=False)
    )
    weaponslist.append(
        getWeaponDict(name='Gauntlet', bulk='L', type='SM', damage='1d4 B', hands='1', group='BRAWLING',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 2, 'copperPiece': 0},
                      traits=[], uncommon=False)
    )
    weaponslist.append(
        getWeaponDict(name='Light mace', bulk='L', type='SM', damage='1d4 B', hands='1', group='CLUB',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 4, 'copperPiece': 0},
                      traits=[], uncommon=False)
    )
    weaponslist.append(
        getWeaponDict(name='Longspear', bulk='2', type='SM', damage='1d8 P', hands='2', group='SPEAR',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 5, 'copperPiece': 0},
                      traits=[], uncommon=False)
    )
    weaponslist.append(
        getWeaponDict(name='Mace', bulk='1', type='SM', damage='1d6 B', hands='1', group='CLUB',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 12, 'copperPiece': 0},
                      traits=[], uncommon=False)
    )
    weaponslist.append(
        getWeaponDict(name='Morningstar', bulk='1', type='SM', damage='1d6 B', hands='1', group='CLUB',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 10, 'copperPiece': 0},
                      traits=[], uncommon=False)
    )
    weaponslist.append(
        getWeaponDict(name='Sickle', bulk='L', type='SM', damage='1d4 S', hands='1', group='KNIFE',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 2, 'copperPiece': 0},
                      traits=[], uncommon=False)
    )
    weaponslist.append(
        getWeaponDict(name='Spear', bulk='1', type='SM', damage='1d6 P', hands='1', group='SPEAR',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 1, 'copperPiece': 0},
                      traits=[], uncommon=False)
    )
    weaponslist.append(
        getWeaponDict(name='Spiked gauntlet', bulk='L', type='SM', damage='1d4 P', hands='1', group='BRAWLING',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 3, 'copperPiece': 0},
                      traits=[], uncommon=False)
    )
    weaponslist.append(
        getWeaponDict(name='Staff', bulk='1', type='SM', damage='1d4 B', hands='1', group='CLUB',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 0, 'copperPiece': 0},
                      traits=[], uncommon=False)
    )

    weaponslist.append(
        getWeaponDict(name='Bastard sword', bulk='1', type='MM', damage='1d8 P', hands='1', group='SWORD',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 35, 'copperPiece': 0},
                      traits=[], uncommon=False)
    )
    weaponslist.append(
        getWeaponDict(name='Battle axe', bulk='1', type='MM', damage='1d8 S', hands='1', group='AXE',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 12, 'copperPiece': 0},
                      traits=[], uncommon=False)
    )
    weaponslist.append(
        getWeaponDict(name='Bo staf', bulk='1', type='MM', damage='1d8 P', hands='2', group='CLUB',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 2, 'copperPiece': 0},
                      traits=[], uncommon=False)
    )
    weaponslist.append(
        getWeaponDict(name='Falchion', bulk='1', type='MM', damage='1d10 S', hands='1', group='SWORD',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 30, 'copperPiece': 0},
                      traits=[], uncommon=False)
    )
    weaponslist.append(
        getWeaponDict(name='Flail', bulk='1', type='MM', damage='1d6 B', hands='1', group='FLAIL',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 8, 'copperPiece': 0},
                      traits=[], uncommon=False)
    )
    weaponslist.append(
        getWeaponDict(name='Glaive', bulk='1', type='MM', damage='1d8 S', hands='2', group='POLEARM',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 10, 'copperPiece': 0},
                      traits=[], uncommon=False)
    )
    weaponslist.append(
        getWeaponDict(name='Greataxe', bulk='2', type='MM', damage='1d12 S', hands='2', group='AXE',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 22, 'copperPiece': 0},
                      traits=[], uncommon=False)
    )
    weaponslist.append(
        getWeaponDict(name='Greatclub', bulk='2', type='MM', damage='1d10 B', hands='2', group='CLUB',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 12, 'copperPiece': 0},
                      traits=[], uncommon=False)
    )
    weaponslist.append(
        getWeaponDict(name='Greatpick', bulk='2', type='MM', damage='1d10 P', hands='2', group='PICK',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 14, 'copperPiece': 0},
                      traits=[], uncommon=False)
    )
    weaponslist.append(
        getWeaponDict(name='Greatsword', bulk='2', type='MM', damage='1d12 S', hands='2', group='SWORD',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 20, 'copperPiece': 0},
                      traits=[], uncommon=False)
    )
    weaponslist.append(
        getWeaponDict(name='Guisarme', bulk='2', type='MM', damage='1d10 S', hands='2', group='POLEARM',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 14, 'copperPiece': 0},
                      traits=[], uncommon=False)
    )
    weaponslist.append(
        getWeaponDict(name='Halberd', bulk='2', type='MM', damage='1d10 P', hands='2', group='POLEARM',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 18, 'copperPiece': 0},
                      traits=[], uncommon=False)
    )
    weaponslist.append(
        getWeaponDict(name='Hatchet', bulk='L', type='MM', damage='1d6 S', hands='1', group='AXE',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 4, 'copperPiece': 0},
                      traits=[], uncommon=False)
    )
    weaponslist.append(
        getWeaponDict(name='Heavy shield bash', bulk='', type='MM', damage='1d4 B', hands='1', group='SHIELD',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 0, 'copperPiece': 0},
                      traits=[], uncommon=False)
    )
    weaponslist.append(
        getWeaponDict(name='Heavy shield boss', bulk='', type='MM', damage='1d6 B', hands='1', group='SHIELD',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 5, 'copperPiece': 0},
                      traits=[], uncommon=False)
    )
    weaponslist.append(
        getWeaponDict(name='Lance', bulk='2', type='MM', damage='1d8 P', hands='2', group='SPEAR',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 12, 'copperPiece': 0},
                      traits=[], uncommon=False)
    )

    weaponslist.append(
        getWeaponDict(name='Light hammer', bulk='L', type='MM', damage='1d6 B', hands='1', group='HAMMER',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 3, 'copperPiece': 0},
                      traits=[], uncommon=False)
    )
    weaponslist.append(
        getWeaponDict(name='Light pick', bulk='L', type='MM', damage='1d4 P', hands='1', group='PICK',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 4, 'copperPiece': 0},
                      traits=[], uncommon=False)
    )
    weaponslist.append(
        getWeaponDict(name='Light shield bash', bulk='', type='MM', damage='1d3 B', hands='1', group='SHIELD',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 0, 'copperPiece': 0},
                      traits=[], uncommon=False)
    )
    weaponslist.append(
        getWeaponDict(name='Light shield boss', bulk='', type='MM', damage='1d4 B', hands='1', group='SHIELD',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 4, 'copperPiece': 0},
                      traits=[], uncommon=False)
    )
    weaponslist.append(
        getWeaponDict(name='Light shield spikes', bulk='', type='MM', damage='1d4 P', hands='1', group='SHIELD',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 4, 'copperPiece': 0},
                      traits=[], uncommon=False)
    )
    weaponslist.append(
        getWeaponDict(name='Longsword', bulk='1', type='MM', damage='1d8 S', hands='1', group='SWORD',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 10, 'copperPiece': 0},
                      traits=[], uncommon=False)
    )
    weaponslist.append(
        getWeaponDict(name='Main–gauche', bulk='L', type='MM', damage='1d4 P', hands='1', group='KNIFE',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 5, 'copperPiece': 0},
                      traits=[], uncommon=False)
    )
    weaponslist.append(
        getWeaponDict(name='Maul', bulk='2', type='MM', damage='1d12 B', hands='2', group='HAMMER',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 26, 'copperPiece': 0},
                      traits=[], uncommon=False)
    )
    weaponslist.append(
        getWeaponDict(name='Pick', bulk='1', type='MM', damage='1d6 P', hands='1', group='PICK',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 7, 'copperPiece': 0},
                      traits=[], uncommon=False)
    )
    weaponslist.append(
        getWeaponDict(name='Ranseur', bulk='2', type='MM', damage='1d10 P', hands='2', group='POLEARM',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 14, 'copperPiece': 0},
                      traits=[], uncommon=False)
    )
    weaponslist.append(
        getWeaponDict(name='Rapier', bulk='1', type='MM', damage='1d6 P', hands='1', group='SWORD',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 15, 'copperPiece': 0},
                      traits=[], uncommon=False)
    )
    weaponslist.append(
        getWeaponDict(name='Sap', bulk='L', type='MM', damage='1d6 B', hands='1', group='CLUB',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 1, 'copperPiece': 0},
                      traits=[], uncommon=False)
    )
    weaponslist.append(
        getWeaponDict(name='Scimitar', bulk='L', type='MM', damage='1d6 S', hands='1', group='SWORD',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 11, 'copperPiece': 0},
                      traits=[], uncommon=False)
    )
    weaponslist.append(
        getWeaponDict(name='Scythe', bulk='2', type='MM', damage='1d10 S', hands='2', group='POLEARM',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 18, 'copperPiece': 0},
                      traits=[], uncommon=False)
    )
    weaponslist.append(
        getWeaponDict(name='Shortsword', bulk='L', type='MM', damage='1d6 P', hands='1', group='SWORD',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 9, 'copperPiece': 0},
                      traits=[], uncommon=False)
    )
    weaponslist.append(
        getWeaponDict(name='Starknife', bulk='L', type='MM', damage='1d4 P', hands='1', group='KNIFE',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 24, 'copperPiece': 0},
                      traits=[], uncommon=False)
    )
    weaponslist.append(
        getWeaponDict(name='Trident', bulk='1', type='MM', damage='1d8 P', hands='1', group='SPEAR',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 13, 'copperPiece': 0},
                      traits=[], uncommon=False)
    )
    weaponslist.append(
        getWeaponDict(name='War flail', bulk='2', type='MM', damage='1d10 B', hands='2', group='FLAIL',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 15, 'copperPiece': 0},
                      traits=[], uncommon=False)
    )
    weaponslist.append(
        getWeaponDict(name='Warhammer', bulk='1', type='MM', damage='1d8 B', hands='1', group='HAMMER',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 12, 'copperPiece': 0},
                      traits=[], uncommon=False)
    )
    weaponslist.append(
        getWeaponDict(name='Whip', bulk='1', type='MM', damage='1d4 S ', hands='1', group='FLAIL',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 1, 'copperPiece': 0},
                      traits=[], uncommon=False)
    )

    weaponslist.append(
        getWeaponDict(name='Blowgun', bulk='L', type='SR', damage='1 P ', hands='1', group='DART',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 1, 'copperPiece': 0},
                      traits=[], uncommon=False, reload=1, range=20)
    )
    weaponslist.append(
        getWeaponDict(name='Crossbow', bulk='1', type='SR', damage='1d8 P ', hands='2', group='BOW',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 30, 'copperPiece': 0},
                      traits=[], uncommon=False, reload=1, range=120)
    )
    weaponslist.append(
        getWeaponDict(name='Dart', bulk='L', type='SR', damage='1d4 P', hands='1', group='DART',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 0, 'copperPiece': 1},
                      traits=[], uncommon=False, reload=0, range=20)
    )
    weaponslist.append(
        getWeaponDict(name='Hand crossbow', bulk='L', type='SR', damage='1d6 P ', hands='1', group='BOW',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 25, 'copperPiece': 0},
                      traits=[], uncommon=False, reload=1, range=60)
    )
    weaponslist.append(
        getWeaponDict(name='Heavy crossbow', bulk='2', type='SR', damage='1d10 P ', hands='2', group='BOW',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 40, 'copperPiece': 0},
                      traits=[], uncommon=False, reload=2, range=120)
    )
    weaponslist.append(
        getWeaponDict(name='Javelin', bulk='L', type='SR', damage='1d6 P', hands='1', group='DART',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 1, 'copperPiece': 0},
                      traits=[], uncommon=False, reload=0, range=30)
    )
    weaponslist.append(
        getWeaponDict(name='Sling', bulk='L', type='SR', damage='1d6 B', hands='1', group='SLING',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 0, 'copperPiece': 0},
                      traits=[], uncommon=False, reload=1, range=30)
    )

    weaponslist.append(
        getWeaponDict(name='Composite longbow', bulk='2', type='MR', damage='1d8 P', hands='1', group='BOW',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 200, 'copperPiece': 0},
                      traits=[], uncommon=False, reload=0, range=100)
    )
    weaponslist.append(
        getWeaponDict(name='Composite shortbow', bulk='1', type='MR', damage='1d6 P', hands='1', group='BOW',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 140, 'copperPiece': 0},
                      traits=[], uncommon=False, reload=0, range=60)
    )
    weaponslist.append(
        getWeaponDict(name='Longbow', bulk='2', type='MR', damage='1d8 P', hands='1', group='BOW',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 60, 'copperPiece': 0},
                      traits=[], uncommon=False, reload=0, range=100)
    )
    weaponslist.append(
        getWeaponDict(name='Shortbow', bulk='1', type='MR', damage='1d6 P', hands='1', group='BOW',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 30, 'copperPiece': 0},
                      traits=[], uncommon=False, reload=0, range=60)
    )
    weaponslist.append(
        getWeaponDict(name='Clan dagger', bulk='L', type='SM', damage='1d4 P', hands='1', group='KNIFE',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 25, 'copperPiece': 0},
                      traits=[], uncommon=True)
    )
    weaponslist.append(
        getWeaponDict(name='Katar', bulk='L', type='SM', damage='1d4 P', hands='1', group='KNIFE',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 3, 'copperPiece': 0},
                      traits=[], uncommon=True)
    )
    weaponslist.append(
        getWeaponDict(name='Dogslicer', bulk='L', type='MM', damage='1d6 S', hands='1', group='SWORD',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 1, 'copperPiece': 0},
                      traits=[], uncommon=True)
    )
    weaponslist.append(
        getWeaponDict(name='Elven curve blade', bulk='2', type='MM', damage='1d8 S', hands='2', group='SWORD',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 38, 'copperPiece': 0},
                      traits=[], uncommon=True)
    )
    weaponslist.append(
        getWeaponDict(name='Filcher’s fork', bulk='L', type='MM', damage='1d4 P', hands='1', group='SPEAR',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 11, 'copperPiece': 0},
                      traits=[], uncommon=True)
    )
    weaponslist.append(
        getWeaponDict(name='Gnome hooked hammer', bulk='1', type='MM', damage='1d6 B', hands='1', group='HAMMER',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 18, 'copperPiece': 0},
                      traits=[], uncommon=True)
    )
    weaponslist.append(
        getWeaponDict(name='Horsechopper', bulk='2', type='MM', damage='1d8 S', hands='2', group='POLEARM',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 9, 'copperPiece': 0},
                      traits=[], uncommon=True)
    )
    weaponslist.append(
        getWeaponDict(name='Kama', bulk='L', type='MM', damage='1d6 S', hands='1', group='KNIFE',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 10, 'copperPiece': 0},
                      traits=[], uncommon=True)
    )
    weaponslist.append(
        getWeaponDict(name='Katana', bulk='1', type='MM', damage='1d8 S', hands='1', group='SWORD',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 20, 'copperPiece': 0},
                      traits=[], uncommon=True)
    )
    weaponslist.append(
        getWeaponDict(name='Kukri', bulk='L', type='MM', damage='1d6 S', hands='1', group='KNIFE',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 6, 'copperPiece': 0},
                      traits=[], uncommon=True)
    )
    weaponslist.append(
        getWeaponDict(name='Nunchaku', bulk='L', type='MM', damage='1d6 B', hands='1', group='CLUB',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 2, 'copperPiece': 0},
                      traits=[], uncommon=True)
    )
    weaponslist.append(
        getWeaponDict(name='Orc knuckle dagger', bulk='L', type='MM', damage='1d6 P', hands='1', group='KNIFE',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 7, 'copperPiece': 0},
                      traits=[], uncommon=True)
    )
    weaponslist.append(
        getWeaponDict(name='Sai', bulk='L', type='MM', damage='1d4 P', hands='1', group='KNIFE',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 6, 'copperPiece': 0},
                      traits=[], uncommon=True)
    )
    weaponslist.append(
        getWeaponDict(name='Spiked chain', bulk='1', type='MM', damage='1d8 S', hands='2', group='FLAIL',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 28, 'copperPiece': 0},
                      traits=[], uncommon=True)
    )
    weaponslist.append(
        getWeaponDict(name='Temple sword', bulk='1', type='MM', damage='1d8 S', hands='1', group='SWORD',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 14, 'copperPiece': 0},
                      traits=[], uncommon=True)
    )
    weaponslist.append(
        getWeaponDict(name='Dwarven waraxe', bulk='2', type='EM', damage='1d8 S', hands='1', group='AXE',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 25, 'copperPiece': 0},
                      traits=[], uncommon=True)
    )
    weaponslist.append(
        getWeaponDict(name='Gnome flickmace', bulk='2', type='EM', damage='1d8 B', hands='1', group='FLAIL',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 24, 'copperPiece': 0},
                      traits=[], uncommon=True)
    )
    weaponslist.append(
        getWeaponDict(name='Orc necksplitter', bulk='1', type='EM', damage='1d8 S', hands='1', group='KNIFE',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 21, 'copperPiece': 0},
                      traits=[], uncommon=True)
    )
    weaponslist.append(
        getWeaponDict(name='Sawtooth sabre', bulk='L', type='EM', damage='1d6 S', hands='1', group='SWORD',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 50, 'copperPiece': 0},
                      traits=[], uncommon=True)
    )
    weaponslist.append(
        getWeaponDict(name='Halfling sling staff', bulk='1', type='MR', damage='1d10 B', hands='2', group='SLING',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 50, 'copperPiece': 0},
                      traits=[], uncommon=True, range=80, reload=1)
    )
    weaponslist.append(
        getWeaponDict(name='Shuriken', bulk='', type='MR', damage='1d10 B', hands='1', group='DART',
                      price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 0, 'copperPiece': 1},
                      traits=[], uncommon=True, range=20, reload=0)
    )
    stringweapons = ''
    i = 1
    j = 16

    for weapondict in weaponslist:
        stringprice = '{"model": "core.price", "pk": ' + str(j) + ', "fields": {"platinumPiece": ' + str(
            weapondict['price']['platinumPiece']) + ', "goldPiece": ' + str(
            weapondict['price']['goldPiece']) + ', "silverPiece": ' + str(
            weapondict['price']['silverPiece']) + ', "copperPiece": ' + str(
            weapondict['price']['copperPiece']) + '}},\n'

        stringweapon = '{"model": "core.weapon", "pk": ' + str(i) + ', "fields": {"name": "' + weapondict[
            'name'] + '", "price": ' + str(j) + ', "bulk": "' + weapondict['bulk'] + '", "type": "' + weapondict[
                          'type'] + '", "damage": "' + weapondict['damage'] + '", "hands": "' + str(
            weapondict['hands']) + '", "group": "' + str(
            weapondict['group']) + '", "traits": ' + str(
            weapondict['traits']) + ', "uncommon": "' + str(weapondict['uncommon']) \
                       +'", "reload": "' + str(weapondict['reload']) +'", "range": "' + str(weapondict['range']) + '"}},\n'

        i += 1
        j += 1
        stringweapons += stringprice + stringweapon

    fixtureweapons = '[\n' + stringweapons[:len(stringweapons) - 2] + '\n]'

    return fixtureweapons


def generatefixtureammunitions():

    ammolist = []
    ammolist.append(
        getAmmoDict(name='blowgun darts', bulk='L',
                    price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 0, 'copperPiece': 5},
                    ammoForWeapons=[49])
    )
    ammolist.append(
        getAmmoDict(name='bolts', bulk='L',
                    price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 1, 'copperPiece': 0},
                    ammoForWeapons=[50, 52, 53])
    )
    ammolist.append(
        getAmmoDict(name='sling bullets', bulk='L',
                    price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 0, 'copperPiece': 1},
                    ammoForWeapons=[55, 79])
    )
    ammolist.append(
        getAmmoDict(name='arrows', bulk='L',
                    price={'platinumPiece': 0, 'goldPiece': 0, 'silverPiece': 1, 'copperPiece': 0},
                    ammoForWeapons=[56, 57, 58, 59])
    )

    stringammos = ''
    i = 1
    j = 96

    for ammodict in ammolist:
        stringprice = '{"model": "core.price", "pk": ' + str(j) + ', "fields": {"platinumPiece": ' + str(
            ammodict['price']['platinumPiece']) + ', "goldPiece": ' + str(
            ammodict['price']['goldPiece']) + ', "silverPiece": ' + str(
            ammodict['price']['silverPiece']) + ', "copperPiece": ' + str(
            ammodict['price']['copperPiece']) + '}},\n'

        stringammo = '{"model": "core.ammunition", "pk": ' + str(i) + ', "fields": {"name": "' + ammodict[
            'name'] + '", "price": ' + str(j) + ', "bulk": "' + ammodict['bulk'] + '", "ammoForWeapons": ' + str(ammodict[
                          'ammoForWeapons']) + '}},\n'
        i += 1
        j += 1
        stringammos += stringprice + stringammo

    fixtureammos = '[\n' + stringammos[:len(stringammos) - 2] + '\n]'
    return fixtureammos

def main():
    print(generatefixtureammunitions())

if __name__ == "__main__":
    main()
