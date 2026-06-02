import logging

from src.models.cloud_resource import CloudResource


logger = logging.getLogger("test")


def test_orphaned_resource_returns_true():
    resource = CloudResource(
        "vol-123",
        "EBS",
        "orphaned",
        logger
    )

    assert resource.audit() is True


def test_idle_resource_returns_true():
    resource = CloudResource(
        "vol-123",
        "EBS",
        "idle",
        logger
    )

    assert resource.audit() is True


def test_active_resource_returns_false():
    resource = CloudResource(
        "i-123",
        "EC2",
        "active",
        logger
    )

    assert resource.audit() is False
    