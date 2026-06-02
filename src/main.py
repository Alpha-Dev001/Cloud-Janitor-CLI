from config import ENVIRONMENT
from models import CloudResource
from utils import setup_logger


logger = setup_logger()


def run_janitor_service() -> None:
    logger.info(
        f"Starting Cloud Janitor in [{ENVIRONMENT}] mode"
    )

    resources = [
        CloudResource(
            "vol-123",
            "EBS Volume",
            "orphaned",
            logger
        ),
        CloudResource(
            "i-456",
            "EC2 Instance",
            "active",
            logger
        ),
        CloudResource(
            "vol-789",
            "EBS Volume",
            "idle",
            logger
        )
    ]

    flagged_resources = []

    for resource in resources:
        if resource.audit():
            flagged_resources.append(resource)

    with open(
        "janitor_audit_report.txt",
        "w"
    ) as report:
        report.write(
            f"Cloud Janitor Report ({ENVIRONMENT})\n"
        )

        report.write("=" * 40 + "\n")

        for resource in flagged_resources:
            report.write(
                f"{resource.resource_id} "
                f"- {resource.resource_type}\n"
            )

        report.write(
            f"\nTotal Risks: {len(flagged_resources)}\n"
        )

    logger.info("Audit report generated")


if __name__ == "__main__":
    run_janitor_service()