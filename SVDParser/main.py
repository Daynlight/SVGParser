from typeguard import typechecked
import config


@typechecked
def main():
  print(config.SRC_PATH)
  pass


main()
