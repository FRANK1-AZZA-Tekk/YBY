from .degradation import DegradationStateMachine
from .events import EventBus, YBYEvent
from .observability import get_logger
from .privacy import PrivacyPolicy
from .routing import Router, RoutingContext


def main() -> None:
    logger = get_logger()
    router = Router()
    privacy = PrivacyPolicy()
    degradation = DegradationStateMachine()
    bus = EventBus()

    event = YBYEvent(
        source="yby-core",
        event_type="system.started",
        payload={"state": degradation.state.value},
    )
    bus.publish(event)

    context = RoutingContext(text="status", privacy_level="P1")
    decision = router.decide(context)
    policy = privacy.classify(context.privacy_level)
    logger.info(
        "YBY ZERO iniciado provider=%s privacy=%s",
        decision.provider,
        policy.level,
    )


if __name__ == "__main__":
    main()
