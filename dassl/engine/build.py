from dassl.utils import Registry, check_availability

TRAINER_REGISTRY = Registry("TRAINER")


def build_trainer(cfg):
    avai_trainers = TRAINER_REGISTRY.registered_names()
    check_availability(cfg.TRAINER.NAME, avai_trainers)
    if cfg.VERBOSE:
        print("Loading trainer: {}".format(cfg.TRAINER.NAME))
    print("YYYYYYYYYYYYYYYYYYYYYYYY:", TRAINER_REGISTRY.get(cfg.TRAINER.NAME)(cfg)) #<trainers.coop.CoOp object at 0x7fcd8f06d040>
    return TRAINER_REGISTRY.get(cfg.TRAINER.NAME)(cfg)

