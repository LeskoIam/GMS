import os
from datetime import datetime

import pytest


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
