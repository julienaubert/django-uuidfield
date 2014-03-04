import uuid
from django.core import serializers

from django.db import IntegrityError
from django.test import TestCase

import six
from uuidfield.tests.forms import ManualUUIDForm
from uuidfield.tests.models import (AutoUUIDField, ManualUUIDField,
    NamespaceUUIDField, BrokenNamespaceUUIDField, HyphenatedUUIDField,
    AutoUUIDFieldVersion1, BlankManualUUIDField)


class UUIDFieldTestCase(TestCase):

    def test_auto_uuid1(self):
        obj = AutoUUIDFieldVersion1.objects.create()
        self.assertTrue(obj.uuid)
        self.assertEquals(len(obj.uuid.hex), 32)
        self.assertTrue(isinstance(obj.uuid, uuid.UUID))
        self.assertEquals(obj.uuid.version, 1)

    def test_auto_uuid4(self):
        obj = AutoUUIDField.objects.create()
        self.assertTrue(obj.uuid)
        self.assertEquals(len(obj.uuid.hex), 32)
        self.assertTrue(isinstance(obj.uuid, uuid.UUID))
        self.assertEquals(obj.uuid.version, 4)

    def test_raises_exception(self):
        self.assertRaises(IntegrityError, ManualUUIDField.objects.create)

    def test_manual(self):
        obj = ManualUUIDField.objects.create(uuid=uuid.uuid4())
        self.assertTrue(obj)
        self.assertEquals(len(obj.uuid.hex), 32)
        self.assertTrue(isinstance(obj.uuid, uuid.UUID))
        self.assertEquals(obj.uuid.version, 4)

    def test_namespace(self):
        obj = NamespaceUUIDField.objects.create()
        self.assertTrue(obj)
        self.assertEquals(len(obj.uuid.hex), 32)
        self.assertTrue(isinstance(obj.uuid, uuid.UUID))
        self.assertEquals(obj.uuid.version, 5)

    def test_broken_namespace(self):
        self.assertRaises(ValueError, BrokenNamespaceUUIDField.objects.create)

    def test_hyphenated(self):
        obj = HyphenatedUUIDField.objects.create(name='test')
        uuid = obj.uuid

        self.assertTrue('-' in six.text_type(uuid))
        self.assertTrue('-' in str(uuid))

        self.assertEquals(len(uuid), 36)

        # ensure the hyphens don't affect re-saving object
        obj.name = 'shoe'
        obj.save()

        obj = HyphenatedUUIDField.objects.get(uuid=obj.uuid)

        self.assertTrue(obj.uuid, uuid)
        self.assertTrue(obj.name, 'shoe')

    def test_can_use_hyphenated_uuids_in_filter_and_get(self):
        obj = AutoUUIDField.objects.create()
        obj_uuid = uuid.UUID(str(obj.uuid))
        self.assertTrue('-' in six.text_type(obj_uuid))
        self.assertTrue('-' in str(obj_uuid))
        inserted_obj = AutoUUIDField.objects.get(uuid=obj_uuid)
        filtered_obj = AutoUUIDField.objects.filter(uuid=obj_uuid)[0]
        self.assertEqual(inserted_obj.uuid, obj_uuid)
        self.assertEqual(filtered_obj.uuid, obj_uuid)

    def test_serialize_roundtrip(self):
        obj = AutoUUIDField.objects.create()
        serial_str = serializers.serialize("json",
                                           AutoUUIDField.objects.all())
        models = list(serializers.deserialize("json", serial_str))
        self.assertEqual(len(models), 1)
        self.assertEqual(models[0].object.uuid, obj.uuid)

    def test_serialize_roundtrip_when_blank(self):
        obj = BlankManualUUIDField.objects.create()
        assert obj.uuid is None
        serial_str = serializers.serialize("json",
                                           BlankManualUUIDField.objects.all())
        models = list(serializers.deserialize("json", serial_str))
        self.assertEqual(len(models), 1)
        self.assertEqual(models[0].object.uuid, obj.uuid)


class FormUUIDField(TestCase):

    def test_formfield(self):
        form = ManualUUIDForm({'uuid': uuid.uuid4().hex})
        self.assertTrue(form.is_valid())
        form = ManualUUIDForm({'uuid': ''})
        self.assertFalse(form.is_valid())
