import argparse
import pathlib
import os
from aoe_opening_data import aoe_replay_stats

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Get quick stats from a folder of AoE2 DE Replays")
    parser.add_argument("input", type=pathlib.Path, help="Input Folder")
    parser.add_argument("-u", "--include_units", action="store_true")
    parser.add_argument("-U", "--only_unique_units", action="store_true")
    parser.add_argument("-b", "--include_buildings", action="store_true")
    parser.add_argument("-B", "--only_unique_buildings", action="store_true")
    parser.add_argument("-t", "--include_techs", action="store_true")
    parser.add_argument("-o", "--include_player_openings", action="store_true")
    args = parser.parse_args()

    count = 0
    for filename in os.listdir(args.input):
      f = os.path.join(args.input, filename)
      if os.path.isfile(f):
        fname = os.path.splitext(f)
        if fname[1] == ".aoe2record":
          print(f"Starting rec: {count}")
          count += 1
          players, header, civs, loser_id = aoe_replay_stats.parse_replay(f)
          player_strategies = aoe_replay_stats.guess_strategy(players)
          csv = aoe_replay_stats.print_to_csv(players,
              header,
              civs,
              player_strategies,
              args.include_units,
              args.only_unique_units,
              args.include_buildings,
              args.only_unique_buildings,
              args.include_techs,
              args.include_player_openings)
          with open(fname[0]+".csv", "w") as f:
            f.write(csv)


