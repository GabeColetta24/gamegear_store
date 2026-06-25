from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from products.models import Product
from .forms import ReviewForm
from .models import Review


# Add a new review
@login_required
def add_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.product = product
            review.user = request.user
            review.save()
            return redirect("product_detail", product.id)
    else:
        form = ReviewForm()

    return render(
        request,
        "reviews/review_form.html",
        {
            "form": form,
            "product": product,
        },
    )


# Edit an existing review
@login_required
def edit_review(request, review_id):
    review = get_object_or_404(
        Review,
        id=review_id,
        user=request.user,
    )

    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect("product_detail", review.product.id)
    else:
        form = ReviewForm(instance=review)

    return render(
        request,
        "reviews/review_form.html",
        {
            "form": form,
            "product": review.product,
        },
    )


# Delete a review
@login_required
def delete_review(request, review_id):
    review = get_object_or_404(
        Review,
        id=review_id,
        user=request.user,
    )

    product_id = review.product.id
    review.delete()

    return redirect("product_detail", product_id)