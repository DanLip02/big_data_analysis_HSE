import os
import psycopg2
from PIL import Image, ImageDraw, ImageFont
import subprocess

def text_to_image(text, filename):
    # Determine image size based on text lines
    lines = text.split('\n')

    try:
        font = ImageFont.truetype("Courier", 14)
    except:
        try:
            font = ImageFont.truetype("/System/Library/Fonts/Supplemental/Courier New.ttf", 14)
        except:
            font = ImageFont.load_default()


    dummy_img = Image.new('RGB', (1, 1))
    draw = ImageDraw.Draw(dummy_img)
    
    max_width = 0
    total_height = 0
    line_spacing = 4
    for line in lines:
        try:
            bbox = draw.textbbox((0, 0), line, font=font)
            w = bbox[2] - bbox[0]
            h = bbox[3] - bbox[1]
        except:
            w = len(line) * 8
            h = 14
        max_width = max(max_width, w)
        total_height += h + line_spacing

    img_width = int(max_width + 40)
    img_height = int(max_height := max(total_height + 40, 50))
    
    img = Image.new('RGB', (img_width, img_height), color=(30, 30, 30))
    draw = ImageDraw.Draw(img)
    
    y_text = 20
    for line in lines:
        draw.text((20, y_text), line, font=font, fill=(230, 230, 230))
        try:
            bbox = draw.textbbox((0, 0), line, font=font)
            h = bbox[3] - bbox[1]
        except:
            h = 14
        y_text += h + line_spacing
        
    img.save(filename)

def run():
    queries = {}
    for i in range(1, 29):
        with open(f"queries/task_{i}.sql", "r") as f:
            queries[i] = f.read()

    os.makedirs("images", exist_ok=True)
    
    conn = psycopg2.connect(dbname="danilalipatov", user="postgres", password="postgres", host="localhost", port=5430)
    conn.autocommit = True
    cur = conn.cursor()
    
    with open("HW_4_results.md", "w") as md:
        md.write("# Домашнее задание #4 (SQL)\n\n")
        
        for i in range(1, 29):
            with open("temp_query.sql", "w") as f:
                f.write(queries[i])
                
            result = subprocess.run(
                ["psql", "-h", "localhost", "-p", "5430", "-U", "postgres", "-d", "danilalipatov", "-f", "temp_query.sql"],
                env=dict(os.environ, PGPASSWORD="postgres"),
                capture_output=True, text=True
            )
            
            output = result.stdout
            if result.stderr:
                output += "\n-- Errors/Notices --\n" + result.stderr

            lines = output.split('\n')
            if len(lines) > 50:
                output = '\n'.join(lines[:45]) + f"\n\n... {len(lines)-45}"
                
            if not output.strip():
                output = "Успешно выполнено. Нет вывода."
                
            img_path = f"images/task_{i}.png"
            text_to_image(output, img_path)
            
            md.write(f"## Задание {i}\n\n")
            md.write("### Запрос:\n")
            md.write("```sql\n")
            md.write(queries[i])
            md.write("```\n\n")
            md.write("### Результат:\n")
            md.write(f"![Скриншот задания {i}](images/task_{i}.png)\n\n")
            md.write("---\n")
            
    cur.close()
    conn.close()
    
    if os.path.exists("temp_query.sql"):
        os.remove("temp_query.sql")

if __name__ == "__main__":
    run()
