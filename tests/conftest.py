import logging
import os
from datetime import datetime

import pytest

from gms_app.models import Garden, GardenBed, Plant

log = logging.getLogger(__name__)


####################################
# pytest-html report customization #
####################################
@pytest.hookimpl(optionalhook=True)
def pytest_html_report_title(report):
    """Set html report title."""
    now = datetime.strftime(datetime.now(), "%d-%m-%Y %H:%M:%S")
    report.title = f"Test run at {now}"


# @pytest.hookimpl(optionalhook=True)
# def pytest_html_results_table_header(cells):
#     """For html report insert 'Test Case ID' column."""
#     cells.insert(2, "<th>Test Case ID</th>")


# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     """For html report generate TestRail links to test case/s as set with @pytestrail.case("CxxXXxx") decorator."""
#     outcome = yield
#     tr_ids = [m.kwargs["ids"] for m in item.own_markers if m.name == "testrail"]
#     if len(tr_ids) != 0:
#         tr_link = "https://etrel.testrail.io/index.php?/cases/view/"
#         tr_links = "&nbsp;".join([f"<a href='{tr_link + tr_id[1:]}' target='_blank'>{tr_id}</a>" for tr_id in tr_ids[0]])  # noqa
#     else:
#         tr_links = "Use '@pytestrail.case('&lt;case_id&gt;')' to mark test with TestRail test ID"
#     outcome._result.test_rail_links = tr_links


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    """Configure pytest test run."""
    report_base_dir = "tests/test_run_results"
    test_run_datetime = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
    test_run_subdir = os.path.join(report_base_dir, f"run_{test_run_datetime}")
    os.makedirs(test_run_subdir, exist_ok=True)

    config.option.htmlpath = os.path.join(test_run_subdir, f"report_{test_run_datetime}.html")
    config.option.log_file = os.path.join(test_run_subdir, f"log_{test_run_datetime}.log")


############
# Fixtures #
############


@pytest.fixture(scope="session", autouse=True)  # Fails with scope="module" ?
def _prepare_db(django_db_setup, django_db_blocker):
    """Set up non-modified objects used by all test methods"""
    with django_db_blocker.unblock():
        # Create 1 Garden
        garden = Garden.objects.create(
            name="Test Garden",
            description="Test Garden Description",
        )

        # Create 2 GardenBeds
        garden_bed_0 = GardenBed.objects.create(
            garden=garden,
            name="Test Garden Bed 1",
            description="Test Garden Bed Description 1",
        )
        garden_bed_1 = GardenBed.objects.create(
            garden=garden,
            name="Test Garden Bed 2",
            description="Test Garden Bed Description 2",
        )
        log.info("\tGarden '%s' - garden_bed_0 '%s'", garden.name, garden_bed_0.name)
        log.info("\tGarden '%s' - garden_bed_1 '%s'", garden.name, garden_bed_1.name)

        # Create 2 Plants
        plant_0 = Plant.objects.create(
            name="Test Plant 1",
            description="Test Plant Description 1",
        )
        plant_1 = Plant.objects.create(
            name="Test Plant 2",
            description="Test Plant Description 2",
        )
        log.info("\t\tAdded plant_0 '%s'", plant_0.name)
        log.info("\t\tAdded plant_1 '%s'", plant_1.name)

        # Add plant_0 to garden_bed_0
        garden_bed_0.add_plant(plant_0, location={"x": 0, "y": 0})
        log.info("\t\tAdded plant_0 '%s' to '%s'", plant_0.name, garden_bed_0)
