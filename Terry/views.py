from django.shortcuts               import render, redirect
from django.http                    import JsonResponse
from django.contrib.auth.decorators import login_required
from .models                        import UserProfile
from django.utils.timezone          import now

import random


@login_required
def Gameover(request):
    profile = UserProfile.objects.get(user = request.user)

    return render(request,'db/gameover.html')

@login_required
def Terry(request):
    profile = UserProfile.objects.get(user=request.user)

    if profile.lives == 0:

        return redirect('/Terry/Gameover/')

    background_image = 'Spacedanger.gif' if profile.lives < 3 else 'Space.png'
    skin_image = f"{profile.active_skin.split('.')[0]}-bad.gif" if profile.lives < 3 else f"{profile.active_skin.split('.')[0]}.gif"

    context = {
        'profile': profile,
        'active_skin': skin_image,
        'background_image': background_image,
    }
    return render(request, 'db/mainterry.html', context)







@login_required
def Consejos(request):

    profile = UserProfile.objects.get(user=request.user)

    if profile.lives == 0:
        return redirect('/Terry/')
    
    context = {
        'profile': profile
    }
    return render(request, 'db/consejos.html', context)





@login_required
def Trivia(request):
    profile = UserProfile.objects.get(user=request.user)
    background_image = 'Spacedanger.gif' if profile.lives < 3 else 'Space.png'
    skin_image = f"{profile.active_skin.split('.')[0]}-bad.gif" if profile.lives < 3 else f"{profile.active_skin.split('.')[0]}.gif"
    
    
    if profile.lives == 0:
        return redirect('/Terry/')

    if request.method == 'POST':
        
        is_correct = request.GET.get('correct') == 'true'

        


        
        if is_correct:
                
            profile.trivias_completed        += 1
            profile.consecutive_trivias      += 1
            profile.last_trivia_date          = now().date()
            profile.consecutive_failedtrivias = 0

                
            if profile.consecutive_trivias          >= 5:
                profile.lives                        = min(5, profile.lives + 1)  
                profile.consecutive_trivias          = 0  


        else:
                
            profile.consecutive_trivias        = 0
            profile.consecutive_failedtrivias += 1

            if profile.consecutive_failedtrivias >= 2:
                profile.lives                     = max(0, profile.lives - 1)
                profile.consecutive_failedtrivias = 0
        
        
        profile.save()

        return JsonResponse({'status': 'success' if is_correct else 'failure'})

    # Lista de preguntas
    preguntas = [
        {
            "question": "¿Qué es el cambio climático?",
            "options": [
                {"text": "Un cambio temporal del clima en una región", "is_correct": False},
                {"text": "Variaciones prolongadas en el clima global debido a causas naturales", "is_correct": False},
                {"text": "Cambios significativos y duraderos en el clima provocados principalmente por actividades humanas", "is_correct": True}
            ]
        },
        {
            "question": "¿Qué impacto tiene el cambio climático en la agricultura?",
            "options": [
                {"text": "Aumenta la fertilidad del suelo y mejora la producción", "is_correct": False},
                {"text": "Afecta las cosechas por sequías y eventos climáticos extremos", "is_correct": True},
                {"text": "No tiene efectos sobre los cultivos", "is_correct": False}
            ]
        },
        {
            "question": "¿Cuál es una forma efectiva de mitigar el cambio climático?",
            "options": [
                {"text": "Utilizar más combustibles fósiles para aumentar la producción de energía", "is_correct": False},
                {"text": "Reducir la deforestación y utilizar fuentes de energía renovable", "is_correct": True},
                {"text": "Dejar de utilizar vehículos eléctricos y volver a los combustibles tradicionales", "is_correct": False}
            ]
        },
        {
            "question": "¿Qué efecto tiene el cambio climático en los océanos?",
            "options": [
                {"text": "Aumenta la temperatura y acidifica el agua dañando la vida marina", "is_correct": True},
                {"text": "Enfría los océanos, mejorando la biodiversidad", "is_correct": False},
                {"text": "No tiene un impacto directo en los océanos", "is_correct": False}
            ]
        },
        {
            "question": "¿Cómo puede afectar el cambio climático la salud humana?",
            "options": [
                {"text": "Reduce la incidencia de enfermedades respiratorias", "is_correct": False},
                {"text": "Aumenta el riesgo de enfermedades debido a las olas de calor y contaminación del aire", "is_correct": True},
                {"text": "Mejora la calidad del aire y disminuye la expansión de enfermedades", "is_correct": False}
            ]
        },
        {
            "question": "¿Qué consecuencias tiene el aumento del nivel del mar?",
            "options": [
                {"text": "Mejora la calidad de las costas y genera más espacios para playas", "is_correct": False},
                {"text": "Amenaza las comunidades costeras y causa inundaciones", "is_correct": True},
                {"text": "No tiene efectos notables en las zonas costeras", "is_correct": False}
            ]
        },
    ]

    
    pregunta_actual = random.choice(preguntas)
    
    context = {
        'profile': profile,
        'question_text': pregunta_actual['question'],
        'options': pregunta_actual['options'],
        'active_skin': skin_image,
        'background_image': background_image,
    }
    return render(request, 'db/trivia.html', context)







@login_required
def Skins(request):
    
    profile = UserProfile.objects.get(user=request.user)

    if profile.lives == 0:
        return redirect('/Terry/')
    
    context = {
        'trivias_completed': profile.trivias_completed,  
        'active_skin': profile.active_skin,              
    }
    return render(request, 'db/skins.html', context)






@login_required
def SeleccionarSkin(request, skin_name):

    profile = UserProfile.objects.get(user=request.user)
    
    if skin_name == "Pinguino.gif" and profile.trivias_completed < 5:
        return HttpResponse("No tienes suficientes trivias completadas para esta skin.", status=403)
    

    if skin_name == "Deathstarskin.gif" and profile.trivias_completed < 10:
        return HttpResponse("No tienes suficientes trivias completadas para esta skin.", status=403)
    
    
    profile.active_skin = skin_name
    profile.save()

    return render(request, 'db/skins.html', {'profile': profile, 'trivias_completed': profile.trivias_completed})