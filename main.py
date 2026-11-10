import logging

from src.user_data_pipeline.pipeline import run_pipeline


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )
    run_pipeline()


if __name__ == "__main__":
    main()
