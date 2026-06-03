import json
from config import ENVIRONMENT, DRY_RUN
from models import CloudResource
from utils import setup_logger

logger = setup_logger()


def run_janitor_service() -> None:
    logger.info(f"Starting Cloud Janitor in [{ENVIRONMENT}] mode")

    resources = [
        CloudResource("vol-123", "EBS Volume", "orphaned", logger),
        CloudResource("i-456", "EC2 Instance", "active", logger),
        CloudResource("vol-789", "EBS Volume", "idle", logger)
    ]

    flagged_resources = []
    report_data = []

    for resource in resources:

        if DRY_RUN:
            logger.warning(f"[DRY RUN] Checking {resource.resource_id}")

        if resource.audit():
            flagged_resources.append(resource)

            report_data.append({
                "resource_id": resource.resource_id,
                "type": resource.resource_type,
                "status": resource.status,
                "risk_score": resource.risk_score()
            })

    with open("janitor_audit_report.json", "w") as report:
        json.dump({
            "environment": ENVIRONMENT,
            "total_risks": len(flagged_resources),
            "resources": report_data
        }, report, indent=2)

    logger.info("Audit report generated successfully")


if __name__ == "__main__":
    run_janitor_service()