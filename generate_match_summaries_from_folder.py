import argparse
import pathlib
import os
from aoe_opening_data import aoe_replay_stats
from mgz import summary

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Get quick stats from a folder of AoE2 DE Replays")
    parser.add_argument("input", type=pathlib.Path, help="Input Folder")
    parser.add_argument("-u", "--include-units", action="store_true")
    parser.add_argument("-U", "--only-unique-units", action="store_true")
    parser.add_argument("-b", "--include-buildings", action="store_true")
    parser.add_argument("-B", "--only-unique-buildings", action="store_true")
    parser.add_argument("-t", "--include-techs", action="store_true")
    parser.add_argument("-o", "--include-player-openings", action="store_true")
    parser.add_argument("-s", "--single-file-output", action="store_true")
    args = parser.parse_args()

    count = 0
    if args.single_file_output:
      single_file = open(os.path.join(args.input, "output.csv"), "w")
    for filename in os.listdir(args.input):
      f = os.path.join(args.input, filename)
      if os.path.isfile(f):
        fname = os.path.splitext(f)
        if fname[1] == ".aoe2record":
          print(f"Starting rec: {count}")
          count += 1
          with open(f, "rb") as handle:
            game_summary = summary.FullSummary(handle)
          players, header, civs, loser_id = aoe_replay_stats.parse_replay(f)
          player_strategies = aoe_replay_stats.guess_strategy(players)
          csv = aoe_replay_stats.print_to_csv(players,
              game_summary,
              header,
              civs,
              player_strategies,
              args.include_units,
              args.only_unique_units,
              args.include_buildings,
              args.only_unique_buildings,
              args.include_techs,
              args.include_player_openings)
          if args.single_file_output:
            single_file.write(csv)
          else:
            with open(fname[0]+".csv", "w") as f:
              f.write(csv)


