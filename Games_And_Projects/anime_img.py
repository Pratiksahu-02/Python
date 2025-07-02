import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance

def create_anime_character():
    # Create a black background
    width, height = 600, 800
    image = Image.new('RGBA', (width, height), (0, 0, 0, 255))
    draw = ImageDraw.Draw(image)
    
    # Create skin tone
    skin_color = (239, 224, 205, 255)
    
    # Draw face outline
    face_width = 250
    face_height = 300
    face_left = (width - face_width) // 2
    face_top = 200
    draw.ellipse(
        (face_left, face_top, face_left + face_width, face_top + face_height),
        fill=skin_color
    )
    
    # Draw hair
    hair_color = (40, 40, 40, 255)
    hair_highlight = (100, 30, 30, 255)
    
    # Main hair
    hair_points = [
        (face_left - 20, face_top + 100),
        (face_left - 30, face_top - 20),
        (face_left + 50, face_top - 40),
        (face_left + face_width//2, face_top - 50),
        (face_left + face_width - 50, face_top - 40),
        (face_left + face_width + 30, face_top - 20),
        (face_left + face_width + 20, face_top + 100),
        (face_left + face_width + 30, face_top + 150),
        (face_left + face_width, face_top + 130),
        (face_left + face_width - 50, face_top + 20),
        (face_left + 50, face_top + 20),
        (face_left, face_top + 130),
        (face_left - 30, face_top + 150),
    ]
    draw.polygon(hair_points, fill=hair_color)
    
    # Hair spikes - top and sides
    for i in range(5):
        # Left spikes
        spike_x = face_left + 30 + i*20
        spike_y = face_top - 10
        draw.polygon([
            (spike_x, spike_y),
            (spike_x - 15, spike_y - 40 - i*5),
            (spike_x + 15, spike_y - 30 - i*3)
        ], fill=hair_color)
        
        # Right spikes
        spike_x = face_left + face_width - 30 - i*20
        draw.polygon([
            (spike_x, spike_y),
            (spike_x + 15, spike_y - 40 - i*5),
            (spike_x - 15, spike_y - 30 - i*3)
        ], fill=hair_color)
    
    # Add some hair highlights
    for i in range(3):
        highlight_x = face_left + 40 + i*30
        highlight_y = face_top + 20
        draw.line(
            [(highlight_x, highlight_y), (highlight_x + 10, highlight_y + 100)],
            fill=hair_highlight, width=5
        )
    
    # Draw closed eyes
    eye_y = face_top + 120
    eye_width = 60
    eye_height = 15
    
    # Left eye
    left_eye_x = face_left + 60
    draw.line(
        [(left_eye_x, eye_y), (left_eye_x + eye_width, eye_y)],
        fill=(0, 0, 0), width=5
    )
    
    # Right eye
    right_eye_x = face_left + face_width - 60 - eye_width
    draw.line(
        [(right_eye_x, eye_y), (right_eye_x + eye_width, eye_y)],
        fill=(0, 0, 0), width=5
    )
    
    # Draw face mask
    mask_color = (40, 40, 40, 255)
    mask_top = face_top + 150
    mask_height = 100
    
    # Main mask shape
    mask_points = [
        (face_left + 40, mask_top),
        (face_left + face_width - 40, mask_top),
        (face_left + face_width - 20, mask_top + mask_height),
        (face_left + 20, mask_top + mask_height),
    ]
    draw.polygon(mask_points, fill=mask_color)
    
    # Add mask folds/lines
    for i in range(3):
        line_y = mask_top + 25 + i*25
        draw.line(
            [(face_left + 30, line_y), (face_left + face_width - 30, line_y)],
            fill=(20, 20, 20), width=2
        )
    
    # Draw neck
    neck_top = face_top + face_height - 50
    neck_width = 80
    neck_left = (width - neck_width) // 2
    draw.rectangle(
        (neck_left, neck_top, neck_left + neck_width, neck_top + 100),
        fill=skin_color
    )
    
    # Draw shirt/clothing
    shirt_color = (40, 40, 40, 255)
    shirt_top = neck_top + 80
    shirt_width = 300
    shirt_left = (width - shirt_width) // 2
    
    draw.rectangle(
        (shirt_left, shirt_top, shirt_left + shirt_width, height),
        fill=shirt_color
    )
    
    # Add shirt collar
    collar_color = (60, 60, 60, 255)
    draw.rectangle(
        (neck_left - 20, shirt_top, neck_left + neck_width + 20, shirt_top + 30),
        fill=collar_color, outline=(30, 30, 30), width=2
    )
    
    # Add shoulder strap
    strap_color = (80, 80, 80, 255)
    strap_width = 40
    draw.rectangle(
        (shirt_left - strap_width, shirt_top + 50, shirt_left, height - 100),
        fill=strap_color
    )
    
    # Create horns on a separate layer
    horns_layer = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    horns_draw = ImageDraw.Draw(horns_layer)
    
    # Draw the base horns
    horn_color = (255, 255, 255, 200)
    
    # Left horn
    left_horn_x = face_left + 70
    left_horn_y = face_top - 20
    left_horn_points = [
        (left_horn_x, left_horn_y),
        (left_horn_x - 15, left_horn_y - 80),
        (left_horn_x + 5, left_horn_y - 100),
        (left_horn_x + 15, left_horn_y - 30),
    ]
    horns_draw.polygon(left_horn_points, fill=horn_color)
    
    # Right horn
    right_horn_x = face_left + face_width - 70
    right_horn_y = face_top - 20
    right_horn_points = [
        (right_horn_x, right_horn_y),
        (right_horn_x + 15, right_horn_y - 80),
        (right_horn_x - 5, right_horn_y - 100),
        (right_horn_x - 15, right_horn_y - 30),
    ]
    horns_draw.polygon(right_horn_points, fill=horn_color)
    
    # Apply glow effect to horns
    for i in range(10):
        horns_glow = horns_layer.copy()
        horns_glow = horns_glow.filter(ImageFilter.GaussianBlur(5 + i))
        enhancer = ImageEnhance.Brightness(horns_glow)
        horns_glow = enhancer.enhance(0.5 - i*0.03)
        
        # Tint the glow red
        glow_data = np.array(horns_glow)
        red_mask = glow_data[:,:,0] > 0
        glow_data[red_mask, 0] = np.minimum(255, glow_data[red_mask, 0] * 1.2)
        glow_data[red_mask, 1] = glow_data[red_mask, 1] * 0.4
        glow_data[red_mask, 2] = glow_data[red_mask, 2] * 0.4
        horns_glow = Image.fromarray(glow_data)
        
        # Composite the glow onto the main image
        image = Image.alpha_composite(image, horns_glow)
    
    # Add the original horns on top of the glow
    image = Image.alpha_composite(image, horns_layer)
    
    return image

# Create and save the image
anime_character = create_anime_character()
anime_character.save('anime_character_with_horns.png')

# Display the image (if running in an environment that supports it)
anime_character.show()