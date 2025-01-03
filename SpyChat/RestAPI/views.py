from django.shortcuts import redirect, render

from .forms import PictureForm

def uploadForm(req):
    if req.method == 'POST':
        form = PictureForm(req.POST, req.FILES)
        if form.is_valid(): 
            form.save()
            return redirect('/admin')
            #  handle_uploaded_file(request.FILES["file"])
        else:
            context = {'form': form}
            return render(req, 'upload.html', context)
    context = {'form': PictureForm()}
    return render(req, 'upload.html', context)

