from django.shortcuts import render, get_object_or_404
from django.http import StreamingHttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Food, Cart, CartItem
import cv2
import mediapipe as mp
import pyautogui

# Hand tracking setup
capture_hands = mp.solutions.hands.Hands()
drawing_option = mp.solutions.drawing_utils
screen_width, screen_height = pyautogui.size()

def gen_frames():
    camera = cv2.VideoCapture(0)
    x1 = y1 = x2 = y2 = 0

    while True:
        success, image = camera.read()
        if not success:
            break
        else:
            image_height, image_width, _ = image.shape
            image = cv2.flip(image, 1)
            rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            output_hands = capture_hands.process(rgb_image)
            all_hands = output_hands.multi_hand_landmarks

            if all_hands:
                for hand in all_hands:
                    drawing_option.draw_landmarks(image, hand)
                    one_hand_landmarks = hand.landmark
                    for id, lm in enumerate(one_hand_landmarks):
                        x = int(lm.x * image_width)
                        y = int(lm.y * image_height)
                        if id == 8:
                            mouse_x = int(screen_width / image_width * x)
                            mouse_y = int(screen_height / image_height * y)
                            cv2.circle(image, (x, y), 10, (0, 255, 255), -1)
                            pyautogui.moveTo(mouse_x, mouse_y)
                            x1 = x
                            y1 = y
                        if id == 4:
                            x2 = x
                            y2 = y
                            cv2.circle(image, (x, y), 10, (0, 255, 255), -1)
                dist = y2 - y1
                if dist < 20:
                    pyautogui.click()

            ret, buffer = cv2.imencode('.jpg', image)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    camera.release()
    cv2.destroyAllWindows()

def video_feed(request):
    return StreamingHttpResponse(gen_frames(), content_type='multipart/x-mixed-replace; boundary=frame')

def food_list(request):
    foods = Food.objects.all()
    foods_by_category = {}
    for category, _ in Food.CATEGORIES:
        foods_by_category[category] = foods.filter(category=category)
    return render(request, 'list.html', {'foods_by_category': foods_by_category})

def food_detail(request, slug):
    food_detail = get_object_or_404(Food, slug=slug)
    context = {
        "food_detail": food_detail
    }
    return render(request, 'detail.html', context)

def add_to_cart(request):
    if request.method == 'POST':
        food_id = request.POST.get('food_id')
        food = get_object_or_404(Food, pk=food_id)
        # Add item to cart logic here
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})
