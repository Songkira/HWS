@require_POST
def follow(request, __(a)__):
    if request.user.is_authenticated:
        you = get_object_or_404(get_user_model(), pk=__(a)__)
        me = request.user

        if you != me:
            if you.__(b)__.__(c)__(pk=me.pk).exists():
                you.__(b)__.__(d)__(me)
            else:
                you.__(b)__.__(e)__(me)
        return redirect('accounts:profile', you.username)
    return redirect('accounts:login')