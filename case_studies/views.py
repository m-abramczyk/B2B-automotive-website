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

    case_studies = list(CaseStudy.objects.filter(is_published=True).order_by('-year'))
    current_index = next((i for i, cs in enumerate(case_studies) if cs.slug == slug), None)
    prev_case_study = case_studies[current_index - 1] if current_index is not None and current_index > 0 else None
    next_case_study = case_studies[current_index + 1] if current_index is not None and current_index < len(case_studies) - 1 else None

    cover = case_study.cover if case_study else None
    expert = case_study.expert

    context = {
        'case_study': case_study,
        'prev_case_study': prev_case_study,
        'next_case_study': next_case_study,
        'cover': cover,
        'expert': expert,
    }

    return render(request, 'page-case-study-detail.html', context)