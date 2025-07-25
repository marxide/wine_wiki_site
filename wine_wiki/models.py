from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import default, slugify
from django.utils.translation import autoreload_started
from django.urls import reverse


class Producer(models.Model):
    """represents a producer"""

    producer_name = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    description = models.TextField(help_text="Description of the producer")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.producer_name)
        super(Producer, self).save(*args, **kwargs)


class Section(models.Model):
    """
    Represents the wine list structure
    """

    order = models.IntegerField(unique=True)
    section = models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return str(self.section)


class Subsection(models.Model):
    """
    mixin class for wine list subcategories
    """

    section = models.ForeignKey(Section, on_delete=models.PROTECT)
    subsection = models.CharField(max_length=100, primary_key=True)
    order = models.IntegerField()

    def __str__(self):
        return str(self.subsection)


class Wine(models.Model):
    """base class representing a wine object"""

    line_num_tot = models.IntegerField(
        null=True, default=-1
    )  # -1 implies missing number, can apply a default sort by name in view
    page_num = models.IntegerField(null=False, default=-1)
    page_line_num = models.IntegerField(null=False, default=-1)
    section = models.ForeignKey(Section, on_delete=models.PROTECT, null=True)
    subsection = models.ForeignKey(Subsection, on_delete=models.PROTECT, null=True)
    subsubsection = models.CharField(
        null=False, default=""
    )  # ' ' implies it requires assignment.
    vintage = models.CharField(max_length=4, blank=True, null=True, default=None)
    merged_text_ext = models.TextField(
        blank=True,
        null=True,
        default=None,
    )  # left over from field extractoin, also here for debugging

    base_year = models.IntegerField(
        blank=True,
        null=True,
        default=None,
    )
    cuvee_name = models.TextField(blank=True, null=True, default=None)
    disgorg_year = models.IntegerField(blank=True, null=True, default=None)
    price = models.IntegerField(blank=False)
    merged_text = models.TextField(
        blank=True,
        null=True,
        default=None,
    )  # the initial extracted text, useful for downstream debugging
    producer = models.CharField(max_length=100, blank=True, null=True, default=None)
    dryness = models.CharField(max_length=100, blank=True, null=True, default=None)
    country = models.CharField(max_length=100, blank=True, null=True, default=None)
    state = models.CharField(max_length=100, blank=True, null=True, default=None)
    region = models.CharField(max_length=100, blank=True, null=True, default=None)
    subregion = models.CharField(max_length=100, blank=True, null=True, default=None)
    commune = models.CharField(max_length=100, blank=True, null=True, default=None)
    vineyard = models.CharField(max_length=100, blank=True, null=True, default=None)
    wine_name = models.CharField(max_length=100, blank=True, null=True, default=None)
    variety = models.CharField(max_length=100, blank=True, null=True, default=None)
    style = models.CharField(max_length=100, blank=True, null=True, default=None)
    classification = models.CharField(
        max_length=100, blank=True, null=True, default=None
    )
    volume = models.CharField(max_length=100, blank=True, null=True, default=None)
    series = models.CharField(max_length=100, blank=True, null=True, default=None)
    bpos_key = models.CharField(max_length=100, blank=True, null=True, default=None)
    description = models.TextField(blank=True, null=True, default=None)
    is_published = models.BooleanField(default=False, verbose_name="Publish?")
    created_on = models.DateTimeField(
        auto_now_add=True
    )  # date added to website database

    """represents a wine wiki wine"""

    def get_absolute_url(self):
        return reverse("wine", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.vintage} {self.wine_name} {self.region} {self.subregion}"

    def winesearcher_str(self):
        """assemble a string that matches winesearcher"""
        return f"{self.producer} {self.wine_name} {self.variety} {self.subregion} {self.region}/{self.vintage}".replace(
            " ", "+"
        ).replace("++", "+")  # in the event of null fields

    def search_eng_str(self):
        """assemble a string that matches winesearcher"""
        return f"{self.producer} {self.wine_name} {self.variety} {self.subregion} {self.region} {self.vintage}".replace(
            " ", "+"
        ).replace("++", "+")  # in the event of null fields
