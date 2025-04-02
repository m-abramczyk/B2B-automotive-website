from itertools import chain
from django.db.models import Prefetch

from django.utils.translation import gettext as _
from django.shortcuts import render, get_object_or_404
from django.http import Http404

from pages.models import Page
from .models import CaseStudy, Section, SectionImage


def case_study_detail(request, parent_slug, slug):

    # Resolving parent URL
    case_studies_index = get_object_or_404(Page, is_case_studies_index=True, is_published=True)
    if case_studies_index.parent:
        parent = get_object_or_404(Page, slug=parent_slug)
        if parent != case_studies_index.parent:
            raise Http404("Invalid parent page for the case study.")

    # Prefetch ordered sections and their related images
    sections_qs = Section.objects.prefetch_related(
        Prefetch('section_images', queryset=SectionImage.objects.order_by('order'))
    ).order_by('order')

    case_study = get_object_or_404(
        CaseStudy.objects.prefetch_related(
            Prefetch('sections', queryset=sections_qs)
        ),
        slug=slug,
    )

    case_studies = list(CaseStudy.objects.filter(is_published=True).order_by('-year'))
    current_index = next((i for i, cs in enumerate(case_studies) if cs.slug == slug), None)
    if current_index is not None:
        prev_case_study = case_studies[current_index - 1] if current_index > 0 else case_studies[-1]
        next_case_study = case_studies[current_index + 1] if current_index < len(case_studies) - 1 else case_studies[0]
    else:
        prev_case_study = None
        next_case_study = None

    cover = case_study.cover if case_study else None
    expert = case_study.expert
    case_study_labels = case_study.labels.order_by('order')
    case_study_data = case_study.data_items.order_by('order')
    sections = case_study.sections.all()
    all_images = list(chain(*[section.section_images.all() for section in sections]))
    meta_title = case_study.meta_title if case_study.meta_title else case_study.menu_title.rstrip(":")
    meta_description = case_study.meta_description

    context = {
        'case_study': case_study,
        'prev_case_study': prev_case_study,
        'next_case_study': next_case_study,
        'cover': cover,
        'expert': expert,
        'case_study_labels': case_study_labels,
        'case_study_data': case_study_data,
        'sections': sections,
        'all_images': all_images,
        'meta_title': meta_title,
        'meta_description': meta_description,
    }

    return render(request, 'page-case-study-detail.html', context)