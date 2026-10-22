from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from inventory.models import AssemblyStatusOption, PaintingStatusOption
from django.db import transaction


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_default_options(sender, instance, created, **kwargs):
    if not created:
        return

    assembly_status_options = [
        "Unassembled",
        "In Progress",
        "Assembled",
    ]

    painting_status_options = [
        "Unpainted",
        "Primed",
        "Base Coated",
        "Shaded",
        "Highlighted",
    ]

    with transaction.atomic():
        for index, assembly_status_option in enumerate(
            assembly_status_options, start=1
        ):
            AssemblyStatusOption.objects.create(
                owner=instance,
                name=assembly_status_option,
                position=index,
            )

        for index, painting_status_option in enumerate(
            painting_status_options, start=1
        ):
            PaintingStatusOption.objects.create(
                owner=instance,
                name=painting_status_option,
                position=index,
            )
