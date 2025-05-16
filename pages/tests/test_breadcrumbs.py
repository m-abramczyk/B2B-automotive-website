import unittest
from unittest.mock import patch, Mock

from pages.context_processors import build_breadcrumbs


class TestBuildBreadcrumbs(unittest.TestCase):

    def test_homepage_returns_empty_breadcrumbs(self):
        request = Mock()
        request.path = "/en/"
        result = build_breadcrumbs(request)
        self.assertEqual(result, {"breadcrumbs": []})

    @patch("pages.context_processors.Contact")
    def test_contact_page(self, MockContact):
        request = Mock()
        request.path = "/en/contact/"

        mock_contact = Mock()
        mock_contact.menu_title = "Contact Us"
        mock_contact.get_absolute_url.return_value = "/en/contact/"
        MockContact.objects.first.return_value = mock_contact

        result = build_breadcrumbs(request)

        self.assertEqual(result["breadcrumbs"], [{
            "title": "Contact Us",
            "url": "/en/contact/"
        }])

    @patch("pages.context_processors.PrivacyPolicy")
    def test_privacy_policy_page(self, MockPrivacyPolicy):
        request = Mock()
        request.path = "/en/privacy-policy/"

        mock_privacy_policy = Mock()
        mock_privacy_policy.menu_title = "Privacy Policy"
        mock_privacy_policy.get_absolute_url.return_value = "/en/privacy-policy/"
        MockPrivacyPolicy.objects.filter.return_value.first.return_value = mock_privacy_policy

        result = build_breadcrumbs(request)

        self.assertEqual(result["breadcrumbs"], [{
            "title": "Privacy Policy",
            "url": "/en/privacy-policy/"
        }])

    @patch("pages.context_processors.Page")
    def test_page_with_slug_and_parent(self, MockPage):
        request = Mock()
        request.path = "/en/services/swimming/"

        # Simulate two-level path: 'services' -> 'swimming'
        mock_services = Mock()
        mock_services.menu_title = "Services"
        mock_services.get_absolute_url.return_value = "/en/services/"
        mock_swimming = Mock()
        mock_swimming.menu_title = "Swimming"
        mock_swimming.get_absolute_url.return_value = "/en/services/swimming/"

        # Page.objects.get() gets called twice with different parents
        MockPage.objects.get.side_effect = [mock_services, mock_swimming]

        result = build_breadcrumbs(request)

        self.assertEqual(result["breadcrumbs"], [
            {"title": "Services", "url": "/en/services/"},
            {"title": "Swimming", "url": "/en/services/swimming/"},
        ])

    @patch("pages.context_processors.CaseStudy")
    @patch("pages.context_processors.Page")
    def test_case_study_page(self, MockPage, MockCaseStudy):
        request = Mock()
        request.path = "/en/company/case-studies/zeekr-x/"

        # Simulate Index parent
        mock_company = Mock()
        mock_company.menu_title = "Company"
        mock_company.get_absolute_url.return_value = "/en/company/"

        mock_index_page = Mock()
        mock_index_page.menu_title = "Case Studies"
        mock_index_page.get_absolute_url.return_value = "/en/company/case-studies/"
        mock_index_page.is_case_studies_index = True

        MockPage.DoesNotExist = type('DoesNotExist', (Exception,), {})
        MockPage.objects.get.side_effect = [mock_company, mock_index_page, MockPage.DoesNotExist()]

        mock_case_study = Mock()
        mock_case_study.menu_title = "Zeekr X"
        mock_case_study.get_absolute_url.return_value = "/en/company/case-studies/zeekr-x/"
        MockCaseStudy.objects.filter.return_value.first.return_value = mock_case_study

        result = build_breadcrumbs(request)

        self.assertEqual(result["breadcrumbs"], [
            {"title": "Company", "url": "/en/company/"},
            {"title": "Case Studies", "url": "/en/company/case-studies/"},
            {"title": "Zeekr X", "url": "/en/company/case-studies/zeekr-x/"},
        ])


if __name__ == "__main__":
    unittest.main()