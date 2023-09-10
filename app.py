from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data for blog posts (you can replace this with a database later)
blog_posts = [
    {
        'title': 'First Post',
        'content': 'This is the content of the first post.'
    },
    {
        'title': 'Second Post',
        'content': 'This is the content of the second post.'
    }
]

@app.route('/')
def index():
    return render_template('index.html', posts=blog_posts)

@app.route('/add_post', methods=['GET', 'POST'])
def add_post():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        new_post = {'title': title, 'content': content}
        blog_posts.append(new_post)
        return redirect(url_for('index'))
    return render_template('add_post.html')

if __name__ == '__main__':
    app.run(debug=True)
