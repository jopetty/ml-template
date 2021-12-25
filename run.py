import dotenv
import hydra
from omegaconf import DictConfig

dotenv.load_dotenv(override=True)


@hydra.main(config_path="conf/", config_name="config.yaml")
def main(cfg: DictConfig):

    from src.utils import utils

    if cfg.get("print_config"):
        utils.print_config(cfg, resolve=True)


if __name__ == "__main__":
    main()
