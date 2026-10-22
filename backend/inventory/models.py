from django.db import models
from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.core.validators import MinValueValidator

# Create your models here.


class InventoryItem(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="inventory_items",
    )
    name = models.CharField(max_length=200)
    manufacturer = models.CharField(max_length=150, blank=True)
    product_name = models.CharField(max_length=200, blank=True)

    class ItemType(models.TextChoices):
        MINIATURE = "MINI", _("Miniature")
        SUPPLY = "SUPP", _("Supply")

    item_type = models.CharField(max_length=4, choices=ItemType.choices)

    quantity = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1)])
    purchase_date = models.DateField(null=True, blank=True)
    purchase_price = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        null=True,
        blank=True,
    )
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class AssemblyStatusOption(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="assembly_status_options",
    )
    name = models.CharField(max_length=200)
    position = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class PaintingStatusOption(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="painting_status_options",
    )
    name = models.CharField(max_length=200)
    position = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class MiniatureDetails(models.Model):
    inventory_item = models.OneToOneField(
        InventoryItem,
        on_delete=models.CASCADE,
        related_name="miniature_details",
    )
    game_system = models.CharField(max_length=200, blank=True)
    faction = models.CharField(max_length=200, blank=True)
    unit_name = models.CharField(max_length=200, blank=True)
    models_per_unit = models.PositiveIntegerField(
        default=1, validators=[MinValueValidator(1)]
    )
    assembly_status = models.ForeignKey(
        AssemblyStatusOption,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="miniatures",
    )
    painting_status = models.ForeignKey(
        PaintingStatusOption,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="miniatures",
    )

    class Meta:
        verbose_name_plural = "Miniature Details"


class SupplyDetails(models.Model):
    inventory_item = models.OneToOneField(
        InventoryItem,
        on_delete=models.CASCADE,
        related_name="supply_details",
    )

    class Category(models.TextChoices):
        PAINT = "PNT", _("Paint")
        BRUSH = "BRSH", _("Brush")
        TOOL = "TOOL", _("Tool")
        BASINGMATERIAL = "BASE", _("Basing Material")
        OTHER = "OTHR", _("Other")

    category = models.CharField(max_length=4, choices=Category.choices)

    class Meta:
        verbose_name_plural = "Supply Details"
