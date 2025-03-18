from django.utils.translation import gettext as _
from django.shortcuts import render, get_object_or_404
from django.http import Http404

from pages.models import Page
from .models import CaseStudy


def case_study_detail(request, parent_slug, slug):

    case_studies_index = get_object_or_404(Page, is_case_studies_index=True, is_published=True)
    if case_studies_index.parent:
        parent = get_object_or_404(Page, slug=parent_slug)
        if parent != case_studies_index.parent:
            raise Http404("Invalid parent page for the case study.")

    case_study = get_object_or_404(CaseStudy, slug=slug, is_published=True)
    # cover = page.cover.first() if page else None
    expert = case_study.expert
    label = expert.label if expert else None

    context = {
        'case_study': case_study,
        # 'cover': cover,
        'expert': expert,
        'label': label,
    }

    return render(request, 'page-case-study-detail.html', context)