from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from . import models


# Create your views here.


def main_page_red(request):
    return redirect('/ru')


def main_page(request, pk):
    ads = models.Ad.objects.all()

    all_ru_categories = models.Category.objects.all()

    all_shops = models.Shop.objects.all()

    all_stars_ru = models.Star.objects.all()

    all_leads_ru = models.Leading.objects.all()

    all_duty_artists_ru = models.DutyArtist.objects.all()

    all_others_ru = models.Other.objects.all()

    context = {'all_ru_categories': all_ru_categories, 'all_leads_ru': all_leads_ru,
               'all_stars_ru': all_stars_ru, 'all_duty_artists_ru': all_duty_artists_ru,
               'all_others_ru': all_others_ru, 'all_shops': all_shops, 'ads': ads}

    if pk == 'ru':
        return render(request, 'indexru.html', context)

    elif pk == 'uz':
        return render(request, 'indexuz.html', context)


def get_all_catalog(request):
    ad = models.AdCatalog.objects.all()
    all_categories = models.Card.objects.all()
    all_ru_categories = models.Category.objects.all()

    for i in all_categories:
        i.count += 1
        i.save()

    paginator = Paginator(all_categories, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"page_obj": page_obj, 'all_ru_categories': all_ru_categories, 'ad': ad}

    return render(request, 'catalog.html', context)


def get_all_catalog_uz(request):
    ad = models.AdCatalog.objects.all()
    all_categories = models.Card.objects.all()
    all_ru_categories = models.Category.objects.all()

    for i in all_categories:
        i.count += 1
        i.save()

    paginator = Paginator(all_categories, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"page_obj": page_obj, 'all_ru_categories': all_ru_categories, 'ad': ad}

    return render(request, 'cataloguz.html', context)


def catalog_page_ru(request, pk):
    all_ru_categories = models.Category.objects.all()
    current_category = models.Category.objects.get(name_ru=pk)
    current_category.count += 1
    current_category.save()

    if pk != current_category:
        pass

    else:
        try:
            other_category = models.Other.objects.get(name_ru=pk)
            other_category.count += 1
            other_category.save()

        except:
            shop = models.Shop.objects.get(name_ru=pk)
            shop.count += 1
            shop.save()

    all_ru_cards = models.Card.objects.filter(category_name=current_category)
    for i in all_ru_cards:
        i.count += 1
        i.save()

    paginator = Paginator(all_ru_cards, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"page_obj": page_obj, 'all_ru_categories': all_ru_categories, 'category': current_category}

    return render(request, 'catalog.html', context)


def catalog_page_uz(request, pk):
    all_ru_categories = models.Category.objects.all()
    current_category = models.Category.objects.get(name_uz=pk)
    current_category.count += 1
    current_category.save()

    if pk != current_category:
        pass

    else:

        try:
            other_category = models.Other.objects.get(name_uz=pk)
            other_category.count += 1
            other_category.save()

        except:
            shop = models.Shop.objects.get(name_uz=pk)
            shop.count += 1
            shop.save()

    all_ru_cards = models.Card.objects.filter(category_name=current_category)
    for i in all_ru_cards:
        i.count += 1
        i.save()

    paginator = Paginator(all_ru_cards, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"page_obj": page_obj, 'all_ru_categories': all_ru_categories, 'category': current_category}

    return render(request, 'cataloguz.html', context)


def get_all_stars(request):
    all_ru_categories = models.Category.objects.all()
    all_stars = models.Star.objects.all()

    for i in all_stars:
        i.count += 1
        i.save()

    paginator = Paginator(all_stars, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"page_obj": page_obj, 'all_ru_categories': all_ru_categories}

    return render(request, 'all_stars_ru.html', context)


def get_all_stars_uz(request):
    all_ru_categories = models.Category.objects.all()
    all_stars = models.Star.objects.all()

    for i in all_stars:
        i.count += 1
        i.save()

    paginator = Paginator(all_stars, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"page_obj": page_obj, 'all_ru_categories': all_ru_categories}

    return render(request, 'all_stars_uz.html', context)


# def get_current_star(request, pk):
#     all_ru_categories = models.Category.objects.all()
#     all_stars = models.Star.objects.all()
#
#     paginator = Paginator(all_stars, 10)
#     page_number = request.GET.get("page")
#     page_obj = paginator.get_page(page_number)
#
#     context = {"page_obj": page_obj, 'all_ru_categories': all_ru_categories}
#
#     return render(request, 'all_stars_ru.html', context)


