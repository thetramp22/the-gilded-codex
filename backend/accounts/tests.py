from django.test import TestCase
from .models import User


class UserTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.testuser = User.objects.create(
            username="Tester01",
            first_name="Test",
            last_name="Testerson",
            email="test@test.com",
            is_staff=False,
        )

    def test_user_creation(self):
        self.assertEqual(self.testuser.assembly_status_options.count(), 3)
        self.assertEqual(self.testuser.painting_status_options.count(), 5)

        expected_assembly_options = [
            "Unassembled",
            "In Progress",
            "Assembled",
        ]
        actual_assembly_options = list(
            self.testuser.assembly_status_options.order_by("position").values_list(
                "name", flat=True
            )
        )
        self.assertEqual(expected_assembly_options, actual_assembly_options)

        expected_painting_options = [
            "Unpainted",
            "Primed",
            "Base Coated",
            "Shaded",
            "Highlighted",
        ]
        actual_painting_options = list(
            self.testuser.painting_status_options.order_by("position").values_list(
                "name", flat=True
            )
        )
        self.assertEqual(
            expected_painting_options,
            actual_painting_options,
        )

    def test_user_update(self):
        self.testuser.first_name = "Test II"
        self.testuser.save()

        self.assertEqual(self.testuser.assembly_status_options.count(), 3)
        self.assertEqual(self.testuser.painting_status_options.count(), 5)
