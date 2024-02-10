from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/article')
def article_catalog():
    return render_template('index.html')

@app.route('/ad')
def ad():
    return "Nah not really rofl"


@app.route('/journalist')
def journoids():
    journalists = [
        {'name': 'John Doe', 'id': 'JohnDoe', 'articles': 10, 'reliability': 'High', 'bio': 'A brief biography for Journalist 1.'},
        {'name': 'Jane Smith', 'id': 'JaneSmith', 'articles': 15, 'reliability': 'Medium', 'bio': 'A brief biography for Journalist 2.'},
        # Add more journalists as needed
    ]

    return render_template('journoids.html', journalists=journalists)

@app.route('/journalist/<string:journalist_name>')
def journalist(journalist_name):
    # Simulated data for demonstration
    journalists = [
        {'name': 'John Doe',
         'id': 'JohnDoe',
        'articles_count': 10, 
        'reads_count': 500, 
        'rating': 4.5, 
        'bio': "John Doe, the extraordinary wordsmith and master storyteller, has crafted a literary legacy "
            "that spans across the vast realms of journalism. With an awe-inspiring count of 120 articles "
            "and a readership soaring to an astounding 5000, John stands tall as a prolific writer who "
            "weaves words into captivating narratives. Renowned across various platforms and news networks, "
            "he has etched his name in the annals of storytelling history.\n\n"
            "Not just a wordsmith, John Doe has an impressive track record that reads like a novel itself. "
            "His journey through the corridors of news has been nothing short of epic, and his relentless "
            "pursuit of truth has earned him a remarkable 4.8 rating. At the seasoned age of 50, John continues "
            "to inspire with his literary prowess, all while sharing his New York abode with his faithful canine companion.", 
        'affiliation': 'BBC News: 1984 to present', 
        'education': 'University of Wakanda: 2003-2007', 
        'pfp': 'images/journalists/img1.jpg'},


        {'name': 'Jane Smith', 
         'id': 'JaneSmith',
         'articles_count': 15, 
         'reads_count': 700, 
         'rating': 3.8, 
         'bio': 'Jane Smith is an amateur writer who took it up as a passion and is constantly learning new things. Although her views may be controversial, she still gets greater reach due to her literary acumen. She is 60 years old and lives with cats in Seattle', 
         'affiliation': 'Freelance "Journalist": 2001 to present', 
         'education': 'Self Taught University: 2003-2007', 
         'pfp': 'images/journalists/img2.jpg'},
        # Add more journalists as needed
    ]

    # Find the journalist with the specified name
    journalist = next((j for j in journalists if j['name'].replace(" ", "") == journalist_name), None)

    if journalist:
        return render_template('profile.html', journalist=journalist)
    else:
        # Handle the case where the journalist is not found
        return "Journalist not found", 404


@app.route('/article/<source>')
def show_article(source):
    # Construct the JSON file path
    json_file_path = 'templates/articles/all_articles.json'

    try:
        # Read the JSON file
        with open(json_file_path, 'r') as file:
            all_articles = json.load(file)
        
        # Get the specific article based on the source
        article_data = all_articles.get(source)
        
        if not article_data:
            raise KeyError(f"Article not found for source: {source}")

    except (FileNotFoundError, KeyError) as e:
        return f"Error: {e}"

    return render_template('articles/article_template.html', article=article_data)


if __name__ == '__main__':
    app.run(debug=True)