def get_all_leading_ru(request):
    all_ru_categories = models.Category.objects.all()
    all_leads = models.Leading.objects.all()

    for i in all_leads:
        i.count += 1
        i.save()

    paginator = Paginator(all_leads, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"page_obj": page_obj, 'all_ru_categories': all_ru_categories}

    return render(request, 'all_leads_ru.html', context)


def get_all_leading_uz(request):
    all_ru_categories = models.Category.objects.all()
    all_leads = models.Leading.objects.all()

    for i in all_leads:
        i.count += 1
        i.save()

    paginator = Paginator(all_leads, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"page_obj": page_obj, 'all_ru_categories': all_ru_categories}

    return render(request, 'all_leads_uz.html', context)


def get_all_duty_artists_ru(request):
    all_ru_categories = models.Category.objects.all()
    all_duty_stars = models.DutyArtist.objects.all()
    for i in all_duty_stars:
        i.count += 1
        i.save()

    paginator = Paginator(all_duty_stars, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"page_obj": page_obj, 'all_ru_categories': all_ru_categories}

    return render(request, 'all_duty_stars_ru.html', context)


def get_all_duty_artists_uz(request):
    all_ru_categories = models.Category.objects.all()
    all_duty_stars = models.DutyArtist.objects.all()
    for i in all_duty_stars:
        i.count += 1
        i.save()

    paginator = Paginator(all_duty_stars, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {"page_obj": page_obj, 'all_ru_categories': all_ru_categories}

    return render(request, 'all_duty_stars_uz.html', context)


def get_current_card_ru(request, pk):
    all_ru_categories = models.Category.objects.all()
    current_card = models.Card.objects.filter(Q(card_name_ru__icontains=pk))
    for i in current_card:
        i.count += 1
        i.save()

    category = models.Card.objects.get(card_name_ru=pk)
    category.count += 1
    category.save()

    paginator = Paginator(current_card, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'current_card_ru.html', {'page_obj': page_obj, 'all_ru_categories': all_ru_categories,
                                                    'category': category})


def get_current_card_uz(request, pk):
    all_ru_categories = models.Category.objects.all()
    current_card = models.Card.objects.filter(Q(card_name_uz__icontains=pk))
    for i in current_card:
        i.count += 1
        i.save()

    category = models.Card.objects.get(card_name_uz=pk)
    category.count += 1
    category.save()

    paginator = Paginator(current_card, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'current_card_uz.html', {'page_obj': page_obj, 'all_ru_categories': all_ru_categories,
                                                    'category': category})


def get_current_star_ru(request, pk):
    all_ru_categories = models.Category.objects.all()
    current_star = models.Star.objects.filter(Q(name_ru__icontains=pk))
    for i in current_star:
        i.count += 1
        i.save()

    category = models.Star.objects.get(name_ru=pk)
    category.count += 1
    category.save()

    paginator = Paginator(current_star, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'current_star_ru.html', {'page_obj': page_obj, 'all_ru_categories': all_ru_categories,
                                                    'category': category})


def get_current_star_uz(request, pk):
    all_ru_categories = models.Category.objects.all()
    current_star = models.Star.objects.filter(Q(name_uz__icontains=pk))
    for i in current_star:
        i.count += 1
        i.save()

    category = models.Star.objects.get(name_uz=pk)
    category.count += 1
    category.save()

    paginator = Paginator(current_star, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'current_star_uz.html', {'page_obj': page_obj, 'all_ru_categories': all_ru_categories,
                                                    'category': category})


def get_current_lead_ru(request, pk):
    all_ru_categories = models.Category.objects.all()
    current_leads = models.Leading.objects.filter(Q(name_ru__icontains=pk))
    for i in current_leads:
        i.count += 1
        i.save()

    category = models.Leading.objects.get(name_ru=pk)
    category.count += 1
    category.save()

    paginator = Paginator(current_leads, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'current_lead_ru.html', {'page_obj': page_obj, 'all_ru_categories': all_ru_categories,
                                                    'category': category})


def get_current_lead_uz(request, pk):
    all_ru_categories = models.Category.objects.all()
    current_leads = models.Leading.objects.filter(Q(name_uz__icontains=pk))
    for i in current_leads:
        i.count += 1
        i.save()

    category = models.Leading.objects.get(name_uz=pk)
    category.count += 1
    category.save()

    paginator = Paginator(current_leads, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'current_lead_uz.html', {'page_obj': page_obj, 'all_ru_categories': all_ru_categories,
                                                    'category': category})


def get_current_duty_artist_ru(request, pk):
    all_ru_categories = models.Category.objects.all()
    current_duty = models.DutyArtist.objects.filter(Q(name_ru__icontains=pk))
    for i in current_duty:
        i.count += 1
        i.save()

    category = models.DutyArtist.objects.get(name_ru=pk)
    category.count += 1
    category.save()

    paginator = Paginator(current_duty, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'current_duty_artist_ru.html', {'page_obj': page_obj, 'all_ru_categories': all_ru_categories,
                                                            'category': category})


def get_current_duty_artist_uz(request, pk):
    all_ru_categories = models.Category.objects.all()
    current_duty = models.DutyArtist.objects.filter(Q(name_uz__icontains=pk))
    for i in current_duty:
        i.count += 1
        i.save()

    category = models.DutyArtist.objects.get(name_uz=pk)
    category.count += 1
    category.save()

    paginator = Paginator(current_duty, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, 'current_duty_artist_uz.html', {'page_obj': page_obj, 'all_ru_categories': all_ru_categories,
                                                            'category': category})


def count_ads(request):
    if request.method == 'POST':
        pk = request.POST.get('id')
        current_ad = models.Ad.objects.get(id=pk)
        current_ad.count += 1
        current_ad.save()

        return redirect(f'{current_ad.url}')


def count_ads_catalog(request):
    if request.method == 'POST':
        pk = request.POST.get('id')
        current_ad = models.AdCatalog.objects.get(id=pk)
        current_ad.count += 1
        current_ad.save()

        return redirect(f'{current_ad.url}')


def search_catalog_ru(request):
    if request.method == 'POST':
        try:
            searching_for = request.POST.get('q')
            current_card = models.Card.objects.get(card_name_ru=searching_for)
            current_card.count += 1
            current_card.save()

            return redirect(f"ru/card/{current_card}")

        except:
            return redirect("/ru/all-catalogs")


def search_catalog_uz(request):
    if request.method == 'POST':
        try:
            searching_for = request.POST.get('q')
            current_card = models.Card.objects.get(card_name_uz=searching_for)
            current_card.count += 1
            current_card.save()

            return redirect(f"uz/card/{current_card}")

        except:
            return redirect(f"/uz/all-catalogs")


def search_star_ru(request):
    if request.method == 'POST':
        try:
            searching_for = request.POST.get('q')
            current_card = models.Star.objects.get(name_ru=searching_for)
            current_card.count += 1
            current_card.save()

            return redirect(f"ru/star/{current_card}")

        except:
            return redirect(f"ru/catalog/all-stars")


def search_star_uz(request):
    if request.method == 'POST':
        try:
            searching_for = request.POST.get('q')
            current_card = models.Star.objects.get(name_uz=searching_for)
            current_card.count += 1
            current_card.save()

            return redirect(f"uz/star/{current_card}")

        except:
            return redirect(f"uz/catalog/all-stars")


def search_leads_ru(request):
    if request.method == 'POST':
        try:
            searching_for = request.POST.get('q')
            current_card = models.Leading.objects.get(name_ru=searching_for)
            current_card.count += 1
            current_card.save()

            return redirect(f"ru/lead/{current_card}")

        except:
            return redirect(f"/ru/catalog/all-leads")


def search_leads_uz(request):
    if request.method == 'POST':
        try:
            searching_for = request.POST.get('q')
            current_card = models.Leading.objects.get(name_uz=searching_for)
            current_card.count += 1
            current_card.save()

            return redirect(f"uz/lead/{current_card}")

        except:
            return redirect(f"uz/catalog/all-leads")


def search_duty_artists_ru(request):
    if request.method == 'POST':
        try:
            searching_for = request.POST.get('q')
            current_card = models.DutyArtist.objects.get(name_ru=searching_for)
            current_card.count += 1
            current_card.save()

            return redirect(f"ru/duty-artist/{current_card}")

        except:
            return redirect(f"ru/catalog/all-duty-artists")


def search_duty_artists_uz(request):
    if request.method == 'POST':
        try:
            searching_for = request.POST.get('q')
            current_card = models.DutyArtist.objects.get(name_uz=searching_for)
            current_card.count += 1
            current_card.save()

            return redirect(f"uz/duty-artist/{current_card}")

        except:
            return redirect(f"uz/catalog/all-duty-artists")