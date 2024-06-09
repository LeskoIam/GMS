# Documentation is like sex.
# When it's good, it's very good.
# When it's bad, it's better than nothing.
# When it lies to you, it may be a while before you realize something's wrong.
import logging

import pytest
from django.urls import reverse

from gms_app.models import Garden, GardenBed, Plant, Planting

log = logging.getLogger(__name__)


@pytest.mark.parametrize(("viewname", "kwargs_"), [("home", {}), ("garden_list", {}), ("garden_detail", {"pk": 1})])
@pytest.mark.django_db()
def test_views_loads(client, viewname, kwargs_):
    """We want to know if basic views load without error.

    :param viewname: name of the view to test
    :param kwargs_: any required arguments like primary key (PK)
    """
    log.info("Testing view '%s' with kwargs_ '%s'", viewname, kwargs_)
    uri = reverse(viewname, kwargs=kwargs_ if kwargs_ else None)
    resp = client.get(uri)
    assert resp.status_code == 200
