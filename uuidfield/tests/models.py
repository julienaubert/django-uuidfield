import uuid
from django.db import models
from uuidfield import UUIDField


class AutoUUIDField(models.Model):
    uuid = UUIDField(auto=True)


class AutoUUIDFieldVersion1(models.Model):
    uuid = UUIDField(auto=True, version=1)


class HyphenatedUUIDField(models.Model):
    uuid = UUIDField(auto=True, hyphenate=True)
    name = models.CharField(max_length=16)


class ManualUUIDField(models.Model):
    uuid = UUIDField(auto=False)


class BlankManualUUIDField(models.Model):
    # note: django recommends char-based-fields to have null=False
    # however, UUIDField sets uuid to None if blank is True instead of ''
    # therefore null=True is unfortunately required.
    uuid = UUIDField(auto=False, blank=True, null=True)


class NamespaceUUIDField(models.Model):
    uuid = UUIDField(auto=True, namespace=uuid.NAMESPACE_URL, version=5)


class BrokenNamespaceUUIDField(models.Model):
    uuid = UUIDField(auto=True, namespace='lala', version=5)
