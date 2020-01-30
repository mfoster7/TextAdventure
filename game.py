import world, items, actions

last_action = " "
def getLastAction():
    return last_action
def play():
    world.load_tiles()
    from player import Player
    player = Player()
    room = world.tile_exists(player.location_x, player.location_y)
    print(room.intro_text())
    while player.is_alive() and not player.victory:
        room = world.tile_exists(player.location_x, player.location_y)
        room.modify_player(player)
        # Check again since the room could have changed the player's state
        if player.is_alive() and not player.victory:
            count = 0
            total_actions = 0
            print('\033[2m' + "Choose an action:")
            available_actions = room.available_actions()
            for action in available_actions:
                print(action)
            action_input = input('Action: ' + '\033[0m')
            for action in available_actions:
                total_actions+1
                if action_input == action.hotkey:
                    player.do_action(action, **action.kwargs)
                    last_action = action_input
                    #print(last_action)
                    break
                else:
                    count+1
            if(total_actions == count):
                    print("That input is not an available action \n")

if __name__ == "__main__":
    play()
