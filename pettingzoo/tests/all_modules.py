from pettingzoo.atari import *

from pettingzoo.classic import *

from pettingzoo.gamma import *

from pettingzoo.mpe import *

from pettingzoo.magent import *

from pettingzoo.sisl import *

all_prefixes = ["atari", "classic", "gamma", "magent", "mpe", "sisl"]

all_environments = {
    "atari/boxing": boxing_v0,
    "atari/combat_tank": combat_tank_v0,
    "atari/combat_plane": combat_plane_v0,
    "atari/double_dunk": double_dunk_v0,
    "atari/entombed_cooperative": entombed_cooperative_v0,
    "atari/entombed_competitive": entombed_competitive_v0,
    "atari/flag_capture": flag_capture_v0,
    "atari/joust": joust_v0,
    "atari/ice_hockey": ice_hockey_v0,
    "atari/maze_craze": maze_craze_v0,
    "atari/mario_bros": mario_bros_v0,
    "atari/othello": othello_v0,
    "atari/pong_classic": pong_classic_v0,
    "atari/pong_basketball": pong_basketball_v0,
    "atari/pong_foozpong": pong_foozpong_v0,
    "atari/pong_quadrapong": pong_quadrapong_v0,
    "atari/pong_volleyball": pong_volleyball_v0,
    "atari/space_invaders": space_invaders_v0,
    "atari/space_war": space_war_v0,
    "atari/surround": surround_v0,
    "atari/tennis": tennis_v0,
    "atari/video_checkers": video_checkers_v0,
    "atari/wizard_of_wor": wizard_of_wor_v0,
    "atari/warlords": warlords_v0,

    "classic/chess": chess_v0,
    "classic/rps": rps_v0,
    "classic/rpsls": rpsls_v0,
    "classic/connect_four": connect_four_v0,
    "classic/tictactoe": tictactoe_v0,
    "classic/leduc_holdem": leduc_holdem_v0,
    "classic/mahjong": mahjong_v0,
    "classic/texas_holdem": texas_holdem_v0,
    "classic/texas_holdem_no_limit": texas_holdem_no_limit_v0,
    "classic/uno": uno_v0,
    "classic/dou_dizhu": dou_dizhu_v0,
    "classic/gin_rummy": gin_rummy_v0,
    "classic/go": go_v0,
    "classic/hanabi": hanabi_v0,
    "classic/backgammon": backgammon_v0,

    "gamma/knights_archers_zombies": knights_archers_zombies_v0,
    "gamma/pistonball": pistonball_v0,
    "gamma/cooperative_pong": cooperative_pong_v0,
    "gamma/prison": prison_v0,
    "gamma/prospector": prospector_v0,

    "magent/battle": battle_v0,
    "magent/pursuit": adversarial_pursuit_v0,
    "magent/gather": gather_v0,
    "magent/combined_arms": combined_arms_v0,
    "magent/tiger": tiger_deer_v0,
    "magent/battlefield": battlefield_v0,

    "mpe/simple_adversary": simple_adversary_v0,
    "mpe/simple_crypto": simple_crypto_v0,
    "mpe/simple_push": simple_push_v0,
    "mpe/simple_reference": simple_reference_v0,
    "mpe/simple_speaker_listener": simple_speaker_listener_v0,
    "mpe/simple_spread": simple_spread_v0,
    "mpe/simple_tag": simple_tag_v0,
    "mpe/simple_world_comm": simple_world_comm_v0,
    "mpe/simple": simple_v0,

    "sisl/multiwalker": multiwalker_v0,
    "sisl/waterworld": waterworld_v0,
    "sisl/pursuit": pursuit_v0,
}
