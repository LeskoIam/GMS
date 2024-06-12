# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.
import logging

import pytest
from django.urls import reverse

from gms_app.models import Garden, GardenBed, Plant, Planting

log = logging.getLogger(__name__)


@pytest.mark.parametrize(
    ("view_name", "heading", "kwargs_"),
    [
        ("home", "GMS home", {}),
        ("garden_list", "List of Gardens", {}),
        ("garden_detail", "Garden details", {"pk": 1}),
        ("add_plant", "Add Plant", {}),
        ("add_plant_to_bed", "Add Plant to Garden Bed", {}),
    ],
)
@pytest.mark.django_db()
def test_view_loads(client, view_name, heading, kwargs_):
    """We want to know if basic views load without error.

    :param view_name: name of the view to test
    :param heading: heading of the view
    :param kwargs_: any required arguments like primary key (PK)
    """
    uri = reverse(view_name, kwargs=kwargs_ if kwargs_ else None)
    log.info("Testing view '%s' with heading '%s' and kwargs_ '%s'. <uri: %s>", view_name, heading, kwargs_, uri)

    resp = client.get(uri)

    assert resp.status_code == 200

    log.info("Heading '%s' in view source", heading)
    assert heading in resp.content.decode()
