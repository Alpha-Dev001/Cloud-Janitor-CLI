from logging import Logger


class CloudResource:
    def __init__(
        self,
        resource_id: str,
        resource_type: str,
        status: str,
        logger: Logger
    ) -> None:
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.status = status
        self.logger = logger

    def audit(self) -> bool:
        if self.status in ("orphaned", "idle"):
            self.logger.warning(
                f"Resource {self.resource_id} "
                f"({self.resource_type}) is {self.status}"
            )
            return True

        self.logger.info(
            f"Resource {self.resource_id} "
            f"({self.resource_type}) is compliant"
        )

        return False