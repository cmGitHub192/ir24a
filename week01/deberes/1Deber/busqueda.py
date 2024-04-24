from flask import Flask, render_template, request, jsonify
import os
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    keyword = request.args.get('keyword')

    # Directorio donde se encuentran los archivos TXT
    directory = 'libros' 

    # Lista para almacenar los resultados
    results = []

    # Búsqueda de la palabra en todos los archivos TXT
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
                occurrences = re.findall(r'\b' + re.escape(keyword) + r'\b', content, re.IGNORECASE)
                if occurrences:
                    results.append({
                        'filename': filename,
                        'occurrences': len(occurrences),
                        'keywords': ', '.join(occurrences)
                    })

    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)
